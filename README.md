# ENSM
The official repository for the Enhanced Network Security Monitoring Project. Network security combined with deep learning AI for threat detection and network analysis.

## Overview
The ENSM project is a network security analytics engine integrated with artificial intelligence that provides enhanced network monitoring and threat detection capabilities. As an important and adaptive component in network security data analysis pipelines, ENSM uses custom logging and security configurations allowing network admins or the SOC to customize their network analytics to their liking. With an AI-enhanced analysis engine built for recognizing potential security threat events, ENSM delivers insightful findings, and organized network data. ENSM will use Python 3 accompanied by the AI utilities PyTorch, Tensorflow, and Keras. Depending on our timeframe for the completion of this project, a UI may be developed to replace the UI stack component.

## How Does ENSM work
Much like Elasticsearch, ENSM gets passed logs from all hosts on a network by Logstash which is a log-gathering engine that uses beats(*local log parsing utilities*) installed on all of the different systems on the network to access their logs. The data that ENSM receives is then processed through the ENSM AI-enhanced analysis engine which finds patterns in the logs and determines if there is a potential security threat event happening. The data is then passed to a UI interpreter which displays the data to the user interface.
