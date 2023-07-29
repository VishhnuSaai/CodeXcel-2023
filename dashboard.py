import pandas as pd
import plotly.express as px
import streamlit as st 

st.set_page_config(page_title="Dashboard",page_icon=":bar_chart:")

st.header("Welcome to our Dashboard")
st.subheader("<-- To add filters")
prod_data=pd.read_excel("Hacathon data 2023.xlsx",
                        engine='openpyxl',
                        sheet_name='Sales')
variables=prod_data.columns
x_axis_select=st.selectbox("select X axis", variables)
y_axis_select=st.selectbox("select Y axis", variables)
st.sidebar.header("Please Filter Here:")
st.sidebar.subheader("*At least one component must be selected from each filter")
productcat=st.sidebar.multiselect(
    "Select the Product Category:",
    options=prod_data["Product Category"].unique()
)
product=st.sidebar.multiselect(
    "Select the product:",
    options=prod_data["Product"].unique()
)
orderpriority=st.sidebar.multiselect(
    "Select the order priority:",
    options=prod_data["Order Priority"].unique()
)
country=st.sidebar.multiselect(
    "Select the country:",
    options=prod_data["Country"].unique()
)

prod_selection=prod_data.query(
    "`Product` == @product & `Order Priority` == @orderpriority & `Country` == @country  "
)
st.title(":bar_chart: Dashboard")
total_sales=int(prod_selection["Sales"].sum())
avg_sales=round(prod_selection["Sales"].mean(),2)
left,right=st.columns(2)
with left:
    st.subheader("Total sales:")
    st.subheader(f"US $ {total_sales:}")
with right:
    st.subheader("Average sales:")
    st.subheader(f"US $ {avg_sales:}")
myplot=px.scatter(prod_selection,x=x_axis_select,y=y_axis_select)
st.dataframe(prod_selection)
st.plotly_chart(myplot)

hide_st_style=""""
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
</style>
"""
st.markdown(hide_st_style,unsafe_allow_html=True)


