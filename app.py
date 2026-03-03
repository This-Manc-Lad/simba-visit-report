import streamlit as st
import pandas as pd
from datetime import datetime
from PIL import Image

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

# --- HEADER (NEW: Professional Logo Integration) ---
# Load the logo (ensure it is in the same folder as your app.py)
logo = Image.open('simba_logo.png')
st.image(logo, width=150, use_column_width=False)
st.markdown("<h1 style='text-align: center; color: black; padding-bottom: 20px;'>WHOLESALE PARTNER VISIT REPORT</h1>", unsafe_allow_html=True)
st.markdown("---")

# --- (Previous Sections 1-4: Visit Details, VM, Competitors...) ---
st.header("🏢 Store Context")
st.selectbox("Select Store", ["John Lewis Oxford St", "Bensons for Beds Manchester", "Furniture Village Trafford"])

st.header("✅ VM Checklist")
st.write("Ensure all brand materials are present.")
vm_visibility = st.radio("Logo Visible?", ["Yes", "Somewhat", "No"], horizontal=True)

# --- NEW: Photo Upload Feature ---
st.header("📷 Visit Documentation")
st.write("Upload a photo of the display area or competitor activity.")
visit_photo = st.file_uploader("Upload Store Photo (JPG/PNG)", type=['png', 'jpg'])

if visit_photo is not None:
    st.image(visit_photo, caption='Uploaded visit photo.', use_column_width=True)

# --- SUBMIT ---
st.markdown("---")
if st.button("SUBMIT REPORT"):
    st.success("Report submitted successfully!")
