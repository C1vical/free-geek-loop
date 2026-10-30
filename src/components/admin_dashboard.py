import streamlit as st
import plotly.express as px

def render_admin_dashboard():
    st.header("📊 FGT Operations Dashboard")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Active SME Partners", "12 Partners", delta="+4 this month")
    col2.metric("Quarterly Laptop Pipeline", "280 Units", delta="82% Refurbish Yield")
    col3.metric("Pending Triage Queue", "15 Units", delta="-5 today")
    
    st.subheader("Incoming Hardware Pipeline")
    chart_data = {"Month": ["Jan", "Feb", "Mar", "Apr"], "Pledged Units": [40, 65, 90, 120]}
    fig = px.bar(chart_data, x="Month", y="Pledged Units", title="Corporate Hardware Pipeline Forecast")
    st.plotly_chart(fig, use_container_width=True)