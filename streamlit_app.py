import os
from urllib.parse import urlunparse, urlencode

import pandas as pd
import requests
import streamlit as st

data = pd.read_csv('data.csv')


def get_random_data():
    return data.sample(n=1).iloc[0]


def runtime_convert(time_in_min):
    try:
        minutes = int(time_in_min.split()[0])
        h = minutes // 60
        m = minutes % 60

        return f'{str(h)} h {str(m)} min'
    except:
        return None


def get_ombd_data(movie_id):
    omdb_api = os.getenv('OMDb_API')

    scheme = 'https'
    netloc = 'omdbapi.com'
    path = ''
    params = ''
    query = urlencode(
        {
            'apikey': omdb_api,
            'i': movie_id
        }
    )
    fragment = ''

    omdb_url = urlunparse((scheme, netloc, path, params, query, fragment))

    try:
        response = requests.get(omdb_url)
        if response.status_code == 200:
            omdb_data = response.json()
            return omdb_data
        else:
            print(
                f'Error: Received response status code {response.status_code}')
            return None
    except requests.exceptions.RequestException as e:
        print(f'Request failed: {e}')
        return None


# Page Title
st.title('IMDB Watchlist movie randomizer')

if st.button('Generate movie'):
    random_row = get_random_data()
    omdb_data = get_ombd_data(random_row['Const'])

    image_url = omdb_data['Poster']
    title = omdb_data['Title'] + ', ' + omdb_data['Year']
    runtime = runtime_convert(omdb_data['Runtime'])
    genre = omdb_data['Genre']
    plot = omdb_data['Plot']
    director = 'Director: ' + omdb_data['Director']
    actors = 'Cast: ' + omdb_data['Actors'] + '\n'
    awards = omdb_data['Awards']
    omdb_ratings = omdb_data['Ratings']
    omdb_ratings_formatted = []

    st.header(title)
    st.image(image_url)
    st.text(runtime)
    st.text(genre)
    st.text(plot)
    st.text(director)
    st.text(actors)
    st.text(awards)
    if omdb_ratings is not None:
        for rating in omdb_ratings:
            omdb_ratings_formatted.append(
                f'{rating['Source']}: {rating['Value']}')

    st.text('\n'.join(omdb_ratings_formatted))
    st.divider()
