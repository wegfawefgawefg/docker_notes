import time
import json
import datetime

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

def customCallback(client, userdata, message):
    print("Received a new message: ")
    print(message.payload)
    print("from topic: ")
    print(message.topic)
    print("--------------\n\n")


myAWSIoTMQTTClient = None
myAWSIoTMQTTClient = AWSIoTMQTTClient(
    clientID="test")
myAWSIoTMQTTClient.configureEndpoint(
    hostName="a1rnbut4n85cro-ats.iot.us-west-2.amazonaws.com", 
    portNumber=[8883,443][0])
myAWSIoTMQTTClient.configureCredentials(
    CAFilePath="/home/gibson/Coding/advs/aws_iot/test_2/AmazonRootCA1.pem",
    KeyPath="/home/gibson/Coding/advs/aws_iot/test_2/efa81f3c9e-private.pem.key",
    CertificatePath="/home/gibson/Coding/advs/aws_iot/test_2/efa81f3c9e-certificate.pem.crt",
)

topic = "test/testing"

myAWSIoTMQTTClient.connect()
myAWSIoTMQTTClient.subscribe(topic, 1, customCallback)
time.sleep(2)

while True:
    message = {}
    message['message'] = "dog"
    message['timestamp'] = str(datetime.datetime.now())
    messageJson = json.dumps(message)
    myAWSIoTMQTTClient.publish(topic, messageJson, 1)
    print('Published topic %s: %s\n' % (topic, messageJson))
    time.sleep(1)
