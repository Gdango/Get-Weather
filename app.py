import os
import json
import sms_send
import api_request
import extract_data

def main():
    Data = api_request.Data()

    if extract_data.Will_Rain(Data) == True:
        sms_send.sms_send("It will rain within the next 4 days!")
    