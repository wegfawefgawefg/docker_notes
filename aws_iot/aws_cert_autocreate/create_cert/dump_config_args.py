import json
import sys
import os

with open("aws_config.json") as f:
    j = json.load(f)
    with open("aws_config", 'w') as f:
        f.write(j["AWSAccessKeyId"])
        f.write("\n")
        f.write(j["AWSSecretKey"])
        f.write("\n")
        f.write(j["region"])
        f.write("\n")
        f.write(j["dataFormat"])
        f.write("\n")
