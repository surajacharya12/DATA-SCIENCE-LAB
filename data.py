"""
╔══════════════════════════════════════════════════════════════╗
║   🔬 END-TO-END DATA PIPELINE — Beginner's Walkthrough       ║
║   Built with Python + Streamlit + Plotly                     ║
║   Run with:  streamlit run data_pipeline_app.py              ║
╚══════════════════════════════════════════════════════════════╝
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ─────────────────────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Data Pipeline Walkthrough",
    page_icon="🔬",
    layout="wide",
)

# ─────────────────────────────────────────────────────────────
# CUSTOM STYLING
# ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
    /* Dark background */
    .stApp { background-color: #0f0e1a; color: #e2e8f0; }
    .stApp h1, .stApp h2, .stApp h3 { color: #c7d2fe; }

    /* Step boxes */
    .step-box {
        background: #111827;
        border-radius: 12px;
        padding: 20px 24px;
        margin-bottom: 16px;
        border-left: 4px solid;
    }
    .explainer {
        background: #1a1a2e;
        border-radius: 8px;
        padding: 12px 16px;
        color: #9ca3af;
        font-size: 14px;
        margin-bottom: 16px;
        border: 1px solid #2d2d4e;
    }
    /* KPI cards */
    .kpi-card {
        background: #111827;
        border-radius: 10px;
        padding: 16px;
        text-align: center;
        border: 1px solid #1e3a5f;
    }
    /* Sidebar */
    section[data-testid="stSidebar"] { background: #0c0b18 !important; }
</style>
""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════
# ════════  PIPELINE FUNCTIONS  ══════════════════════════════
# ════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────
# STEP 1 — INGESTION
# ─────────────────────────────────────────────────────────────
def ingest_data() -> pd.DataFrame:
    """Load raw sales data (simulating a CSV / database read)."""
    records = [
        {"date": "2024-01-05", "product": "Laptop",  "region": "North", "quantity": 3,    "price": 999.99},
        {"date": "2024-01-07", "product": "Phone",   "region": "South", "quantity": 5,    "price": 499.99},
        {"date": "2024-01-10", "product": "Laptop",  "region": "East",  "quantity": 2,    "price": 999.99},
        {"date": "2024-01-15", "product": "Tablet",  "region": "West",  "quantity": 8,    "price": 299.99},
        {"date": "2024-02-03", "product": "Phone",   "region": "North", "quantity": 10,   "price": 499.99},
        {"date": "2024-02-14", "product": "Laptop",  "region": "South", "quantity": 4,    "price": 999.99},
        {"date": "2024-02-20", "product": "Tablet",  "region": "East",  "quantity": 6,    "price": 299.99},
        {"date": "2024-02-28", "product": "Phone",   "region": "West",  "quantity": 7,    "price": 499.99},
        {"date": "2024-03-05", "product": "Laptop",  "region": "North", "quantity": 5,    "price": 999.99},
        {"date": "2024-03-10", "product": "Tablet",  "region": "South", "quantity": None, "price": 299.99},  # 🐛 missing!
        {"date": "2024-03-18", "product": "Phone",   "region": "East",  "quantity": 9,    "price": 499.99},
        {"date": "2024-03-22", "product": "Laptop",  "region": "West",  "quantity": -1,   "price": 999.99},  # 🐛 bad data!
        {"date": "2024-03-25", "product": "Tablet",  "region": "North", "quantity": 4,    "price": 299.99},
        {"date": "2024-04-02", "product": "Phone",   "region": "South", "quantity": 12,   "price": 499.99},
        {"date": "2024-04-11", "product": "Laptop",  "region": "East",  "quantity": 3,    "price": 999.99},
        {"date": "2024-04-19", "product": "Tablet",  "region": "West",  "quantity": 7,    "price": 299.99},
    ]
    return pd.DataFrame(records)


# ─────────────────────────────────────────────────────────────
# STEP 2 — CLEANING
# ─────────────────────────────────────────────────────────────
def clean_data(df: pd.DataFrame):
    """Fix nulls, remove invalid records, compute derived columns."""
    log = []
    df = df.copy()

    # Fix: fill missing quantity with 1
    missing_mask = df["quantity"].isna()
    for idx in df[missing_mask].index:
        log.append({"type": "⚠️ Fixed", "row": idx + 1,
                    "message": f"Row {idx+1}: Missing quantity → filled with 1"})
    df.loc[missing_mask, "quantity"] = 1

    # Remove: negative quantity
    bad_mask = df["quantity"] < 0
    for idx in df[bad_mask].index:
        log.append({"type": "❌ Skipped", "row": idx + 1,
                    "message": f"Row {idx+1}: Negative quantity ({int(df.loc[idx,'quantity'])}) → removed"})
    df = df[~bad_mask].reset_index(drop=True)

    # Derive columns
    df["quantity"] = df["quantity"].astype(int)
    df["date"]     = pd.to_datetime(df["date"])
    df["total"]    = (df["quantity"] * df["price"]).round(2)
    df["month"]    = df["date"].dt.strftime("%b %Y")

    stats = {
        "raw":     16,
        "fixed":   int(missing_mask.sum()),
        "skipped": int(bad_mask.sum()),
        "clean":   len(df),
    }
    return df, pd.DataFrame(log), stats


# ─────────────────────────────────────────────────────────────
# STEP 3 — TRANSFORM
# ─────────────────────────────────────────────────────────────
def transform_data(df: pd.DataFrame):
    """Aggregate into monthly, product, and region summaries."""
    month_order = ["Jan 2024", "Feb 2024", "Mar 2024", "Apr 2024"]

    monthly = (
        df.groupby("month")
          .agg(revenue=("total", "sum"), units=("quantity", "sum"), transactions=("total", "count"))
          .reset_index()
    )
    monthly["month"] = pd.Categorical(monthly["month"], categories=month_order, ordered=True)
    monthly = monthly.sort_values("month").reset_index(drop=True)
    monthly["revenue"] = monthly["revenue"].round(2)

    by_product = (
        df.groupby("product")
          .agg(revenue=("total", "sum"), units=("quantity", "sum"))
          .reset_index()
          .rename(columns={"product": "name"})
    )
    by_product["revenue"] = by_product["revenue"].round(2)

    by_region = (
        df.groupby("region")
          .agg(revenue=("total", "sum"), units=("quantity", "sum"))
          .reset_index()
          .rename(columns={"region": "name"})
    )
    by_region["revenue"] = by_region["revenue"].round(2)

    return monthly, by_product, by_region


# ─────────────────────────────────────────────────────────────
# STEP 4 — ANALYZE
# ─────────────────────────────────────────────────────────────
def analyze_data(monthly, by_product, by_region):
    """Compute KPIs."""
    total_revenue = monthly["revenue"].sum()
    total_units   = monthly["units"].sum()
    total_tx      = monthly["transactions"].sum()
    avg_order     = total_revenue / total_tx if total_tx else 0
    best_month    = monthly.loc[monthly["revenue"].idxmax(), "month"]
    best_product  = by_product.loc[by_product["revenue"].idxmax(), "name"]
    best_region   = by_region.loc[by_region["revenue"].idxmax(), "name"]
    return {
        "Total Revenue":      f"${total_revenue:,.2f}",
        "Total Units Sold":   int(total_units),
        "Total Transactions": int(total_tx),
        "Avg Order Value":    f"${avg_order:,.2f}",
        "Best Month":         best_month,
        "Best Product":       best_product,
        "Best Region":        best_region,
    }


# ════════════════════════════════════════════════════════════
# ════════  STREAMLIT UI  ════════════════════════════════════
# ════════════════════════════════════════════════════════════

# ─── Header ──────────────────────────────────────────────────
st.markdown("## 🔬 Data Pipeline — Beginner's Walkthrough")
st.markdown("Use the **sidebar** to reveal each stage of the pipeline one step at a time.")
st.divider()

# ─── Sidebar: Step Selector ──────────────────────────────────
STEPS = [
    "📥 Step 1 — Ingestion",
    "🧹 Step 2 — Cleaning",
    "⚙️  Step 3 — Transformation",
    "📊 Step 4 — Analysis",
    "📈 Step 5 — Visualization",
]

with st.sidebar:
    st.markdown("### 🗂️ Pipeline Steps")
    st.caption("Choose how far through the pipeline to go:")
    step = st.radio("Show steps up to:", STEPS, index=0)
    current_step = STEPS.index(step) + 1

    st.divider()
    st.caption("📌 **Each step builds on the previous one.**\nWork through them in order for best understanding.")

    # Progress bar
    st.progress(current_step / len(STEPS), text=f"Step {current_step} / {len(STEPS)}")


# ─── Run Pipeline (always runs all steps, we just show progressively) ──
raw_df                          = ingest_data()
clean_df, clean_log, clean_stats = clean_data(raw_df)
monthly, by_product, by_region  = transform_data(clean_df)
kpis                            = analyze_data(monthly, by_product, by_region)


# ════════════════════════════════════════════════════════════
# STEP 1 — INGESTION
# ════════════════════════════════════════════════════════════
if current_step >= 1:
    with st.expander("📥 Step 1 — Data Ingestion", expanded=True):
        st.markdown("""
