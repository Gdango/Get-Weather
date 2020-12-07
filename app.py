import extract_data
from flask import Flask
import os
import json
import sms_send

with open('Data.txt') as json_file:
    Data = json.load(json_file)

if extract_data.Will_Rain(Data) == False:
    sms_send.sms_send("It will not rain within the next 4 days!")
else:
    print("It will rain!")