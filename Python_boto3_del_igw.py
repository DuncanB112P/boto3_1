import boto3

ec2 = boto3.client('ec2')

igwID = 'igw-03fff99e6621921a2'

response = ec2.delete_internet_gateway(
    InternetGatewayId=igwID,
)

print(response)