<div class="explainer">
💡 <strong>What's happening?</strong> We load raw sales records — just like opening a CSV file or
reading from a database. We don't change anything yet, we just bring the data in and take a look.
</div>
""", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        col1.metric("📋 Records loaded", len(raw_df))
        col2.metric("📅 First date", raw_df["date"].iloc[0])
        col3.metric("📅 Last date", raw_df["date"].iloc[-1])

        # Highlight bad rows
        def highlight_bad(row):
            if row["quantity"] != row["quantity"] or str(row["quantity"]) == "None":
                return ["background-color: #2d1800"] * len(row)
            try:
                if float(row["quantity"]) < 0:
                    return ["background-color: #200e0e"] * len(row)
            except (ValueError, TypeError):
                pass
            return [""] * len(row)

        st.dataframe(
            raw_df.style.apply(highlight_bad, axis=1),
            use_container_width=True,
            height=420,
        )
        st.caption("🔴 Red rows = data problems we'll fix in the next step")


# ════════════════════════════════════════════════════════════
# STEP 2 — CLEANING
# ════════════════════════════════════════════════════════════
if current_step >= 2:
    with st.expander("🧹 Step 2 — Data Cleaning", expanded=True):
        st.markdown("""
<div class="explainer">
💡 <strong>What's happening?</strong> We scan every row for problems. Missing values get a sensible
default. Rows with impossible values (like negative quantities) are removed entirely. This is like
proofreading before analysis.
</div>
""", unsafe_allow_html=True)

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("📥 Raw",      clean_stats["raw"])
        c2.metric("⚠️ Fixed",   clean_stats["fixed"],   delta="filled with 1",  delta_color="off")
        c3.metric("❌ Removed",  clean_stats["skipped"], delta="bad data",       delta_color="inverse")
        c4.metric("✅ Clean",    clean_stats["clean"])

        st.markdown("#### 🪵 Cleaning Log")
        if not clean_log.empty:
            for _, row in clean_log.iterrows():
                color = "#f59e0b" if "Fixed" in row["type"] else "#ef4444"
                st.markdown(
                    f'<div style="padding:8px 12px; margin-bottom:6px; border-radius:6px; '
                    f'background:{"#1c1a00" if "Fixed" in row["type"] else "#200e0e"}; '
                    f'border-left:3px solid {color}; font-size:13px;">'
                    f'{row["type"]}: {row["message"]}</div>',
                    unsafe_allow_html=True
                )

        st.markdown("#### ✅ Clean Data (ready for analysis)")
        st.dataframe(clean_df, use_container_width=True, height=320)


# ════════════════════════════════════════════════════════════
# STEP 3 — TRANSFORMATION
# ════════════════════════════════════════════════════════════
if current_step >= 3:
    with st.expander("⚙️ Step 3 — Data Transformation", expanded=True):
        st.markdown("""
