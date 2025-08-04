import numpy as np
from .market_maker import MarketMaker

class DynamicSpreadMM(MarketMaker):
    """Volatility-adjusted spreads"""
    def place_orders(self, mid_price: float, lookback: int = 20) -> tuple[float, float]:
        if len(self.price_history) >= lookback:
            volatility = np.std(self.price_history[-lookback:]) / np.mean(self.price_history[-lookback:])
            dynamic_spread = self.spread * (1 + 3*volatility)  # Scale with volatility
        else:
            dynamic_spread = self.spread
            
        bid = mid_price * (1 - dynamic_spread / 2)
        ask = mid_price * (1 + dynamic_spread / 2)
        return round(bid, 2), round(ask, 2)

class MeanReversionMM(MarketMaker):
    """Tighten spreads below mean price"""
    def place_orders(self, mid_price: float, lookback: int = 30) -> tuple[float, float]:
        if len(self.price_history) >= lookback:
            mean_price = np.mean(self.price_history[-lookback:])
            spread_adj = 0.7 if mid_price < mean_price else 1.3  # 30% adjustment
        else:
            spread_adj = 1.0
            
        bid = mid_price * (1 - (self.spread * spread_adj) / 2)
        ask = mid_price * (1 + (self.spread * spread_adj) / 2)
        return round(bid, 2), round(ask, 2)

class TrendFollowingMM(MarketMaker):
    """Widen spreads in downtrends"""
    def place_orders(self, mid_price: float, lookback: int = 30) -> tuple[float, float]:
        if len(self.price_history) >= lookback:
            x = np.arange(lookback)
            slope = np.polyfit(x, self.price_history[-lookback:], 1)[0]
            spread_adj = 0.8 if slope > 0 else 1.4  # 40% wider in downtrends
        else:
            spread_adj = 1.0
            
        bid = mid_price * (1 - (self.spread * spread_adj) / 2)
        ask = mid_price * (1 + (self.spread * spread_adj) / 2)
        return round(bid, 2), round(ask, 2)