class ValidationError(Exception):
    pass

def validate_inputs(symbol, side, order_type, quantity, price):
    symbol = symbol.strip().upper()
    if not symbol.endswith("USDT") or len(symbol) < 5:
        raise ValidationError("Symbol must be a valid USDT-M pair (e.g., BTCUSDT).")
    
    if side not in ("BUY", "SELL"):
        raise ValidationError("Side must be BUY or SELL.")
        
    if order_type not in ("MARKET", "LIMIT"):
        raise ValidationError("Type must be MARKET or LIMIT.")
        
    if float(quantity) <= 0:
        raise ValidationError("Quantity must be positive.")
        
    if order_type == "LIMIT" and (price is None or float(price) <= 0):
        raise ValidationError("Price is required and must be positive for LIMIT orders.")
    
    return symbol