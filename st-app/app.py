##__all__ = ['DATA_INFO', 'AUTHOR_INFO', 'APP_NAME', 
##            'SideBar', 'app_sidebar', 'IMAGE_PATH', 
##           'load_cached_data', 'app_mainscreen', 'sb']

import numpy as np
import pandas as pd
import datetime as dt

from pathlib import Path
import streamlit as st

from PIL import Image
from IPython.display import display

# TODO: Following is a hack to fix issue with import paths using in notebook vs. script

# try:
#     from .datapipe import load_and_cache_raw_data
# except:
#    from datapipe import load_and_cache_raw_data

# TODO: Link in read .toml config & secrets

DATA_INFO = 'Using API for ASX data'
AUTHOR_INFO = 'Michaek @ DataBooth.com.au'
APP_NAME = "LK Share Price lookup app"
CACHED_DATA = 'TODO: Data cache file'
CLIENT_NAME = 'Lea Kuan Tan'

st.set_page_config(page_title=APP_NAME, layout='wide')

AVATAR_URL = "https://www.w3schools.com/howto/img_avatar.png"
BRAND_URL = "https://images.contentstack.io/v3/assets/blt1d89a78b502b83f3/blt000cfbfbc534f253/615468f7c3934450a14e3233/img_bikes_hero_dsk.jpg?q=90"
#IMAGE_PATH = 'st-app/resources'
#IMAGE_PATH = Path.cwd().resolve()/IMAGE_PATH

#def ST_APP_CONFIG_TOML = Path().cwd().parent / \"app_secrets.toml\"

class SideBar:
    app_name = APP_NAME
    client_name = CLIENT_NAME
    datasource = DATA_INFO
    datasize = 0   # TODO: Look to calculate this (in GB)
    author = AUTHOR_INFO
    data_title = 'Data details...'
    data_local = False
    today_date = dt.date.today()
    file_name = "Select CSV file..."
#   end_date = dt.date.today()
#    selected_data = None


def app_sidebar(APP_NAME):
    sb = SideBar()
    st.sidebar.info("Menu")
    # col1, col2 = st.sidebar.beta_columns(2)

    #with col1:
        #st.write(IMAGE_URL)
        #image1 = Image.open(IMAGE_PATH/'AppleWatchExercise.jpeg').resize((144, 144))  # NOTE: resize done here
    st.sidebar.image(image=BRAND_URL, use_column_width=True, output_format='PNG')
    #with col2:
        #st.markdown("## TODO")
        #image2 = Image.open(IMAGE_PATH/'HealthFitLogo.png')
        #st.image(image=image2, use_column_width=True, output_format='PNG')

    st.sidebar.markdown(sb.author)

    return sb


# @st.cache
def load_and_cache_data():
    data_df = pd.read_feather(CACHED_DATA)   # load cached (downsampled) data
    return data_df


def app_mainscreen(APP_NAME, sb):
    st.header(APP_NAME + " // " + CLIENT_NAME)
    #st.write("Today's date: " + str(sb.today_date))
    #st.file_uploader
    #csv_file_name = st.file_uploader("Name of CSV data file to convert?", type=['csv'])
    
    # st.write(csv_file_name)
    
    # import data
    data_df = pd.DataFrame()

    #if csv_file_name is not None:
    #    data_df = pd.read_csv(csv_file_name, skiprows=2)

    
    #data_df.rename(columns={"Relative Resistance": "RelativeResistance"}, inplace=True)

    #tcx_file_name = st.file_uploader("Name of TCX data file you would like to merge", type = ['tcx'])

    #new_tcx = ''.join(data_df.apply(convert_csv_row_to_xml, axis=1))
    
    #data_df = load_cached_walking_data()
    #sb.datasize = data_df.memory_usage(deep=True).sum() / 1024 / 1024
    
    # joining tcx
    #TCXFILE = pd.read_xml(tcx_file_name)

    #with open(TCXFILE, "a") as tcxwrite: 
        #for line in new_tcx:
            #tcxwrite.write(line)
            
    #show_raw_csv = st.checkbox("Show raw CSV data")
    #if show_raw_csv:
    #    st.write(data_df)
    #    #st.write(new_tcx)
    #    #st.write(TCXFILE)

    #show_raw_xml = st.checkbox("Show raw XML data")
    #if show_raw_xml:
    #    st.write(new_tcx)

    # return data_df
    return None

sb = app_sidebar(APP_NAME)

app_mainscreen(APP_NAME, sb)
