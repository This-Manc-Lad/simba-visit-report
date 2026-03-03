import streamlit as st
import pandas as pd
from datetime import datetime
from PIL import Image
import os

# --- APP CONFIGURATION ---
st.set_page_config(page_title="Simba Partner Report v0.2", page_icon="🦁", layout="centered")

# Custom CSS for Simba Cyan Header and Buttons
st.markdown("""
    <style>
    .stAppHeader {background-color: #00A9CE;}
    .css-1544g2n {padding-top: 2rem;}
    
    /* Center the main title */
    h1 {text-align: center;}
    
    /* Set color for primary submit button */
    div.stButton > button:first-child {background-color: #00A9CE; color: white; border: none; font-weight: bold;}
    
    /* Set color for photo upload button */
    div.stFileUploader > button:first-child {border-color: #00A9CE;}
    </style>
""", unsafe_allow_html=True)

# --- HEADER (Professional Logo Integration) ---
# Load the logo with error handling (Using the exact filename from your GitHub)
logo_path = 'simba-logo.png'

if os.path.exists(logo_path):
    logo = Image.open(logo_path)
    st.image(logo, width=150, use_column_width=False)
else:
    st.warning(f"⚠️ Logo file not found. Please ensure '{logo_path}' is uploaded to GitHub.")

st.markdown("<h1 style='text-align: center; color: black; padding-bottom: 20px;'>WHOLESALE PARTNER VISIT REPORT</h1>", unsafe_allow_html=True)
st.markdown("---")

# --- SECTION 1: STORE CONTEXT ---
st.header("🏢 Store Context")
st.selectbox("Select Store", ["John Lewis Oxford St", "Bensons for Beds Manchester", "Furniture Village Trafford"])

# --- SECTION 2: VM CHECKLIST ---
st.header("✅ VM Checklist")
st.write("Ensure all brand materials
