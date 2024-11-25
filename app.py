import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
from datetime import datetime
import os

from PIL import Image
st.set_page_config(layout = 'wide')

from streamlit_image_comparison import image_comparison

# col_img, col_leg = st.columns((1,1))
# with col_img:
image_comparison(f'./data/images/S1A_20241125.png',
                f'./data/images/S2B_20241031.png')
