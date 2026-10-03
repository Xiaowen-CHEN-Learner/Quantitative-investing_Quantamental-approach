import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Legacy parameter names retained to avoid disguising the original strategy.
A_BUY_THRESHOLD = 20  # VIX > 20: 1.0x long exposure
B_SELL_THRESHOLD = 15  # VIX < 15: 1.9x long exposure, NOT a sale or short
long_position = 1
short_position = 1.9  # Misleading legacy name: positive 1.9 means leveraged long.
normal_pos = 1
START_DATE = (datetime.now() - timedelta(days=365*10)).strftime('%Y-%m-%d')
END_DATE = datetime.now().strftime('%Y-%m-%d')
tickers = ['SPY', '^VIX']

print(f"Fetching data from {START_DATE} to {END_DATE}...")
data = yf.download(tickers, start=START_DATE, end=END_DATE, progress=False, auto_adjust=True)['Close']
df = data.copy()
# Preserved historical implementation: verify provider column order before use.
df.columns = ['SPY', 'VIX']
df = df.dropna()
df['SPY_Ret'] = df['SPY'].pct_change()
df['Position'] = 0
vix_values = df['VIX'].values
positions = np.zeros(len(df))

for i in range(len(df)):
    # Resets daily: the neutral band does NOT hold yesterday's exposure.
    current_pos = normal_pos
    if vix_values[i] > A_BUY_THRESHOLD:
        current_pos = long_position
    elif vix_values[i] < B_SELL_THRESHOLD:
        current_pos = short_position
    positions[i] = current_pos

df['Position'] = positions
# Lagged signal applied to next close-to-close return. Same-close execution
# remains an assumption; this shift alone does not establish executability.
df['Strategy_Ret'] = df['Position'].shift(1) * df['SPY_Ret']
df['SPY_Cum_Ret'] = (1 + df['SPY_Ret']).cumprod()
df['Strategy_Cum_Ret'] = (1 + df['Strategy_Ret']).cumprod()
total_days = (df.index[-1] - df.index[0]).days
cagr_spy = (df['SPY_Cum_Ret'].iloc[-1])**(365/total_days) - 1
cagr_strat = (df['Strategy_Cum_Ret'].iloc[-1])**(365/total_days) - 1
sharpe_spy = (df['SPY_Ret'].mean() / df['SPY_Ret'].std()) * np.sqrt(252)
sharpe_strat = (df['Strategy_Ret'].mean() / df['Strategy_Ret'].std()) * np.sqrt(252)
rolling_max_strat = df['Strategy_Cum_Ret'].cummax()
daily_drawdown_strat = df['Strategy_Cum_Ret'] / rolling_max_strat - 1.0
max_drawdown_strat = daily_drawdown_strat.min()
rolling_max_spy = df['SPY_Cum_Ret'].cummax()
daily_drawdown_spy = df['SPY_Cum_Ret'] / rolling_max_spy - 1.0
max_drawdown_spy = daily_drawdown_spy.min()

print("\n=== Exploratory SPY exposure experiment; costs and financing omitted ===")
print(f"VIX > {A_BUY_THRESHOLD}: {long_position}x; VIX < {B_SELL_THRESHOLD}: {short_position}x; otherwise: {normal_pos}x")
print(f"Strategy CAGR: {cagr_strat:.2%}")
print(f"Benchmark (SPY) CAGR: {cagr_spy:.2%}")
print(f"Strategy Sharpe (zero risk-free assumption): {sharpe_strat:.2f}")
print(f"Benchmark (SPY) Sharpe: {sharpe_spy:.2f}")
print(f"Strategy Max Drawdown: {max_drawdown_strat:.2%}")
print(f"Benchmark (SPY) Max Drawdown: {max_drawdown_spy:.2%}")

plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Strategy_Cum_Ret'], label='VIX-conditioned SPY exposure')
plt.plot(df.index, df['SPY_Cum_Ret'], label='SPY Buy & Hold')
plt.title('Exploratory SPY exposure experiment — costs and financing omitted')
plt.ylabel('Growth of $1; historical simulation')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
