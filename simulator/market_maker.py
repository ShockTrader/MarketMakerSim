class MarketMaker:
    def __init__(self, spread: float = 0.01, inventory_limit: int = 100):
        # Initialize ALL tracking attributes here
        self.spread = spread
        self.inventory = 0
        self.inventory_limit = inventory_limit
        self.pnl_history = []
        self.inventory_history = []  # Critical for backtester
        self.price_history = []  # For volatility calculations
        
    def place_orders(self, mid_price: float) -> tuple[float, float]:
        self.price_history.append(mid_price)
        bid = mid_price * (1 - self.spread / 2)
        ask = mid_price * (1 + self.spread / 2)
        return round(bid, 2), round(ask, 2)
    
    def update_inventory(self, price: float, side: str):
        if side == 'bid':
            self.inventory += 1
            self.pnl_history.append(-price)
        else:
            self.inventory -= 1
            self.pnl_history.append(price)
        self.inventory_history.append(self.inventory)  # Track history