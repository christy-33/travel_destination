import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pywebio.input import *
from pywebio.output import *
from IPython.display import Image
from IPython.display import display
import time
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
app = Flask(__name__)

def choices():
    img = open('DestinationPics/DesiSafar Logo.jpg', 'rb').read()
    put_image(img, width='900px')
    put_markdown('# **Travel Destination Recommendation System**')
    answer = radio("Choose one", options=['Explore Incredible India!', 'Get Travel Recommendations'])
    if(answer == 'Explore Incredible India!'):
        explore()
    if(answer == 'Get Travel Recommendations'):
        put_text('\nLet\'s get started! ')
        #select_recommendation_system()

app.add_url_rule('/tdrs', 'webio_view', webio_view(choices), methods=['GET', 'POST', 'OPTIONS'])
app.run(host='localhost', port=80)
#app.run()