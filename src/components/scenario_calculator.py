import streamlit as st
import plotly.express as px
import pandas as pd

def render_scenario_calculator():
    st.header("🧮 Financial Feasibility & Scenario Calculator")
    st.write("Simulate 3-year revenue trajectory based on SME partnership growth[cite: 1].")
    
    partners = st.slider("SME Corporate Partners", min_value=1, max_value=50, value=10)
    avg_laptops = st.slider("Laptops per Partner/Year", min_value=10, max_value=100, value=20)
    yield_rate = st.slider("Refurbishment Yield Rate (%)", min_value=50, max_value=95, value=75) / 100.0
    avg_price = st.slider("Average Resale Price ($)", min_value=100, max_value=300, value=200)
    
    total_laptops = partners * avg_laptops
    refurbished_units = total_laptops * yield_rate
    projected_revenue = refurbished_units * avg_price
    
    col1, col2 = st.columns(2)
    col1.metric("Projected Annual Revenue", f"${projected_revenue:,.2f}")
    col2.metric("Refurbished Units Distributed", f"{int(refurbished_units)} units")
    
    years = ["Year 1 (2027)", "Year 2 (2028)", "Year 3 (2029)"]
    revenues = [projected_revenue, projected_revenue * 2.2, projected_revenue * 3.8]
    
    df_chart = pd.DataFrame({"Year": years, "Revenue ($)": revenues})
    fig = px.line(df_chart, x="Year", y="Revenue ($)", markers=True, title="3-Year Growth Trajectory")
    st.plotly_chart(fig, use_container_width=True)