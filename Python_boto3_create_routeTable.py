import boto3

ec2 = boto3.client('ec2')

vpc = 'vpc-01814578897290560'

response = ec2.create_route_table(VpcId=vpc)

print(response['RouteTable']['RouteTableId'])