import boto3

ec2 = boto3.client('ec2')


def: delete_RtTable
routeTable = input('Route table ID: ')

response = ec2.delete_route_table(RouteTableId=routeTable)

print(response)