import boto3

ec2 = boto3.client('ec2')

igwID = 'igw-03fff99e6621921a2'

vpc = 'vpc-01814578897290560'


response = ec2.detach_internet_gateway(
    InternetGatewayId=igwID,
    VpcId=vpc,
)

print(response)