<div class="explainer">
💡 <strong>What's happening?</strong> We reshape individual rows into aggregated summaries — like
pivot tables. Instead of 15 rows, we get compact tables showing totals by month, product, and region.
</div>
""", unsafe_allow_html=True)

        t1, t2, t3 = st.columns(3)
        with t1:
            st.markdown("**📅 Monthly Totals**")
            st.dataframe(monthly.style.format({"revenue": "${:,.2f}"}), use_container_width=True, hide_index=True)
        with t2:
            st.markdown("**🏷️ By Product**")
            st.dataframe(by_product.style.format({"revenue": "${:,.2f}"}), use_container_width=True, hide_index=True)
        with t3:
            st.markdown("**🌍 By Region**")
            st.dataframe(by_region.style.format({"revenue": "${:,.2f}"}), use_container_width=True, hide_index=True)


# ════════════════════════════════════════════════════════════
# STEP 4 — ANALYSIS / KPIs
# ════════════════════════════════════════════════════════════
if current_step >= 4:
    with st.expander("📊 Step 4 — Analysis & KPIs", expanded=True):
        st.markdown("""
<div class="explainer">
💡 <strong>What's happening?</strong> KPIs (Key Performance Indicators) are headline numbers that
summarise business performance at a glance. We compute them from the transformed data.
</div>
""", unsafe_allow_html=True)

        kpi_icons = {
            "Total Revenue":      "💰",
            "Total Units Sold":   "📦",
            "Total Transactions": "🧾",
            "Avg Order Value":    "📈",
            "Best Month":         "📅",
            "Best Product":       "🏆",
            "Best Region":        "🌍",
        }
        kpi_items = list(kpis.items())

        # Row 1: 4 metrics
        cols = st.columns(4)
        for i, (label, value) in enumerate(kpi_items[:4]):
            cols[i].metric(f"{kpi_icons[label]} {label}", value)

        # Row 2: 3 metrics
        cols2 = st.columns(3)
        for i, (label, value) in enumerate(kpi_items[4:]):
            cols2[i].metric(f"{kpi_icons[label]} {label}", value)


# ════════════════════════════════════════════════════════════
# STEP 5 — VISUALIZATION
# ════════════════════════════════════════════════════════════
CHART_BG   = "#0c0b18"
GRID_COLOR = "#1f2937"
FONT_COLOR = "#9ca3af"
COLORS     = ["#6366f1", "#f59e0b", "#10b981", "#ef4444", "#8b5cf6", "#06b6d4"]

def chart_layout(fig, title=""):
    fig.update_layout(
        title=title,
        paper_bgcolor=CHART_BG, plot_bgcolor=CHART_BG,
        font_color=FONT_COLOR, font_family="Courier New",
        title_font_color="#c7d2fe",
        xaxis=dict(gridcolor=GRID_COLOR, linecolor=GRID_COLOR),
        yaxis=dict(gridcolor=GRID_COLOR, linecolor=GRID_COLOR),
        legend=dict(bgcolor=CHART_BG, bordercolor="#2d2d4e"),
        margin=dict(l=20, r=20, t=50, b=20),
    )
    return fig

if current_step >= 5:
    with st.expander("📈 Step 5 — Visualization & Report", expanded=True):
        st.markdown("""
