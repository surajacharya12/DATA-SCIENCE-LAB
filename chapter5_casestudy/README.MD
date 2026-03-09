# Twitter Stock Market Analysis (2013 - 2022)

## 📌 Project Overview

This project is an end-to-end data science case study focused on analyzing the historical stock market performance of **Twitter, Inc. (TWTR)**. The analysis covers the period from Twitter's IPO in November 2013 until its acquisition/delisting in late 2022.

The goal of this study is to demonstrate advanced data visualization techniques, exploratory data analysis (EDA), and financial storytelling using Python.

## 📊 Key Research Questions

- What are the long-term trends in Twitter’s closing price?
- How does daily trading volume correlate with price spikes and drops?
- What are the relationships between different market variables (Open, High, Low, Close, Volume)?
- How has stock volatility evolved on a yearly basis?

## 📂 Dataset Description

The dataset used is `twitter_stock.csv`, which contains:

- **Date**: The trading day.
- **Open / Close**: Opening and closing prices.
- **High / Low**: Intraday price extremes.
- **Adj Close**: Adjusted closing price.
- **Volume**: Total shares traded.

## 🛠️ Tech Stack & Libraries

- **Python 3.x**
- **Pandas**: Data manipulation and cleaning.
- **Matplotlib**: Primary charting and subplot creation.
- **Seaborn**: Advanced statistical visualizations (Heatmaps, Boxplots, Pairplots).
- **Plotly Express**: Interactive time-series exploration.

## 🖼️ Visualizations Included

1. **Price Evolution (Line Chart)**: Tracking the growth and decline of TWTR.
2. **Trading Volume Analysis (Bar Chart)**: Identifying peak trading years.
3. **Correlation Heatmap**: Visualizing how strongly stock features are linked.
4. **Price Distribution (Histogram)**: Analyzing the most frequent price ranges.
5. **Yearly Volatility (Boxplots)**: Comparing price stability across different years.
6. **Master Subplot Dashboard**: A unified view combining all critical dimensions into a single high-resolution image.

## 🚀 How to Use

1. **Explore the Notebook**: Open `Twitter_Chapter5_CaseStudy.ipynb` to see the step-by-step analysis, code cells, and detailed insights.
2. **View the Dashboard**: Open `dashboard.html` in any web browser to see the professional analytical report.
3. **Check the Charts**: All generated static plots are saved in the `charts/` directory.

## 📝 Key Insights

- **High Sensitivity**: Twitter's stock shows massive volume spikes during high-volatility events (news, earnings, external acquisitions).
- **Strong Linearity**: Open, High, Low, and Close prices are nearly perfectly correlated, as expected in high-frequency trading.
- **Growth Cycles**: Significant growth was observed post-2020, followed by a period of extreme volatility leading up to the 2022 acquisition activity.

---

**Developed as part of Chapter 5: Data Visualization & Storytelling | Data Science Lab**
