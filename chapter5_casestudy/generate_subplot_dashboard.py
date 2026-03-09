import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set aesthetic style
plt.style.use('fivethirtyeight')
sns.set_palette("muted")

# 1. Load and prepare data
df = pd.read_csv('/Users/suraj/Desktop/DATA-SCIENCE-LAB/chapter5_casestudy/twitter_stock.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Daily_Change'] = df['Close'] - df['Open']

# 2. Create directory for output
output_dir = '/Users/suraj/Desktop/DATA-SCIENCE-LAB/chapter5_casestudy/charts'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 3. Define the Master Subplot Grid (4 rows, 2 columns)
fig, axes = plt.subplots(4, 2, figsize=(24, 32))
fig.suptitle("Twitter Historical Stock Analysis: Comprehensive Dashboard", fontsize=40, fontweight='bold', y=0.98)

# -- Subplot 1: Price Evolution (Line) --
axes[0, 0].plot(df['Date'], df['Close'], color='#1da1f2', linewidth=2.5)
axes[0, 0].set_title('Stock Price Evolution (2013-2022)', fontsize=22, pad=15)
axes[0, 0].set_ylabel('Price ($)', fontsize=18)
axes[0, 0].grid(True, alpha=0.3)

# -- Subplot 2: Trading Volume Trend (Bar) --
yearly_vol = df.groupby('Year')['Volume'].mean().reset_index()
axes[0, 1].bar(yearly_vol['Year'], yearly_vol['Volume'], color='#778beb')
axes[0, 1].set_title('Average Daily Volume by Year', fontsize=22, pad=15)
axes[0, 1].set_ylabel('Volume (Shares)', fontsize=18)

# -- Subplot 3: Attribute Correlation (Heatmap) --
corr = df[['Open', 'High', 'Low', 'Close', 'Volume']].corr()
sns.heatmap(corr, annot=True, cmap='RdBu', center=0, fmt=".2f", ax=axes[1, 0], annot_kws={"size": 16})
axes[1, 0].set_title('Feature Correlation Heatmap', fontsize=22, pad=15)

# -- Subplot 4: Price Distribution (Histogram) --
sns.histplot(df['Close'], bins=40, kde=True, color='#eb4d4b', ax=axes[1, 1])
axes[1, 1].set_title('Price Frequency Distribution', fontsize=22, pad=15)
axes[1, 1].set_xlabel('Price ($)', fontsize=18)

# -- Subplot 5: Yearly Volatility (Boxplot) --
sns.boxplot(x='Year', y='Close', data=df, palette='viridis', ax=axes[2, 0])
axes[2, 0].set_title('Yearly Price Stability & Outliers', fontsize=22, pad=15)
axes[2, 0].set_ylabel('Price ($)', fontsize=18)

# -- Subplot 6: High vs Low Range (Subplot - Line) --
axes[2, 1].plot(df['Date'], df['High'], label='High', color='#2ecc71', alpha=0.7)
axes[2, 1].plot(df['Date'], df['Low'], label='Low', color='#e74c3c', alpha=0.7)
axes[2, 1].set_title('Intraday High/Low Extremes', fontsize=22, pad=15)
axes[2, 1].legend(fontsize=16)

# -- Subplot 7: Volume vs Daily Change (Scatter) --
axes[3, 0].scatter(df['Volume'], df['Daily_Change'], alpha=0.3, color='#9b59b6')
axes[3, 0].axhline(0, color='black', lw=1.5, ls='--')
axes[3, 0].set_title('Volume vs. Price Volatility', fontsize=22, pad=15)
axes[3, 0].set_xlabel('Trading Volume', fontsize=18)
axes[3, 0].set_ylabel('Price Change ($)', fontsize=18)

# -- Subplot 8: Yearly Trends (Strip Plot) --
sns.stripplot(x='Year', y='Close', data=df, size=2, color="#34495e", alpha=0.3, ax=axes[3, 1])
axes[3, 1].set_title('Stock Price Density by Year', fontsize=22, pad=15)

# 4. Final adjustments
plt.tight_layout(rect=[0, 0.03, 1, 0.96])
plt.savefig(os.path.join(output_dir, 'master_subplot_dashboard.png'), dpi=120)
print("SUCCESS: Master subplot dashboard generated.")
