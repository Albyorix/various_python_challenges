################################## Send message to queue ##################################

from boto3 import client

QUEUE_URL = 'https://sqs.us-west-2.amazonaws.com/927914932618/DataQueue'
my_client = client('sqs', region_name='us-west-2')
message_to_queue = {"email": "", "image": ""}
response = my_client.send_message(QueueUrl=QUEUE_URL, MessageBody=str(message_to_queue))

################################## Get the message ##################################
QUEUE_URL = 'https://sqs.us-west-2.amazonaws.com/927914932618/DataQueue'
my_client = client('sqs', region_name='us-west-2')
visibility_timeout = 600  # disappear for 10 minute
max_wait_time_of_message = 10  # Wait a maximum of 10 secondes
try:
    response = my_client.receive_message(QueueUrl=QUEUE_URL, MessageAttributeNames=['string'],
                                         VisibilityTimeout=visibility_timeout, WaitTimeSeconds=max_wait_time_of_message)
    message = response['Messages'][0]['Body']
    receipt_handle = response['Messages'][0]['ReceiptHandle']
    ################################## Delete message ##################################
    response = my_client.delete_message(QueueUrl=QUEUE_URL, ReceiptHandle=receipt_handle)
    print response
except:
    pass
    # TODO send email to tell me it's not working

################################### USE ONLY THE API ####################################

import requests
from bs4 import BeautifulSoup as bs

url = "http://sqs.us-west-2.amazonaws.com/927914932618/DataQueue/"
url += "?Action=SendMessage&MessageBody=This+is+a+test+message"
r = requests.post(url)
print(r.status_code, r.reason)

url = "http://sqs.us-west-2.amazonaws.com/927914932618/DataQueue/"
url += "?Action=ReceiveMessage"
url += "&MaxNumberOfMessages=1"
url += "&VisibilityTimeout=1"
url += "&AttributeName=string"

r = requests.post(url)
print(r.status_code, r.reason)
s = bs(r.text)
print(s.prettify())