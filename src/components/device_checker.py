import streamlit as st
import pandas as pd
from utils.algorithms import calculate_fit_score

def render_device_checker():
    st.header("🔍 Automated CSV Device Fit Checker")
    st.write("Upload an ITAD asset manifest CSV to evaluate refurbishment yield.")
    
    uploaded_file = st.file_uploader("Upload Hardware Manifest (.csv)", type=["csv"])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        df['Fit_Score'] = df.apply(
            lambda row: calculate_fit_score(
                str(row.get('cpu', '')),
                int(row.get('ram_gb', 0)),
                int(row.get('storage_gb', 0)),
                bool(row.get('powers_on', True)),
                str(row.get('screen_condition', 'Good'))
            ), axis=1
        )
        
        df['Action_Recommendation'] = df['Fit_Score'].apply(
            lambda s: "Refurbish for Community / Shop" if s >= 50.0 else "Dismantle for E-Recycle"
        )
        
        st.dataframe(df[['device_id', 'model_name', 'cpu', 'ram_gb', 'Fit_Score', 'Action_Recommendation']])
        
        refurb_count = (df['Action_Recommendation'] == "Refurbish for Community / Shop").sum()
        st.info(f"Yield Summary: **{refurb_count} of {len(df)} units** qualify for high-value refurbishment.")