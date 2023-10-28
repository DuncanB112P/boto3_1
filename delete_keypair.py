import boto3

ec2 = boto3.client('ec2')

kp = 'key from boto3'

response = ec2.delete_key_pair(
    KeyName=kp,
)

print(response)