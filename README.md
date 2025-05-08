# Real-time Cryptocurrency Tracker

## Overview

This project is a real-time cryptocurrency price tracker that displays the current prices of the top 10 cryptocurrencies (by market cap). It fetches data from the CoinGecko API, 
stores it in a Django database, and uses WebSockets (via Django Channels) to push live updates to the user's browser. The front-end is built with basic HTML and Bootstrap for styling,
with JavaScript to handle the WebSocket connection and update the displayed data dynamically.

## Features

* **Real-time Price Updates:** Prices are updated live in the browser as data changes on the server.
* **Top 10 Cryptocurrencies:** Tracks the top 10 cryptocurrencies by market capitalization.
* **Price Change Indication:** Indicates whether the price of a cryptocurrency has gone up (green), down (red), or stayed the same (black).
* **Simple and Responsive UI:** Built with Bootstrap for basic styling and responsiveness.

## Technologies Used

* **Backend:**
    * Python 3
    * Django
    * Django Channels (for WebSockets)
    * Celery (for background task scheduling)
    * Redis (as the Channel Layer and Celery broker)
    * requests (for making HTTP requests to the CoinGecko API)
    * SQLite (for development database)
* **Frontend:**
    * HTML5
    * CSS3
    * Bootstrap
    * JavaScript
    * jQuery (for DOM manipulation)

## Prerequisites

Before you begin, ensure you have the following installed:

* Python 3
* pip (Python package installer)
* Redis (server should be running)

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone REPOSITORY_URL
    ```

2.  **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    # venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (optional but recommended for Django admin):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the Django development server:**
    ```bash
    python manage.py runserver
    ```
    Open your browser and navigate to `http://127.0.0.1:8000/cryptos/`.
    (Note: using Asgi/Daphne)
  
    
7.  **Run the Celery worker (in yet another separate terminal):**
    ```bash
    celery -A crypto_tracker worker -l info 
    ```
    
8.  **Run the Celery Beat (in yet another separate terminal):**
    ```bash
    celery -A crypto_tracker beat -l info 
    ```

## Usage

Once all the servers are running, navigate to `http://127.0.0.1:8000/cryptos/` in your web browser. You should see a table displaying the top 10 cryptocurrencies with their
real-time prices and state indicators. The "Last Updated" field will show the time of the latest update received via WebSocket.
