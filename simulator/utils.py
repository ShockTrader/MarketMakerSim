import pandas as pd
import numpy as np

def generate_test_data(n=1000, volatility=0.1):
    """Generate synthetic price data"""
    returns = np.random.normal(0, volatility, n)
    prices = 100 * np.cumprod(1 + returns)
    return prices.tolist()

def load_csv_data(path: str) -> list[float]:
    """Load prices from CSV"""
    df = pd.read_csv(path)
    return df['close'].values.tolist()