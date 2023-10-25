import boto3

ec2 = boto3.client('ec2')

subnetID='subnet-0c6926991878281b1'

response = ec2.delete_subnet(
    SubnetId=subnetID,
)

print(response)