# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 15:09:37 2021

@author: telkyd
"""

import streamlit as st
import pandas as pd
import os
import sys
#import os
#import time
#import sys
##import math
#import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt
#import matplotlib.style
#import matplotlib as mpl
#import matplotlib.backends.backend_pdf
#from matplotlib.backends.backend_pdf import PdfPages
#from matplotlib.patches import Rectangle, Polygon
#from matplotlib.font_manager import FontProperties
#from os import path
#
#import streamlit as st
#from pylab import *
#st.set_option('deprecation.showPyplotGlobalUse', False)
#import base64
#from fpdf import FPDF

#from tempfile import NamedTemporaryFile

st.title("HELLO!")
antall_lag=st.slider("Velg antall lag",1,10)
lag=[]
phi=[]
Tyngdetetthet=[]
effektiv_tyngdetetthet=[]
kote_topp=[]
c=[]
phi=[]
for i in range(antall_lag):
    cols=st.beta_columns(6)
    lag.append(cols[0].text_input("Lagnavn {}".format(i)))
    phi.append(cols[1].text_input("phi {}".format(i)))
    c.append(cols[2].text_input("Kohesjon {}".format(i)))
    Tyngdetetthet.append(cols[3].text_input("Tyngdetetthet {}".format(i)))
    effektiv_tyngdetetthet.append(cols[4].text_input("Eff tyngdetetthet {}".format(i)))
    kote_topp.append(cols[5].text_input("Kote topp lag {}".format(i)))
#lagre=st.checkbox("Huke av for å lagre som pdf på valgt sti")     
calculate=st.button("Beregn")