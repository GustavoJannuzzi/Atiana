import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import pandas as pd


#with st.sidebar:
#    choose = option_menu("Atiana", ["About", "Fundamentalistas", "Especulativas", "Estudos", "Contact"],
#                         icons=['house', 'camera fill', 'kanban', 'book','person lines fill'],
#                         menu_icon="app-indicator", default_index=0,
#                         styles={
#        "container": {"padding": "5!important", "background-color": "#fafafa"},
#        "icon": {"color": "black", "font-size": "25px"}, 
#        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
#        "nav-link-selected": {"background-color": "#02ab21"},
#    }
#    )


st.set_page_config(
    page_title=("Estratégias Quantitativas")
)

selected2 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
selected2
