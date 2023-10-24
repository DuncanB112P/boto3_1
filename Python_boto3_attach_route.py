import boto3

ec2 = boto3.client('ec2')


cidr = '0.0.0.0/0'
igwID = 'igw-03fff99e6621921a2'
routeTable = 'rtb-045a5cd268ec26252'



route = ec2.create_route(
    DestinationCidrBlock=cidr,
    GatewayId=igwID,
    RouteTableId=routeTable,
)

print(route)