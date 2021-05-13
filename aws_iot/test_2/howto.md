#   watch dees
https://www.youtube.com/watch?v=M8yhED_2GQo


sudo aws configure
    AWS Access Key ID [****************2JFL]: 
    AWS Secret Access Key [****************5gTo]: 
    Default region name [US]: us-west-2
    Default output format [None]:

sudo aws iot create-thing --thing-name "iotest"
    {
        "thingName": "iotest",
        "thingArn": "arn:aws:iot:us-west-2:196637981736:thing/iotest",
        "thingId": "f38cb6b1-15cf-4cd5-ae46-a71c230074d0"
    }

sudo aws create-keys-and-certificate --set-as-active
sudo aws iot create-keys-and-certificate --set-as-active
    {
        "certificateArn": "arn:aws:iot:us-west-2:196637981736:cert/e50c3a38921785d1584a5386c0586c8d1df4bfc9ec16941837bae4dab96c3071",
        "certificateId": "e50c3a38921785d1584a5386c0586c8d1df4bfc9ec16941837bae4dab96c3071",
        "certificatePem": "-----BEGIN CERTIFICATE-----\nMIIDWTCCAkGgAwIBAgIUEchkf5vV9scKHUhh5r4bt1dcdwowDQYJKoZIhvcNAQEL\nBQAwTTFLMEkGA1UECwxCQW1hem9uIFdlYiBTZXJ2aWNlcyBPPUFtYXpvbi5jb20g\nSW5jLiBMPVNlYXR0bGUgU1Q9V2FzaGluZ3RvbiBDPVVTMB4XDTIxMDUxMDE5Mjg1\nOVoXDTQ5MTIzMTIzNTk1OVowHjEcMBoGA1UEAwwTQVdTIElvVCBDZXJ0aWZpY2F0\nZTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAK3Q3aSmOwXvPKF5RDGC\n7zBwDX9J0BFMMOCbG5xFuc97YCdjm7mx5zh+7bz89Qje1pZpwuyw6M3vq3/3hSAo\nzUtEBRty1ADTwnYPXj1V4breWnHAP/yT8uSVc542titDvGmDVSGKohY0mH3BlNoC\nKOmyTvgjlrzqr65wawrhXotmqkKC+e4kFmoaDq5A111o/WoUV/gfa3hmb5PNxr7N\nybEN7JOJ2WcKZQWGrst/XmQpyIp614CHxivDH43En5qR3RAH4qyQdvcvUYmERxQh\n4f0Uvcu81GCq/7DSWQ56TtVWlEMP16h/Wk1p6NbshTTGnRvORzFOGwS2z06UF0Xd\nsvECAwEAAaNgMF4wHwYDVR0jBBgwFoAUD3bqlWzwCtcMNSvjJo/TKCZ+YccwHQYD\nVR0OBBYEFAC4J7L0rjfYmwjFKnnlvT48Uf6FMAwGA1UdEwEB/wQCMAAwDgYDVR0P\nAQH/BAQDAgeAMA0GCSqGSIb3DQEBCwUAA4IBAQC5kPIAwvTTju/vS+g86zKFzfGw\nkXWtZHgx9lNlJtwbviQDAbkbT8xYR5C25HMkhKra2yjoX5WsmKkdf1GbIg5WOB2Z\nB8OAmKfNT8+OgGrcsiwRpsuC7cQaMyo0wtRgQNR2melCXWO1PH7bmWM09gi//t0+\nUlY4BcaNcOr/FFSoC+l9shT2UsxZZSplHsdn8GXq+EYZhTubYdGf8Ao/65pxpqVX\n/t6PBEPT2qZ7B0sbuYnFIkOtLj0AGCTpC1jEZTqkCKnwKl2XqsLO0e/OlDdrCIKV\nP2E/APREUv2Aggd2yDhwq+tuWHUPM6MUcycRfLtXF9VzbMyxg+jwdvTuVxKv\n-----END CERTIFICATE-----\n",
        "keyPair": {
            "PublicKey": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArdDdpKY7Be88oXlEMYLv\nMHANf0nQEUww4JsbnEW5z3tgJ2ObubHnOH7tvPz1CN7WlmnC7LDoze+rf/eFICjN\nS0QFG3LUANPCdg9ePVXhut5accA//JPy5JVznja2K0O8aYNVIYqiFjSYfcGU2gIo\n6bJO+COWvOqvrnBrCuFei2aqQoL57iQWahoOrkDXXWj9ahRX+B9reGZvk83Gvs3J\nsQ3sk4nZZwplBYauy39eZCnIinrXgIfGK8MfjcSfmpHdEAfirJB29y9RiYRHFCHh\n/RS9y7zUYKr/sNJZDnpO1VaUQw/XqH9aTWno1uyFNMadG85HMU4bBLbPTpQXRd2y\n8QIDAQAB\n-----END PUBLIC KEY-----\n",
            "PrivateKey": "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEArdDdpKY7Be88oXlEMYLvMHANf0nQEUww4JsbnEW5z3tgJ2Ob\nubHnOH7tvPz1CN7WlmnC7LDoze+rf/eFICjNS0QFG3LUANPCdg9ePVXhut5accA/\n/JPy5JVznja2K0O8aYNVIYqiFjSYfcGU2gIo6bJO+COWvOqvrnBrCuFei2aqQoL5\n7iQWahoOrkDXXWj9ahRX+B9reGZvk83Gvs3JsQ3sk4nZZwplBYauy39eZCnIinrX\ngIfGK8MfjcSfmpHdEAfirJB29y9RiYRHFCHh/RS9y7zUYKr/sNJZDnpO1VaUQw/X\nqH9aTWno1uyFNMadG85HMU4bBLbPTpQXRd2y8QIDAQABAoIBAAhz1sNx/f7M4oLr\ntcA+oMkXOeDNwxuEPABAKriPv3hyhHuF4YXHO/pIWeFN39CdnYvU+tCtzbRuCkX/\n0G5+7XTSivkJvXuI0LUTDD8pVP/UXkuX0MTEoRQynFu+R1+VPK1Y4KPv7O/tgNjk\nuAtd/YVX0XVJrcPkGcT+3IW77fATaoIKFqa/Pe2zsHdtuSZVkTmdDlI5na8v17lp\nsjcBi84Je6IdLboU0O227ZfdBNco1qO8Ts+/vFLrZPBWL92C178GrSGhGkgu1ghF\nmmoqPqs+mgJD+x0cNIdYkiabkU8eud+4rjDn9Dk1bArHTSODdqi5Yaxqj0sfbb61\nM6dkfdECgYEA0vJO/L9z4hfI/1lStCqCjnJjPn3CgSzbXKelXUO+1MY31YT9R71j\nC5dC5WXIzrf+3ozNqyNte19sb6fBdFaRkxbO1TGD1ESUqaKEi6t87XAxjrto93yk\nP4avTuZdZFvkwrUyR3r9AwBfDsZvvhrhG88jq9x1OuN+ibC0UjZWr10CgYEA0vBn\n/Ca+m93fyUcZTn13N4chzXd565idPBv/otuMrr7f6pajErnqlOjvQjmQlzV4mxB6\nH0QTx6crkDDyXVVLdCfHN7Uv01o8VeFnx6MRpm8QjEDD4zqsQHtWutw6KVCOQSv7\nxd501fZmFRaQi27+eQLDULl6Ma+9tGAwESmKnKUCgYBDe+01AnKqM/3DYuoIZUkb\nFREW3tioxpbuz1shuRiFrVwTXNZCax4SiTOHe8aAC3Dn9ZeeVlkiDOb92WcUNtWf\nfr5wicSo1b/RfQJ2REhVFX1lMiNkeWV6RTY0QZJDFvraJ2mMYJYsraO7cFQzNxoo\n8V1yD7cZPcovdm5ZlrSoqQKBgQDEzYmnBxsFX1/AcfZZddO52fkesx7sQapJf7Hl\nZ0N9chaFz198RDtqDV3VAtI1Ua0ht6DI9QIjX4PUduZZUBAi4k4LWp+xaFosoi3q\nY+k+yBa/VFmu8nnte2Wy12/oRgFDKt8vgFqvmcEqYbAgd0Ey8/H4qeQo4Vd0J94Q\n1Ro/BQKBgEdSb/r7DRilNiLL29Vx+UwLgcq6XrNu27sH1J37GvsEmQ1khtwJLD7L\nVwt+UZQry7zku6zyrA8fg8JPTfYsnYTuMuYGityjGUfrreGEJPF5exCqwdyYseAU\n5Xd4AFGj2MhoryRCWANlEUutuF4yw2CPn9LE4aaGBCoIW2Nfz7KW\n-----END RSA PRIVATE KEY-----\n"
        }
    }

#   create policy.json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iot:*",
            "Resource": "*"
        }
    ]
}

#   call this in folder where policy.json is
sudo aws iot create-policy --policy-name "iotest_policy" --policy-document file://policy.json
    {
        "policyName": "iotest_policy",
        "policyArn": "arn:aws:iot:us-west-2:196637981736:policy/iotest_policy",
        "policyDocument": "{\n    \"Version\": \"2012-10-17\",\n    \"Statement\": [\n        {\n            \"Effect\": \"Allow\",\n            \"Action\": \"iot:*\",\n            \"Resource\": \"*\"\n        }\n    ]\n}\n",
        "policyVersionId": "1"
    }


sudo aws iot attach-principal-policy --policy-name "iotest_policy" --principal "arn:aws:iot:us-west-2:196637981736:cert/e50c3a38921785d1584a5386c0586c8d1df4bfc9ec16941837bae4dab96c3071"

sudo aws iot attach-thing-principal --cli-input-json file://iotest_thing_principal.json