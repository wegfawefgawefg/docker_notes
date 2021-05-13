import time
import json
import datetime

import numpy as np

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

def customCallback(client, userdata, message):
    print("Received a new message: ")
    print(message.payload)
    print("from topic: ")
    print(message.topic)
    print("--------------\n\n")

myAWSIoTMQTTClient = None
myAWSIoTMQTTClient = AWSIoTMQTTClient(
    clientID="dummy_sensor")
myAWSIoTMQTTClient.configureEndpoint(
    hostName="a1rnbut4n85cro-ats.iot.us-west-2.amazonaws.com", 
    portNumber=[8883,443][0])
myAWSIoTMQTTClient.configureCredentials(
    CAFilePath="/app/certs/AmazonRootCA1.pem",
    KeyPath="/app/certs/80ca0c0ba3-private.pem.key",
    CertificatePath="/app/certs/80ca0c0ba3-certificate.pem.crt"
)

topic = "dummy_sensor/5_values"

myAWSIoTMQTTClient.connect()
myAWSIoTMQTTClient.subscribe(topic, 1, customCallback)
time.sleep(2)

while True:
    message = {}
    fake_data = np.random.rand(5)
    message['message'] = fake_data.tolist()
    message['timestamp'] = str(datetime.datetime.now())
    messageJson = json.dumps(message)
    myAWSIoTMQTTClient.publish(topic, messageJson, 1)
    print('Published topic %s: %s\n' % (topic, messageJson))
    time.sleep(1)
