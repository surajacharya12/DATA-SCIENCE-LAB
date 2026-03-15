# Lab Report: End-to-End Data Pipeline Analysis

## Title

**End-to-End Data Pipeline Analysis and Walkthrough**

## Objective

The objective of this lab is to analyze a complete data pipeline implemented in Python and Streamlit. The study focuses on understanding the sequential stages of data processing—**Ingestion, Cleaning, Transformation, Analysis, and Visualization**—and how they contribute to turning raw, "dirty" data into actionable business insights.

## Theory

As demonstrated in the `data.py` walkthrough, a professional data pipeline consists of five critical stages:

1. **Ingestion:** The process of importing raw data from source systems (CSV, Databases, APIs) without modification for initial inspection.
2. **Cleaning:** Identifying and resolving data quality issues such as missing values (nulls) or logical errors (e.g., negative quantities).
3. **Transformation:** Reshaping and aggregating granular row-level data into compact, meaningful summaries (e.g., monthly totals, regional performance).
4. **Analysis (KPI calculation):** Computing Key Performance Indicators (KPIs) like Total Revenue and Average Order Value to summarize business health.
5. **Visualization:** Converting complex numerical data into intuitive charts and graphs to communicate patterns instantly to stakeholders.

## Program Workflow

The program follows a strictly modular architecture where each step relies on the output of the previous one:

1. **Step 1 — Ingestion:**

   - The `ingest_data()` function loads 16 raw sales records.
   - Data includes date, product name, region, quantity, and price.
   - **Issue Detected:** The raw data contains intentional errors (a missing quantity in row 10 and a negative quantity in row 12).
2. **Step 2 — Cleaning:**

   - The `clean_data()` function scans for anomalies.
   - **Fix:** Missing quantities are filled with a default value of `1`.
   - **Removal:** Rows with invalid (negative) quantities are discarded.
   - New columns like `total` (quantity * price) and `month` are derived.
3. **Step 3 — Transformation:**

   - The `transform_data()` function uses Pandas grouping logic to create three summary tables:
     - **Monthly Totals:** Revenue and units sold per month.
     - **By Product:** Total revenue share per product line.
     - **By Region:** Performance metrics across geographical segments.
4. **Step 4 — Analysis:**

   - The `analyze_data()` function computes the headline numbers (KPIs).
   - It identifies the "Best" performing categories (Month, Product, Region).
5. **Step 5 — Visualization:**

   - The Streamlit UI utilizes **Plotly** to render interactive charts:
     - **Line Chart:** Monthly revenue trends.
     - **Bar Charts:** Units and transactions volume.
     - **Pie Charts:** Revenue distribution by Product and Region.

## Code Implementation

Below are key snippets from the program logic:

```python
# Cleaning Logic
def clean_data(df: pd.DataFrame):
    # Fix missing quantity
    df.loc[df["quantity"].isna(), "quantity"] = 1
    # Remove negative quantity
    df = df[df["quantity"] >= 0].reset_index(drop=True)
    # Derive derived column
    df["total"] = (df["quantity"] * df["price"]).round(2)
    return df

# Analysis Logic (KPIs)
def analyze_data(monthly, by_product, by_region):
    return {
        "Total Revenue": f"${monthly['revenue'].sum():,.2f}",
        "Best Product": by_product.loc[by_product["revenue"].idxmax(), "name"],
        "Best Month": monthly.loc[monthly["revenue"].idxmax(), "month"]
    }
```

## Analysis Results (Findings)

Based on the execution of the pipeline, the following business findings were extracted:

### 1. Key Performance Indicators (KPIs)

| Metric                          | Value      |
| :------------------------------ | :--------- |
| **Total Revenue**         | $46,299.14 |
| **Total Units Sold**      | 86         |
| **Total Transactions**    | 15         |
| **Avg Order Value**       | $3,086.61  |
| **Best Performing Month** | Feb 2024   |
| **Best Selling Product**  | Phone      |
| **Top Performing Region** | North      |

### 2. Product Performance Summary

| Product         | Revenue              | Units Sold   |
| :-------------- | :------------------- | :----------- |
| Laptop          | $16,999.83           | 17           |
| **Phone** | **$21,499.57** | **43** |
| Tablet          | $7,799.74            | 26           |

### 3. Regional Performance Summary

| Region          | Revenue              | Units Sold |
| :-------------- | :------------------- | :--------- |
| **North** | **$14,199.78** | 22         |
| South           | $12,799.78           | 22         |
| East            | $11,299.80           | 20         |
| West            | $7,999.78            | 22         |

## Discussion

The analysis reveals that although **Laptops** have a high individual unit price, **Phones** drive the majority of the revenue ($21,499.57) due to a significantly higher volume of units sold (43 units).

A critical part of the workflow was the **Cleaning Phase**. Without fixing row 10 (missing value) and removing row 12 (negative value), the final revenue and unit counts would have been inaccurate, potentially leading to wrong business decisions. The use of a **Modular Pipeline** ensures that the data is trustworthy before it reaches the CEO's dashboard.

## Conclusion

The data pipeline was successfully analyzed and demonstrated. The program effectively showcases how Python's ecosystem (`Pandas`, `Plotly`, `Streamlit`) can be used to construct a professional, end-to-end data reporting system. This lab highlights the importance of data integrity and the power of visualization in translating raw numbers into meaningful business stories.
