import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
import sys,logging
sys.path.insert(0,'../scripts/')
from data_fetch import get_data

logging.basicConfig(filename='../log/log.log', filemode='a',encoding='utf-8', level=logging.DEBUG)
train_data = get_data('data/train_processed.csv','C:/Users/User/Desktop/Pharmaceutical-Sales-Prediction','train_processed_v1')

def holiday_sales():
    st.title("Distribution of total sales across holidays")
    st.markdown("We can see from the below data that holidays have the highest sales volume while Christmas has the lowest volume of sales")
    holiday = train_data[ train_data['StateHoliday'].isin([1,2,3])]
    holiday.groupby('StateHoliday').agg({'Sales':'sum'}).plot(kind='bar',figsize=(9, 8))
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

def store_type_sales():
    st.title("Total amount of sales across different store types.")
    st.markdown("From the figure below we can see the store with type a has the highest sells volume while stores with type b has the lowest volume of sells.")
    train_data.groupby('StoreType').agg({'Sales':'sum'}).sort_values(by='Sales',ascending=False).plot(kind='bar',figsize=(9, 8))
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
def promo_sales_corr():
    st.title("Correlation of promotions, sales and customers")
    st.markdown("From the correalation matrix below we have observed that Promotion has a positve correalation with both sales and customers which means that when ever there is a promotion both sales and customers see an up-tick.")
    sales_promo_rln = train_data.loc[:,['Sales','Promo','Customers']]
    sales_promo_corr = sales_promo_rln.corr()
    st.write(sales_promo_corr)
def sales_prediction():
    st.title("Sales Forecast using Machine learning model")
    st.markdown("This page allows users to forecast sales by inputing information about different stores.")
    st.markdown("Please upload a .CSV file with the appropriate columns and get the sales forecast")
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file != None:
        test_data  = pd.read_csv(uploaded_file)
        test_data.set_index('Date',inplace=True)
        model = pd.read_pickle("../models/2022-09-10-01-43-17.pkl")
        test_data['predicted sales'] = model.predict(test_data)
        fig = px.line(test_data, x=test_data.index, y='predicted sales', title='predicted sales')
        fig.update_xaxes(rangeslider_visible=True)
        fig.show()
        st.write(test_data)
        st.download_button(
            "Press to Download",
            test_data.to_csv(),
            "Predicted_sales.csv",
            "text/csv",
         key='Download-csv'
            )
        


page_names_to_funcs = {
    
    "Distribution of total sales across holidays":holiday_sales,
    "Total amount of sales across different store types.": store_type_sales,
    "Correlation of promotions, sales and customers": promo_sales_corr,
    "Sales Prediction":sales_prediction,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()