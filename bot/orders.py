import logging
from colorama import Fore,Style,init
logger = logging.getLogger("trading_bot.orders")
init(autoreset=True)

def place_order(client, symbol, side, order_type, quantity, price=None):
    payload = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity,
        "newOrderRespType": "RESULT"
    }
    
    print(f"\n[Request Summary] Sending {payload['type']} {payload['side']} order for {payload['symbol']}...")
    logger.info(f"Request Payload: {payload}")
    
    if order_type == "LIMIT":
        payload["price"] = price
        payload["timeInForce"] = "GTC"

    logger.info(f"Attempting {order_type} {side} for {symbol}")
    response = client.send_signed_request("POST", "/fapi/v1/order", payload)
    
    if "orderId" in response:
        logger.info(f"{Style.BRIGHT}{Fore.GREEN}Order Successful: ID {response['orderId']}")
    else:
        logger.error(f"{Fore.RED}Order Failed: {response.get('msg', 'Unknown Error')}")
    
    return response