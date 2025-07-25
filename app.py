import streamlit as st
import pandas as pd
import time
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
import os

# Get current date and time
ts = time.time()
date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
timestamp = datetime.fromtimestamp(ts).strftime("%H:%M-%S")

# Auto-refresh every 5 seconds and track with a key
count = st_autorefresh(interval=5000, limit=None, key="refresh_counter")

# FizzBuzz logic
if count == 0:
    st.write("Count is zero")
elif count % 3 == 0 and count % 5 == 0:
    st.write("FizzBuzz")
elif count % 3 == 0:
    st.write("Fizz")
elif count % 5 == 0:
    st.write("Buzz")
else:
    st.write(f"Count: {count}")

# Read and display attendance CSV
csv_path = f"Attendance/Attendance_{date}.csv"
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
    st.dataframe(df.style.highlight_max(axis=0))
else:
    st.warning(f"Attendance file not found for {date}")
