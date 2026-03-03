import streamlit as st
import pandas as pd
from datetime import datetime
from PIL import Image
import os

# --- APP CONFIGURATION ---
st.set_page_config(page_title="Simba Partner Report", page_icon="🦁", layout="centered")

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
logo_path = 'simba-logo.png'

if os.path.exists(logo_path):
    logo = Image.open(logo_path)
    st.image(logo, width=150, use_column_width=False)
else:
    st.warning(f"⚠️ Logo file not found. Please ensure '{logo_path}' is uploaded to your GitHub repository.")

st.markdown("<h1 style='text-align: center; color: black; padding-bottom: 20px;'>WHOLESALE PARTNER VISIT REPORT</h1>", unsafe_allow_html=True)
st.markdown("---")

# --- SECTION 1: VISIT DETAILS ---
st.header("📍 Visit Details")
col1, col2 = st.columns(2)
with col1:
    visit_date = st.date_input("Visit Date", datetime.today())
    visitor_name = st.text_input("Visitor Name", placeholder="Your Name")
with col2:
    visit_time = st.selectbox("Visit Time", ["AM", "Mid-Day", "PM"])

# --- SECTION 2: STORE CONTEXT ---
st.header("🏢 Store Context")
retailer = st.selectbox("Retail Group", ["John Lewis", "Bensons for Beds", "Furniture Village", "Independent"])
store_name = st.text_input("Store Name / Branch")

# --- SECTION 3: VM CHECKLIST ---
st.header("✅ VM Checklist")
st.write("Ensure all brand materials are present and up to Simba standard.")

vm_data = {}
checklists = [
    "Brand Visibility (Logo/Mats clearly seen?)",
    "Product Presentation (Topper/Pillows neat?)",
    "Marketing Materials (Price Tickets correct?)",
    "Stock Availability (Boxed inventory visible?)"
]

for item in checklists:
    vm_data[item] = st.radio(f"{item}", ["Yes", "Somewhat", "No"], horizontal=True, key=item)

# --- SECTION 4: VISIT DOCUMENTATION ---
st.header("📷 Visit Documentation")
st.write("Upload a photo of the display area or competitor activity.")
visit_photo = st.file_uploader("Upload Store Photo (JPG/PNG)", type=['png', 'jpg'])

if visit_photo is not None:
    st.image(visit_photo, caption='Uploaded visit photo.', use_column_width=True)

# --- SUBMIT ---
st.markdown("---")
if st.button("SUBMIT REPORT"):
    st.success(f"Report for {store_name} submitted successfully!")
    st.balloons() # Adding a little flair for a successful submission!
