# Cameron Auler and Sam Guinther
# ENSM AI Log Analysis Engine

import numpy as np
import pandas as pd
import matplotlib.pylab as plot
import seaborn as sns
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import  f1_score
from sklearn.impute import SimpleImputer
plot.style.use('ggplot')
pd.set_option("display.max_columns", 200)
import memory
import config

'''
This will be the main script for the ENSM log analysis engine.
'''
############################################################################################################################################################################################################################################################
def identify_log():
    print('log Identified')
    print(r'''
          Important markers for each type of log, must be implemented . . .
          -----------------------------------------------------------------
          DHCP: trans_id
          
          ''')
############################################################################################################################################################################################################################################################
############################################################################################################################################################################################################################################################
def read_raw_DHCP():
    with open(config.dhcp_path) as dataset:
        # For each line in the dataset
        for data_line in dataset:
            
            # Format Log Entries
            log_entry = tuple(data_line.split(','), )
            
            # Filter out useless data
            memory.data[log_entry[1]] = (log_entry[0], log_entry[2], log_entry[4], log_entry[6])
    
    #for key, value in memory.data.items():
        #print(f'{key}: {value}')

        #print(f'{value}')
    
    #Create a tuple to store values of the dictionary and then add the values to this new variable
    anomaly_inputs = []
    for key, value in memory.data.items():
        anomaly_inputs.append(value)

    #format inner tuple data to np arrays in the tuple of values from our original dictionary
    arrays = [np.array(inner_tuple) for inner_tuple in anomaly_inputs]
    
    #Convert this array list into a vstack
    readydata = np.vstack(arrays)

    #convert the vstack into a dataframe for the isolation forest to use
    df = pd.DataFrame(readydata)
   
    #define isolation forest model to be used
    if_model = IsolationForest(contamination=0.1, random_state=42)
    
    #One-Hot encode the dataframe to be readable by the machine
    readydata3 = pd.get_dummies(df, columns=[0,1,2,3])

    #Define columns to be targeted
    flags = list(readydata3.columns[:4])
    
    #Fit the data to the model and run analysis
    if_model.fit(readydata3[flags])

    #add anomaly scores column to detect the variance of the line from the rest of the dataset
    readydata3['anomaly_scores'] = if_model.decision_function(readydata3[flags])

    #add anomaly column to the dataframe to display if the prediction is anomalous or not
    readydata3['anomaly'] = if_model.predict(readydata3[flags])
    
    #print findings from the model
    print(readydata3[['anomaly_scores', 'anomaly']])
############################################################################################################################################################################################################################################################
############################################################################################################################################################################################################################################################
def DDos_detection():
     
    labels = ['Destination Port', 'Flow Duration', 'Total Fwd Packets', 'Total Backward Packets', 'Flow Bytes/s', 'Flow Packets/s','FIN Flag Count', 'SYN Flag Count', 'RST Flag Count', 'PSH Flag Count' , 'ACK Flag Count','URG Flag Count']

    # Load the dataset
    data1 = pd.read_csv('DDOS.csv')

    numeric_cols = data1.select_dtypes(include=np.number).columns
    data1[numeric_cols] = data1[numeric_cols][np.isfinite(data1[numeric_cols])]

    #print(data1)

    #extracted features dataframe
    X = data1[labels]

    #label dataframe
    Y= data1['Label']
    
    print( X)
  
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    
    imputer = SimpleImputer(strategy='mean')
    X_train = imputer.fit_transform(X_train)
    X_test = imputer.fit_transform(X_test)

    rfc = RandomForestClassifier(n_estimators=100, random_state=42)

    rfc.fit(X_train, y_train)

    y_pred = rfc.predict(X_test)

    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Precision:", precision_score(y_test, y_pred, average='weighted'))
    print("Recall:", recall_score(y_test, y_pred, average='weighted'))
    print("F1 Score:", f1_score(y_test, y_pred, average='weighted'))
############################################################################################################################################################################################################################################################        
 
read_raw_DHCP()
DDos_detection()



