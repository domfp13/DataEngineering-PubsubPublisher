#!/usr/bin/env python3
# Created by Enrique Plata
# set GOOGLE_APPLICATION_CREDENTIALS=C:\Users\lf188653\GCPKey\microstrategyit-749574041a8c.json

import time
from google.cloud import storage
from google.cloud import pubsub_v1
from functions import getRegistry

def publish_message(event, context):

  INFO = {'bucket': event['bucket'], 'name': event['name'], }   
  REGISTRY = getRegistry()

  # create Pub/Sub notification topic
  publisher = pubsub_v1.PublisherClient()
  topic_path = publisher.topic_path(REGISTRY['PROJECT_ID'], REGISTRY['TOPIC'])
  
  data = u'{}'.format(INFO)
  # Data must be a bytestring
  data = data.encode('utf-8')

  future = publisher.publish(topic_path, data, origin='python-sample', username='gcp')
  
  print(future.result())
