import boto3

ec2 = boto3.client('ec2')


response = ec2.delete_security_group(
    GroupId='sg-06d8586e99730ac54',
)

print(response)