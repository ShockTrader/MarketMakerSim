import numpy as np  # <-- ADD THIS IMPORT
import sys
from pathlib import Path

# Add project to Python path
sys.path.append(str(Path(__file__).parent))

from simulator.backtester import compare_strategies
from simulator.utils import generate_test_data

if __name__ == "__main__":
    prices = generate_test_data(n=500, volatility=0.02)
    results = compare_strategies(prices, spread=0.005)
    
    for res in results:
        # Calculate Sharpe ratio safely
        if len(res['pnl']) > 1 and np.std(res['pnl']) > 0:
            sharpe = np.mean(res['pnl']) / np.std(res['pnl']) * np.sqrt(252)
        else:
            sharpe = 0
        print(f"{res['strategy']:>15} | Sharpe: {sharpe:.2f}")