import streamlit as st

# Set the theme using the config.toml file
st.set_page_config(
    page_title="Smart Health",
    page_icon="⚕️",
    layout="wide",  # Adjustable layout 
    initial_sidebar_state="collapsed"  # Adjustable sidebar
)

# Create the .streamlit/config.toml file (if it doesn't exist)
with open("./config.toml", "w") as f:
    f.write("[theme]\n")
    f.write("primaryColor = '#d33682'\n")
    f.write("backgroundColor = '#002b36'\n")
    f.write("secondaryBackgroundColor = '#586e75'\n")
    f.write("textColor = '#ffd800'\n")
    f.write("font = 'sans serif'\n")

# App content
st.markdown("<h1 style='text-align: center;'>Smart Health</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Your Health, Our Mission !</h2>", unsafe_allow_html=True)

st.sidebar.markdown("# Welcome ")

st.markdown('<p style= "text-align: center; color: black;" ><a href="/dashboard" target="_self" >view dashboard</a></p>', unsafe_allow_html=True)