<div class="explainer">
💡 <strong>What's happening?</strong> Charts let you <em>see</em> patterns instantly. A good chart
communicates in seconds what a table takes minutes to decode. This is the final deliverable of
any data pipeline.
</div>
""", unsafe_allow_html=True)

        # ── Chart 1: Monthly Revenue Line ────────────────────
        st.markdown("#### 📅 Monthly Revenue Trend")
        st.caption("How did total revenue change month over month?")
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(
            x=monthly["month"], y=monthly["revenue"],
            mode="lines+markers+text",
            line=dict(color="#f97316", width=3),
            marker=dict(size=10, color="#f97316"),
            text=[f"${v:,.0f}" for v in monthly["revenue"]],
            textposition="top center",
            textfont=dict(color="#f97316", size=12),
            name="Revenue",
        ))
        st.plotly_chart(chart_layout(fig1), use_container_width=True)

        # ── Chart 2 & 3: Side by side ─────────────────────────
        col_a, col_b = st.columns(2)

        with col_a:
            st.markdown("#### 📦 Units Sold per Month")
            st.caption("Which month moved the most product?")
            fig2 = go.Figure(go.Bar(
                x=monthly["month"], y=monthly["units"],
                marker_color="#6366f1",
                text=monthly["units"], textposition="outside",
            ))
            st.plotly_chart(chart_layout(fig2), use_container_width=True)

        with col_b:
            st.markdown("#### 🧾 Transactions per Month")
            st.caption("How many individual sales happened each month?")
            fig3 = go.Figure(go.Bar(
                x=monthly["month"], y=monthly["transactions"],
                marker_color="#10b981",
                text=monthly["transactions"], textposition="outside",
            ))
            st.plotly_chart(chart_layout(fig3), use_container_width=True)

        # ── Chart 4 & 5: Pie charts ───────────────────────────
        col_c, col_d = st.columns(2)

        with col_c:
            st.markdown("#### 🏆 Revenue by Product")
            st.caption("Which product earns the most?")
            fig4 = go.Figure(go.Pie(
                labels=by_product["name"],
                values=by_product["revenue"],
                marker_colors=COLORS[:len(by_product)],
                hole=0,
            ))
            fig4.update_traces(textinfo="label+percent", textfont_size=13)
            st.plotly_chart(chart_layout(fig4), use_container_width=True)

        with col_d:
            st.markdown("#### 🌍 Revenue by Region")
            st.caption("Which region drives the most sales?")
            fig5 = go.Figure(go.Pie(
                labels=by_region["name"],
                values=by_region["revenue"],
                marker_colors=COLORS[2:2+len(by_region)],
                hole=0.4,
            ))
            fig5.update_traces(textinfo="label+percent", textfont_size=13)
            st.plotly_chart(chart_layout(fig5), use_container_width=True)

        # ── Chart 6: Grouped Bar by product per month ─────────
        st.markdown("#### 📊 Revenue by Product Each Month")
        st.caption("Deep dive: which product drove revenue each month?")
        fig6 = go.Figure()
        for i, prod in enumerate(["Laptop", "Phone", "Tablet"]):
            product_monthly = (
                clean_df[clean_df["product"] == prod]
                .groupby("month")["total"].sum()
                .reindex(monthly["month"].tolist(), fill_value=0)
                .reset_index()
            )
            fig6.add_trace(go.Bar(
                name=prod,
                x=product_monthly["month"],
                y=product_monthly["total"].round(2),
                marker_color=COLORS[i],
            ))
        fig6.update_layout(barmode="group")
        st.plotly_chart(chart_layout(fig6), use_container_width=True)

        # ── What You Learned ──────────────────────────────────
        st.divider()
        st.markdown("### 🎓 What You Learned")
        learned = [
            ("📥", "Ingestion",      "Load raw data from any source — CSV, database, or API."),
            ("🧹", "Cleaning",       "Fix nulls, remove invalid rows, standardise formats."),
            ("⚙️",  "Transformation","Aggregate and reshape data into useful summaries."),
            ("📊", "Analysis",       "Calculate KPIs and surface meaningful business insights."),
            ("📈", "Visualization",  "Turn numbers into charts anyone can understand instantly."),
        ]
        for icon, step_name, desc in learned:
            st.markdown(
                f'<div style="display:flex; gap:12px; padding:10px 0; border-bottom:1px solid #1f2937; font-size:14px;">'
                f'<span style="font-size:18px;">{icon}</span>'
                f'<span style="color:#6366f1; font-weight:700; min-width:120px;">{step_name}</span>'
                f'<span style="color:#9ca3af;">{desc}</span>'
                f'</div>',
                unsafe_allow_html=True
            )