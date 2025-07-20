# import libraries

import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px


#set page config
st.set_page_config(page_title="Car Stock Dashboard", page_icon=":bar_chart:", layout="wide")

# import dataset

@st.cache_data

def get_data():
    df = pd.read_csv('C:/Users/acer/Downloads/cars.csv', index_col=0)
    return df

df = get_data()

# import Sidebar
st.sidebar.header("Please Filter here")
manufacturer = st.sidebar.multiselect(
        "Select the manufacturer:",
        options=df['manufacturer'].unique(),
        default=df['manufacturer'].unique()
    )

# rename the foreign_local_used column 
df=df.rename(columns={"Foreign/Local Used":"Foreign_Local_Used"})

#automation sidebar
automation = st.sidebar.radio(
    "Select the Automation",
    options=df['Automation'].unique()
)

#use category sidebar
use_category=st.sidebar.radio(
    "Select the use_category",
    options=df['Foreign_Local_Used'].unique()
)

# main_page
df_select = df.query(
    "manufacturer== @manufacturer & Automation ==@automation & Foreign_Local_Used==@use_category"
)

#if selection is not available, then stop
if df_select.empty:
    st.warning("No data available based on the current filer setting")
    st.stop()  #halt streamline run

st.title("🦾 Car Stock Dashboard")
st.markdown('##')

#calculate KPI's
average_price = int(df_select['price'].mean()/80)
car_count = df_select.shape[0]
earliest_make_year=df['make-year'].min()

first_column,second_column,third_column = st.columns(3)

with first_column:
    st.subheader('Average Price')
    st.subheader(f"US $ {average_price:,}")
with second_column:
    st.subheader('Car Count')
    st.subheader(f"{car_count:,} Cars")
with third_column:
    st.subheader('Earliest Make Year')
    st.subheader(f"{earliest_make_year:,}")

st.divider()

#plot bar chart to show price per model
price_per_color = df_select.groupby(by=['color'])[['price']].sum().sort_values(by=['price'])

fig_color_price = px.bar(
    price_per_color/80,
    x="price",
    y=price_per_color.index,
    orientation="h",
    title="<b>Price per Color</b>",
    color_discrete_sequence=["#0083b8"] * len(price_per_color),
    template="plotly_white",
)

fig_color_price.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

#plot manufacturer distribution
price_per_make=df_select.groupby(by=['manufacturer'])[['price']].sum().sort_values(by=['price'])

make_price_fig=px.bar(
    price_per_make/80,
    x=price_per_make.index,
    y='price',
    orientation="v",
    title="<b>Price per Manufacturer</b>",
    color_discrete_sequence=["#0083b8"] *len(price_per_make),
    template='plotly_white',
)
make_price_fig.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

left_column,right_column=st.columns(2)
left_column.plotly_chart(fig_color_price, use_container_width=True)
right_column.plotly_chart(make_price_fig, use_container_width=True)

st.divider()

#plot pie chart to show manufacturer distribution
seat_make_dist=df_select.groupby(by=['seat-make'])[['price']].agg('count').sort_values(by=['seat-make'])

fig_seat_dist=px.pie(
    seat_make_dist,
    values="price",
    title="<b>Seat Make Distribution</b>",
    names=seat_make_dist.index,
    color_discrete_sequence=px.colors.sequential.RdBu,
    hole=0.4
)
fig_seat_dist.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

#add more KPI's
max_price =df_select['price'].max()
min_price=df_select['price'].min()

left_column,middle_column,right_column= st.columns(3)
with left_column:
    min_price=df_select['price'].min()
    left_column.metric(
        label="Minimum Price of Cars Selected (US $)",
        value=int(min_price/80)
    )
with left_column:
    max_price=df_select['price'].max()
    left_column.metric(
        label="Maximum Price of Cars Selected (US $)",
        value=int(max_price/80)
    )

with left_column:
    median_price=df_select['price'].median()
    left_column.metric(
        label="Median Price of Cars Selected (US $)",
        value=int(median_price/80)
    )


# seat make plot
middle_column.plotly_chart(fig_seat_dist, use_container_width=True)

# make year plot
make_year_fig=px.histogram(df_select,
                           x='make-year',
                           title="Make Year Distribution")
make_year_fig.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    bargap=0.1,
    xaxis=(dict(showgrid=False))
)
right_column.plotly_chart(make_year_fig, use_container_width=True)

# Hide Strealit Style
st.markdown(
    """
    <style>
    footer {visibility: hidden;}
    footer:after{
    Content: 'Created by Subhash Tiwari';
    visibility: visible;
    position:relative;
    right: 115px;
    }
    {
        background: LightBlue
    }
    </style>
""",
unsafe_allow_html=True,
)





#st.dataframe(df_select)