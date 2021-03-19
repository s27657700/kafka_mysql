from confluent_kafka import Producer
import sys
import time
import pandas as pd
import numpy as np 
def error_cb(err):
    print('Error: %s' % err)
def send_info():
    info=str(input("key in : "))
    if ',' not in info :
        return False
    props = {

        'bootstrap.servers': 'localhost:9092', 
        'error_cb': error_cb                    
    }
    producer = Producer(props)
    topicName = 'project'
    try:
        producer.produce(topicName, info)

        producer.flush()
    except BufferError as e:
        # sys.stderr.write('%% Local producer queue is full ({} messages awaiting delivery): try again\n'
        #                  .format(len(producer)))
        return 'try again'
    except Exception as e:
        return 'try again'
    producer.flush()