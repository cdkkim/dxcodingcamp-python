import streamlit as st
import requests
import plotly.express as px


count_orders_by_date = requests.get('http://localhost:8000/count-orders-by-date').json()

st.title("Line Chart")
st.line_chart(data=count_orders_by_date)


count_orders_by_country = requests.get('http://localhost:8000/count-orders-by-country').json()


# Display bar chart
st.title("Bar Chart")
st.bar_chart(count_orders_by_country)


fig = px.treemap(
    names=count_orders_by_country.keys(),
    values=count_orders_by_country.values(),
    parents=[""] * len(count_orders_by_country.keys()),  # Root level
    title="Treemap of Countries",
)

# Display in Streamlit
st.title("Treemap")
st.plotly_chart(fig)


st.title("Pie Chart")
fig = px.pie(
    names=count_orders_by_country.keys(),
    values=count_orders_by_country.values(),
    title="Pie Chart of Countries",
    hole=0.3  # For a donut chart, adjust the hole value
)

st.plotly_chart(fig)
