import streamlit as st
import pandas as pd
from datetime import datetime

# --- APP CONFIGURATION ---
st.set_page_config(page_title="Simba Partner Report", page_icon="🦁", layout="centered")

# Custom CSS for Simba Branding
st.markdown("""
    <style>
    .stAppHeader {background-color: #00A9CE;}
    .css-1544g2n {padding-top: 2rem;}
    div.stButton > button:first-child {background-color: #00A9CE; color: white; border: none;}
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Simba_Sleep_Logo.svg/2560px-Simba_Sleep_Logo.svg.png", width=200)
st.title("WHOLESALE PARTNER VISIT REPORT")
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

# Dynamic store list based on retailer selection
if retailer == "John Lewis":
    store_name = st.selectbox("Store Branch", ["Oxford Street", "Trafford Centre", "Cheadle", "Leeds", "Edinburgh"])
elif retailer == "Bensons for Beds":
    store_name = st.selectbox("Store Branch", ["Manchester White City", "Warrington", "Wigan", "Bolton"])
else:
    store_name = st.text_input("Enter Store Name manually")

contact_name = st.text_input("Store Contact Name")

# --- SECTION 3: VM CHECKLIST ---
st.header("✅ VM Checklist")

vm_data = {}
checklists = [
    "Brand Visibility (Logo/Mats)",
    "Product Presentation (Topper/Pillows)",
    "Marketing Materials (Price Tickets)",
    "Stock Availability"
]

for item in checklists:
    vm_data[item] = st.radio(f"{item}", ["Yes", "Somewhat", "No"], horizontal=True, key=item)

# --- SECTION 4: COMPETITOR ACTIVITY ---
st.header("🕵️ Competitor Intelligence")
competitor = st.selectbox("Primary Competitor Focus", ["Emma", "Tempur", "Silentnight", "Store Brand", "None"])
comp_activity = st.multiselect("Observed Activity", ["Aggressive Pricing", "New Product Launch", "Prime Positioning", "Staff Incentive"])
comp_notes = st.text_area("Staff Feedback / Notes")

# --- SUBMIT ---
st.markdown("---")
if st.button("SUBMIT REPORT"):
    # This acts as the 'save' function
    report_data = {
        "Date": visit_date,
        "Store": store_name,
        "Visitor": visitor_name,
        "Competitor": competitor,
        "Notes": comp_notes
    }
    st.success(f"Report for {store_name} submitted successfully!")
    st.json(report_data) # Shows the data that would be sent to a database