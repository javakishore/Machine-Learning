import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set the page title
st.title('Real-Time Financial Dashboard')

# Upload CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file:
    # Load data into pandas dataframe
    data = pd.read_csv(uploaded_file)

    # Display first few rows
    st.write(data.head())

    # Ensure the correct columns
    if 'Date' in data.columns and 'Price' in data.columns:
        # Convert the Date column to datetime
        data['Date'] = pd.to_datetime(data['Date'])

        # Calculate 30-day moving average
        data['30_day_MA'] = data['Price'].rolling(window=30).mean()

        # Calculate daily percent change
        data['Percent_Change'] = data['Price'].pct_change() * 100

        # Create a plot
        fig, ax1 = plt.subplots(figsize=(10, 6))

        # Plot stock price and moving average
        ax1.plot(data['Date'], data['Price'], label='Stock Price', color='b')
        ax1.plot(data['Date'], data['30_day_MA'], label='30-Day Moving Average', color='g', linestyle='--')
        ax1.set_xlabel('Date')
        ax1.set_ylabel('Price')
        ax1.set_title('Stock Price with 30-Day Moving Average')
        ax1.legend(loc='upper left')

        # Plot daily percentage change on a secondary y-axis
        ax2 = ax1.twinx()
        ax2.plot(data['Date'], data['Percent_Change'], label='Daily % Change', color='r', linestyle='-.')
        ax2.set_ylabel('Percent Change (%)')

        # Display plot in Streamlit
        st.pyplot(fig)
    else:
        st.error("CSV must contain 'Date' and 'Price' columns.")
