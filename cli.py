import argparse
from bot.logging_config import setup_loggers
from bot.client import BinanceFuturesClient
from bot.validators import validate_inputs, ValidationError
from bot.orders import place_order
from colorama import Fore,Style,init
setup_loggers()
init(autoreset=True)
def main():
    parser = argparse.ArgumentParser(description="Binance Futures CLI Bot")
    parser.add_argument("-s", "--symbol", required=True)
    parser.add_argument("-d", "--side", required=True)
    parser.add_argument("-t", "--type", required=True)
    parser.add_argument("-u", "--quantity", type=float, required=True)
    parser.add_argument("-p", "--price", type=float)

    args = parser.parse_args()

    try:
        symbol = validate_inputs(args.symbol, args.side, args.type, args.quantity, args.price)
        client = BinanceFuturesClient()
        order = place_order(client, symbol, args.side, args.type, args.quantity, args.price)
        print("\n[Order Response Details]")
        print("-" * 30)
        # These keys (orderId, status, etc.) must match Binance's exact API naming
        print(f"Order ID     : {order.get('orderId')}")
        print(f"Status       : {order.get('status')}")
        print(f"Executed Qty : {order.get('executedQty')}")
        print(f"Avg Price    : {order.get('avgPrice', 'N/A')}")
        print(f"\n {Fore.BLUE}{Style.BRIGHT}Summary: ID={order.get('orderId')}, Status={order.get('status')}")
        
    except ValidationError as e:
        print(f"{Fore.YELLOW}Validation Error: {e}")
    except Exception as e:
        print(f"{Fore.RED}Critical Error: {e}")

if __name__ == "__main__":
    main()