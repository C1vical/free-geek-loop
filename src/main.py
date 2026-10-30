import streamlit as st
from components.b2b_portal import render_b2b_portal
from components.device_checker import render_device_checker
from components.demand_matcher import render_demand_matcher
from components.admin_dashboard import render_admin_dashboard
from components.esg_generator import render_esg_generator
from components.scenario_calculator import render_scenario_calculator

st.set_page_config(
    page_title="Free Geek Loop Platform",
    page_icon="🔄",
    layout="wide"
)

def main():
    st.sidebar.title("🔄 Free Geek Loop")
    st.sidebar.caption("FUSE Blueprint 2026 Platform Prototype")
    
    app_mode = st.sidebar.radio(
        "Select Navigation Module:",
        [
            "🏢 Corporate B2B Pledge Portal",
            "🔍 Device Fit Checker (CSV)",
            "🤝 Community Demand Matcher",
            "📊 FGT Operations Dashboard",
            "📄 ESG Report Generator",
            "🧮 Dynamic Scenario Calculator"
        ]
    )
    
    st.sidebar.markdown("---")
    st.sidebar.info("💡 Open-source build for Free Geek Toronto.")

    if app_mode == "🏢 Corporate B2B Pledge Portal":
        render_b2b_portal()
    elif app_mode == "🔍 Device Fit Checker (CSV)":
        render_device_checker()
    elif app_mode == "🤝 Community Demand Matcher":
        render_demand_matcher()
    elif app_mode == "📊 FGT Operations Dashboard":
        render_admin_dashboard()
    elif app_mode == "📄 ESG Report Generator":
        render_esg_generator()
    elif app_mode == "🧮 Dynamic Scenario Calculator":
        render_scenario_calculator()

if __name__ == "__main__":
    main()