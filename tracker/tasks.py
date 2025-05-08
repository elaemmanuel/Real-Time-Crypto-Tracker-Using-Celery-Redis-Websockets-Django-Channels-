from celery import shared_task
import requests
from .models import Coin
from asgiref.sync import AsyncToSync
from channels.layers import get_channel_layer
import time

channel_layer = get_channel_layer()

@shared_task
def fetch_crypto_data():
    try:
        url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=false"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        coins_data_for_websocket = []

        # Save data to the database
        for item in data:
            try:
                coin, created = Coin.objects.get_or_create(
                    symbol=item['symbol'].upper(),
                    defaults={
                        'rank': item['market_cap_rank'],
                        'name': item['name'],
                        'price': item['current_price'],
                    }
                )
                old_price = coin.price
                new_price = item['current_price']
                if new_price > old_price:
                    coin.state = 'Up'
                elif new_price < old_price:
                    coin.state = 'Fall'
                else:
                    coin.state = 'Stable'
                coin.price = new_price
                coin.rank = item['market_cap_rank'] # Update rank as well
                coin.save()
                print(f"Updated {coin.name} ({coin.symbol}) - Price: {coin.price}, Rank: {coin.rank}, State: {coin.state}")
                coins_data_for_websocket.append({
                    'symbol': coin.symbol,
                    'name': coin.name,
                    'current_price': float(coin.price),
                    'market_cap_rank': coin.rank,
                    'state': coin.state
                })
                time.sleep(0.3) # Add a delay of 0.3 seconds between processing each coin
            except Exception as e:
                print(f"Error saving/updating {item['name']} ({item['symbol']}): {e}")
            time.sleep(0.2) # Add a small delay after each coin processing

        print("Data fetched and saved/updated successfully.")

        AsyncToSync(channel_layer.group_send)('crypto_updates', {'type': 'crypto_price_update', 'message': coins_data_for_websocket})

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from CoinGecko: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")