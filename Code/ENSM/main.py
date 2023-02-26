# Cameron Auler and Sam Guinther
# ENSM AI Log Analysis Engine
# February 23

'''
This will be the main script for the ENSM log analysis engine.
'''
import memory
import config

def open_file():
    with open(config.dhcp_path) as dataset:
        for data_line in dataset:
            memory.data = memory.data + (tuple(data_line.split()), )
        
            
            

open_file()