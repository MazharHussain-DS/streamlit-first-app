import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Page settings
st.set_page_config(page_title="My First Streamlit App", layout="centered")

# Header
st.title("🚀 My First Streamlit App")
st.markdown(
    "This simple app helps you learn Streamlit basics like widgets, charts, "
    "file upload, and maps. Edit the file and redeploy to see changes!"
)

# Sidebar Controls
st.sidebar.header("Controls")
name = st.sidebar.text_input("Your name", value="Guest")
chart_type = st.sidebar.selectbox("Chart type", ["Line", "Area", "Bar"])
rows = st.sidebar.slider("Number of rows (sample data)", 10, 200, 50)

# Greet user
st.write(f"Hello, **{name}**! Welcome to your first Streamlit app 🎉")

# Create sample time series data
start = datetime.now()
dates = [start - timedelta(days=i) for i in range(rows)][::-1]
np.random.seed(42)
values = np.cumsum(np.random.randn(rows))

df = pd.DataFrame({"date": dates, "value": values})
df = df.set_index("date")

st.subheader("📊 Sample Data")
st.dataframe(df.head(10))

# Chart Section
st.subheader("📈 Interactive Chart")
if chart_type == "Line":
    st.line_chart(df)
elif chart_type == "Area":
    st.area_chart(df)
else:
    st.bar_chart(df)

# File uploader
st.subheader("📤 Upload a CSV File")
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        user_df = pd.read_csv(uploaded_file)
        st.success("CSV loaded successfully!")
        st.dataframe(user_df.head())

        if st.checkbox("Show dataset summary"):
            st.write(user_df.describe(include='all'))

    except Exception as e:
        st.error(f"Error reading file: {e}")

# Map (sample Karachi area data)
st.subheader("🗺️ Sample Map")
st.write("Random points near Karachi (lat/lon)")

lat_center, lon_center = 24.86, 67.01
map_df = pd.DataFrame({
    "lat": lat_center + np.random.normal(scale=0.02, size=10),
    "lon": lon_center + np.random.normal(scale=0.02, size=10)
})
st.map(map_df)

# Footer
st.markdown("---")
st.header("ℹ️ About This App")
st.markdown("""
**You learned:**
- Creating a Streamlit page  
- Sidebar widgets  
- Time-series charts  
- CSV upload & preview  
- Map visualization  

Want to add new features?  
Tell me and I’ll upgrade the app for you! 🚀
""")
