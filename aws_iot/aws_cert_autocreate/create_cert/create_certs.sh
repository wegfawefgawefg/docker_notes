#!/bin/bash

thing_name=$(openssl rand -hex 6)
echo $thing_name
policy_name=$thing_name"_policy"
echo $policy_name

python3 dump_config_args.py
cat aws_config | sudo aws configure
rm aws_config
sudo mkdir "../certs"
sudo aws iot create-thing --thing-name $thing_name > ../certs/thing.json
sudo aws iot create-keys-and-certificate --set-as-active > ../certs/auth.json
sudo cp ./default_policy.json ../certs/policy.json
sudo aws iot create-policy --policy-name $policy_name --policy-document file://../certs/policy.json

arn=$(python3 fetch_arn.py)
sudo aws iot attach-principal-policy` --policy-name $policy_name --principal $arn
princ_path="file://../certs/"$thing_name"_thing_principal.json"
sudo aws iot attach-thing-principal --cli-input-json $princ_path
