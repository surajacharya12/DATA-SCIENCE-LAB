# Lab Report: Twitter Stock Market Case Study Analysis

## Title
**Exploratory Data Analysis and Visualization of Twitter Stock (2013-2022)**

## Objective
The objective of this lab is to perform an end-to-end data science study on the historical stock performance of Twitter, Inc. (TWTR). The study aims to apply exploratory data analysis (EDA) techniques, identify historical trends, analyze market volatility, and communicate financial insights through structured data storytelling.

## Theory
Stock market analysis involves several key data processing and visualization concepts as demonstrated in this case study:

1.  **Time-Series Analysis:** Tracking a variable (Closing Price) over time to identify long-term growth cycles and seasonal trends.
2.  **Correlation Analysis:** Using Heatmaps to determine the statistical relationship between different market features like Open, High, Low, Close, and Volume.
3.  **Volatility Assessment:** Utilizing Boxplots to visualize the spread and distribution of stock prices across different years, revealing periods of stability versus extreme fluctuation.
4.  **Frequency Distribution:** Using Histograms to understand the density of stock prices and identifying the most common trading ranges.
5.  **Multivariate Exploration:** Combining multiple visualization types (Line, Bar, Heatmap) into a unified dashboard to provide a holistic view of the company's financial health.

## Program Workflow
The analysis followed a rigorous data science pipeline:

1.  **Data Loading:** Importing the `twitter_stock.csv` dataset containing 2,264 trading records from IPO (2013) to delisting (2022).
2.  **Data Preprocessing:** Converting date strings to datetime objects and extracting yearly features for categorical grouping.
3.  **Exploratory Visualization:**
    -   **Line Charts** were used for Price Evolution.
    -   **Bar Charts** analyzed trading Volume peaks.
    -   **Seaborn Heatmaps** identified perfect correlations between price extremes.
4.  **Statistical Summarization:** Calculating mean prices and volume spikes to identify significant market events.
5.  **Dashboard Generation:** Consolidating all insights into a professional visual report.

## Analysis Results (Findings)

### 1. Market Key Performance Indicators (KPIs)
| Metric | Value |
| :--- | :--- |
| **Total Trading Days** | 2,264 |
| **Minimum Closing Price** | $14.01 |
| **Maximum Closing Price** | $77.63 |
| **Overall Average Price** | $36.00 |
| **Average Daily Volume** | 21,751,861 shares |

### 2. Yearly Price Evolution (Average Close)
| Year | Average Closing Price | Market Context |
| :--- | :--- | :--- |
| 2013 | $49.66 | IPO Period |
| 2016 | $17.57 | Historical Lows |
| 2020 | $37.22 | Pandemic Recovery |
| **2021** | **$59.99** | **All-Time High Year** |
| 2022 | $41.03 | Acquisition/Delisting |

### 3. Key Observations
-   **Strong Linearity:** The study confirmed a nearly 1.0 correlation between Open, High, Low, and Close prices, typical for high-liquid stocks.
-   **Volume Spikes:** Massive volume increases were correlated with high-volatility years (2020-2022), signaling intensive investor interest during market shifts and acquisition talks.
-   **Growth Peak:** Twitter reached its most significant growth phase in 2021, averaging nearly $60 per share before the final 2022 acquisition activity.

## Discussion
The analysis demonstrates that Twitter's stock was highly sensitive to institutional news and market sentiment. The transition from the historical lows of 2016 ($17.57) to the peaks of 2021 ($59.99) shows a resilient but volatile growth trajectory. The "Cleaning and Preprocessing" phase was essential to correctly group the data by Year, which revealed that 2021 was the most successful year for shareholders in terms of valuation.

## Conclusion
This case study successfully demonstrates the power of Python's data visualization ecosystem (`Matplotlib`, `Seaborn`). By transforming raw CSV data into structured charts and tables, we were able to extract the financial story of Twitter, Inc. from its public debut to its final private transition. The lab highlights that professional EDA is the foundation for any sound financial or business decision.
