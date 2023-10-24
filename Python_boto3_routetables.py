# Import the boto3 library, which provides an interface to Amazon Web Services (AWS) services.
import boto3

# Create an EC2 (Elastic Compute Cloud) client using boto3.
ec2 = boto3.client('ec2')

# Use the EC2 client to describe route tables and store the response.
response = ec2.describe_route_tables()

# Iterate through the list of route tables in the response and print their RouteTableId and VPCId.
for routeTable in response['RouteTables']:
    print(routeTable['RouteTableId'], routeTable['VpcId'])

    # Iterate through the associations for the current route table.
    for association in routeTable['Associations']:
        # Print the RouteTableAssociationId.
        print(association['RouteTableAssociationId'])
        
        # Check if the association has a 'SubnetId' attribute and, if so, print it.
        if 'SubnetId' in association:
            print(association['SubnetId'])

    # Iterate through the routes for the current route table and print GatewayId and DestinationCidrBlock.
    for route in routeTable['Routes']:
        print(route['GatewayId'], route['DestinationCidrBlock'])