import streamlit as st
from utils.algorithms import calculate_esg_impact

def render_b2b_portal():
    st.header("🏢 Corporate IT Refresh Pledge Portal")
    st.write("Pledge upcoming corporate hardware refreshes to secure priority ITAD booking and ESG reporting.")
    
    with st.form("b2b_pledge_form"):
        company_name = st.text_input("Company Name", "Acme Corp Toronto")
        contact_email = st.text_input("Corporate Contact Email", "it@acme.com")
        pledge_date = st.date_input("Target Refresh Date")
        device_qty = st.number_input("Estimated Laptop Quantity", min_value=5, max_value=500, value=25)
        device_types = st.multiselect("Device Types", ["Laptops", "Desktops", "Monitors", "Networking"], default=["Laptops"])
        
        submitted = st.form_submit_button("Submit Hardware Pledge")
        
    if submitted:
        impact = calculate_esg_impact(device_qty)
        st.success(f"Pledge recorded for {company_name}!")
        col1, col2 = st.columns(2)
        col1.metric("Projected E-Waste Diverted", f"{impact['ewaste_kg']} kg")
        col2.metric("Projected Carbon Offset", f"{impact['co2_saved_kg']} kg CO2e")