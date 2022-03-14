import streamlit as st
import pandas as pd
import numpy as np


st.write("""
# This is just testing for Streamlit

We will work on all with API reference widgets

""")

st.write("""
> Write and magic

""")
st.write('Hello, *World!* :sunglasses:')

st.write(''' > Title Widget ''')
st.title("testing Streamlit")

st.write(''' > Display data elements. dataframe, table, metric, json ''')

dict_data = {"shoes":["White","Black","Grey","Green","Red"], "size":[2,4,5,7,9]}

test_df = pd.DataFrame(dict_data)

st.dataframe(test_df)
st.table(test_df)
st.metric(label="White", value=test_df["size"][0], delta=3)
st.json({"shoes":["White","Black","Grey","Green","Red"], "size":[2,4,5,7,9]})

st.write('''### That was great now lets continue with all these...
> ### Chart elements
''')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
st.area_chart(chart_data)
st.bar_chart(chart_data)

#st.altair_chart
import altair as alt

df = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.altair_chart(c, use_container_width=True)


#st.vega_lite_chart

df = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])

st.vega_lite_chart(df, {
     'mark': {'type': 'circle', 'tooltip': True},
     'encoding': {
         'x': {'field': 'a', 'type': 'quantitative'},
         'y': {'field': 'b', 'type': 'quantitative'},
         'size': {'field': 'c', 'type': 'quantitative'},
         'color': {'field': 'c', 'type': 'quantitative'},
     },
 })

st.write(''' ### Now lets get into the input widgets 
1. Button
2. download button 
3. checkbox
4. radio
5. select
6. multiselect
7. slider
8. select slider
9. text input
10. number input
11. text area
12. date input
13. time input
14. file uploder
15. camera input
15. color picker
''')

#button
if st.button('Say hellow'):
    st.write("hellow there")
else:
    st.write("good bye")

#download button
text_contents = '''This is some text'''
st.download_button('Download some text', text_contents)

#checkbox
agree = st.checkbox("I agree")
if agree:
    st.write("Great!")
else:
    st.write("Not really")

