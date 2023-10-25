import boto3

ec2 = boto3.client('ec2')

vpc = 'vpc-01814578897290560'


response = ec2.delete_vpc(
    VpcId=vpc,
)

print(response)