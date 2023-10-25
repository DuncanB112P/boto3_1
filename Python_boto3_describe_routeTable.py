import boto3

ec2 = boto3.client('ec2')

routeTable = 'rtb-045a5cd268ec26252'


response = ec2.describe_route_tables(RouteTableIds=[routeTable])

print(response)