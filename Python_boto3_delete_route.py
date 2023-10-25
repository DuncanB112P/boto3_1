import boto3

ec2 = boto3.client('ec2')


response = ec2.delete_route(
    DestinationCidrBlock='0.0.0.0/0',
    RouteTableId='rtb-045a5cd268ec26252',
)

print(response)