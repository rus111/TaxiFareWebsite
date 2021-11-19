import streamlit as st
from datetime import datetime 
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

st.markdown('### Date and Time input')
date = st.date_input('Please enter Date of your Journey')
# date = datetime.strptime(date, "%Y-%m-%d")
st.write(date)

time = st.time_input('Please enter Time of your Journey')
date_time = datetime.combine(date, time)
st.markdown('The combined time is: ')
st.write(date_time)

st.write()
pickup_long = st.number_input('Please insert your pickup-longitude')
pickup_lat = st.number_input('Please insert your pickup-latitude')
dropoff_long = st.number_input('Please insert your dropoff-longitude')
dropoff_lat = st.number_input('Please insert your dropoff-latitude')
passenger_count = st.slider('Select passengers number', 1, 8, 1)


'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://api-image-3oxau5jdmq-ew.a.run.app/predict'

if url == 'https://taxifare.lewagon.ai/predict/':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
url_extension = dict(pickup_datetime=str(date_time),
                     pickup_longitude=pickup_long, 
                     pickup_latitude= pickup_lat, 
                     dropoff_longitude = dropoff_long, 
                     dropoff_latitude = dropoff_lat, 
                     passenger_count=passenger_count)
st.write(url_extension)

# st.write(url)
response = requests.get(url, params=url_extension)

response = response.json()

st.markdown('# And the estimated fare is:')

st.write(response['prediction'])