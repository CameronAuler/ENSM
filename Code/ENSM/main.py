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

def identify_log():
    print('log Identified')
    print(r'''
          Important markers for each type of log, must be implemented . . .
          -----------------------------------------------------------------
          DHCP: trans_id
          
          ''')

def read_raw():
    with open(config.dhcp_path) as dataset:
        # For each line in the dataset
        for data_line in dataset:
            
            # Format Log Entries
            log_entry = tuple(data_line.split(None), )
            
            # Filter out useless data
            memory.data[log_entry[1]] = (log_entry[0], log_entry[2], log_entry[4], log_entry[6])
    
    for key, value in memory.data.items():
        print(f'{key}: {value}')
    

def count_ip():
    print('identify_ip')

def check_ip():
    print('check_ip')

read_raw()