import json
import sys
import os

folder = "../certs"
auth = "auth.json"
with open(os.path.join(folder, auth)) as f:
    j = json.load(f)
    arn = j["certificateArn"]
    sys.stdout.write(arn)

#   fetch the certs for later
cert_pem = j["certificatePem"]
priv_key = j["keyPair"]["PublicKey"]
pub_key = j["keyPair"]["PrivateKey"]

with open(os.path.join(folder, "cert"), 'w') as f:
    f.write(cert_pem)
with open(os.path.join(folder, "public_key"), 'w') as f:
    f.write(priv_key)
with open(os.path.join(folder, "private_key"), 'w') as f:
    f.write(pub_key)