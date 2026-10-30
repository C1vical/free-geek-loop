import streamlit as st
import json
import os

def render_demand_matcher():
    st.header("🤝 Circular Demand Matcher")
    st.write("Match corporate hardware pledges with verified local nonprofit requests.")
    
    json_path = os.path.join("data", "community_demand.json")
    if os.path.exists(json_path):
        with open(json_path, "r") as f:
            demand_data = json.load(f)
            
        st.subheader("Active Community Requests")
        for req in demand_data:
            with st.expander(f"📍 {req['name']} ({req['urgency']} Urgency)"):
                st.write(f"**Devices Needed:** {req['required_devices']} laptops")
                st.write(f"**Min Specifications:** {req['min_ram_gb']} GB RAM")
                st.write(f"**Purpose:** {req['purpose']}")
                if st.button(f"Match Batch to {req['name']}", key=req['organization_id']):
                    st.success(f"Reservation confirmed for {req['name']}!")
    else:
        st.warning("Sample demand file not found in data/ directory.")