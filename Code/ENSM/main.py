# Cameron Auler and Sam Guinther
# ENSM AI Log Analysis Engine

import numpy as np
import pandas as pd
import matplotlib.pylab as plot
import seaborn as sns
from sklearn.ensemble import IsolationForest
plot.style.use('ggplot')
pd.set_option("display.max_columns", 200)
import memory
import config

'''
This will be the main script for the ENSM log analysis engine.
'''

def open_file():
    with open(config.dhcp_path) as dataset:
        for data_line in dataset:
            print(data_line)
            # memory.data = memory.data + (tuple(data_line.split()), )

def identify_ip():
    print('identify_ip')

def check_ip():
    print('check_ip')

open_file()
