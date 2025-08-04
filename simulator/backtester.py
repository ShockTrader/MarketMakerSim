import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from .market_maker import MarketMaker
from .strategies import DynamicSpreadMM, MeanReversionMM, TrendFollowingMM

def run_backtest(prices: list[float], strategy: str, **kwargs) -> dict:
    """Run backtest for a specific strategy"""
    strategies = {
        'static': MarketMaker,
        'dynamic': DynamicSpreadMM,
        'mean_reversion': MeanReversionMM,
        'trend_following': TrendFollowingMM
    }
    
    mm = strategies[strategy](**kwargs)
    for price in prices:
        bid, ask = mm.place_orders(price)
        # Simulate random fills
        if np.random.rand() > 0.5:
            mm.update_inventory(bid, 'bid')
        else:
            mm.update_inventory(ask, 'ask')
    
    return {
        'pnl': mm.pnl_history,
        'inventory': mm.inventory_history,
        'strategy': strategy
    }

def compare_strategies(prices: list[float], spread: float = 0.01):
    """Compare all strategies"""
    results = []
    for strategy in ['static', 'dynamic', 'mean_reversion', 'trend_following']:
        res = run_backtest(prices, strategy, spread=spread)
        results.append(res)
    
    # Plot results
    plt.figure(figsize=(12, 6))
    for res in results:
        plt.plot(np.cumsum(res['pnl']), label=res['strategy'])
    
    plt.title("Strategy Comparison")
    plt.xlabel("Trade")
    plt.ylabel("Cumulative P&L")
    plt.legend()
    plt.grid()
    plt.savefig("strategy_comparison.png")
    return results