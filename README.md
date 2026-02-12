# Binance Futures CLI Trading Bot
 A simplified, modular Python application designed to place orders on the Binance Futures Testnet(USDT-M). This project demonstrates professional backend practices including input validation ans structured logging.

 # Features
  **> Order Types:** Supports both MARKET and LIMIT orders.
  
  **> Trading Sides:** Supports both BUY(Long) and SELL(Short) positions.
  
  **>Direct API Integration:** Uses the requests library with manual HMAC SHA256 signing for secure communication with Binance.

  **>Robust Validation:** CLI-level and logic-level validation for symbols, quantities, and prices.

  **>Professional Logging:** Rotating logs to capture request payloads, API responses, and error details.

  **>Enhanced UX:** Color-coded terminal output for successful and failed operations.

# Project Structure
    trading_bot/
    ├── bot/
    │   ├── __init__.py
    │   ├── client.py          # API wrapper
    │   ├── orders.py          # Order placement execution
    │   ├── validators.py      # Input and business logic validation
    │   └── logging_config.py  # Centralized rotating logger setup
    ├── cli.py                 # Command Line Interface entry point
    ├── requirements.txt       # Project dependencies
    └── .env                   # API Credentials (local only)

# Prerequisites
  ->Python 3.x
  
  ->Binance Futures Testnet Account
  
  ->Testnet API Key and Secret Key

# Installation
   Clone the project directory.

        git clone https://github.com/Jiya112005/Binance_Trade_Bot.git
   
   Create a Virtual Environment:
    
    bash
    python -m venv venv

# Activate the Environment:

    Windows: .\venv\Scripts\activate

    Mac/Linux: source venv/bin/activate

# Install Dependencies:
    bash
    pip install -r requirements.txt

# Configuration
  Create a .env file in the root directory and add your Binance Testnet credentials:
    
[!IMPORTANT]
   Never share your API keys or commit your .env file to a public repository.
  
  Code snippet

    BINANCE_API_KEY=your_testnet_api_key
    BINANCE_API_SECRET=your_testnet_api_secret


# Usage Examples

**1. Place a MARKET Order** 

   Market orders execute immediately at the current market price.

    bash
    python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002

**2. Place a LIMIT Order**

  Limit orders require a price and stay open until the market reaches that price.

    bash
    python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 65000
**3. Short Flags Example**
    
    bash
    python cli.py -s ETHUSDT -d BUY -t MARKET -u 0.1

# Logging
All interactions are recorded in the logs/bot.log file.

  **>Audit Trail:** Every order request and corresponding API response is logged.

  **>Error Tracking:** Failed orders (e.g., due to insufficient balance or invalid notional value) are logged with their specific API error codes.

  **>File Handling:** Uses RotatingFileHandler to ensure log files do not exceed 1MB.


# Assumptions & Constraints

  **>USDT-M Market:** This bot is designed specifically for USDT-margined futures. All symbols must end with USDT.

  **>Minimum Notional Value:** Binance Testnet requires a minimum notional value (Price × Quantity) of 100 USDT. Orders below this value will be rejected by the API.

  **>Time Sync:** Your system clock must be synchronized with UTC time, as the API uses timestamps for request signing.

  **>Testnet URL:** The bot is hardcoded to use https://testnet.binancefuture.com for safety during evaluation.

