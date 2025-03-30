import yfinance as yf
import streamlit as st
from datetime import datetime
from openai import OpenAI


def get_stock_data(ticker, start_date='2024-01-01', end_date='2024-02-01'):
    data = yf.download(ticker,start = start_date, end=end_date)
    return data

st.title('Interactive Financial Stock Market Comperative Analysis Tool')

st.sidebar.header('User Input Options')
selected_stock = st.sidebar.text_input('Enter Stock Ticker', 'AAPL').upper() #Default to Apple Inc.
selected_stock2 = st.sidebar.text_input('Enter Stock Ticker 2', 'GOOGL').upper()

col1,col2 = st.columns(2)

with col1 :
    stock_data = get_stock_data(selected_stock)
    st.subheader(f'Displaying data for {selected_stock}')
    st.write(stock_data)
    chart_type = st.sidebar.selectbox(f'Select Chart Type for {selected_stock}', ['Line', 'Bar'])
    if chart_type == 'Line' :
        st.line_chart(stock_data['Close'])
    elif chart_type == 'Bar' :
        st.bar_chart(stock_data['Close'])
with col2 :
    stock_data2 = get_stock_data(selected_stock2)
    st.subheader(f'Displaying data for {selected_stock}')
    st.write(stock_data2)
    chart_type = st.sidebar.selectbox(f'Select Chart Type for {selected_stock2}', ['Line', 'Bar'])
    if chart_type == 'Line':
        st.line_chart(stock_data2['Close'])
    elif chart_type == 'Bar':
        st.bar_chart(stock_data2['Close'])



#Initialize OpenAI client
#client = OpenAI(api_key= st.secrets['OPEN_API_KEY'])

#if st.button('Comparative Performance'):
 #   response = client.chat.completions.create(
  #      model='gpt-4o-mini',
   #     messages=[
    #        {"role": "system",
     #        "content": "You are a financial assistant that will retrieve two tables of financial market data and will summarize the comparative performance in text, in full detail with highlights for each stock and also a conclusion with a markdown output. BE VERY STRICT ON YOUR OUTPUT"},
      #      {"role": "user",
       #      "content": f"This is the {selected_stock} stock data : {stock_data}, this is {selected_stock2} stock data: {stock_data2}"}
        #]
    #)
    #st.write(response.choices[0].message.content)



