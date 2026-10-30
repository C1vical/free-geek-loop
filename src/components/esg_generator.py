import streamlit as st
from utils.algorithms import calculate_esg_impact
from utils.pdf_export import generate_esg_pdf

def render_esg_generator():
    st.header("📄 ESG Carbon & Impact Certificate Generator")
    st.write("Generate official Scope 3 sustainability documentation for corporate donors.")
    
    comp_name = st.text_input("Partner Company Name", "TechCorp Toronto")
    qty = st.number_input("Total Devices Refurbished", min_value=1, value=40)
    
    metrics = calculate_esg_impact(qty)
    
    st.markdown("---")
    st.write(f"**E-Waste Diverted:** {metrics['ewaste_kg']} kg")
    st.write(f"**Scope 3 Carbon Avoided:** {metrics['co2_saved_kg']} kg CO2e")
    
    pdf_bytes = generate_esg_pdf(comp_name, metrics)
    
    st.download_button(
        label="📥 Download ESG Certificate (PDF)",
        data=pdf_bytes,
        file_name=f"{comp_name.lower().replace(' ', '_')}_esg_certificate.pdf",
        mime="application/pdf"
    )