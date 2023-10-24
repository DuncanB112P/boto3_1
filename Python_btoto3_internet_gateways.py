# Import the boto3 library, which provides an interface to Amazon Web Services (AWS) services.
import boto3

# Create an EC2 (Elastic Compute Cloud) client using boto3.
ec2 = boto3.client('ec2')

# Use the EC2 client to describe internet gateways and store the response.
response = ec2.describe_internet_gateways()

# Iterate through the list of internet gateways in the response and print their InternetGatewayId.
for igw in response['InternetGateways']:
    print(igw['InternetGatewayId'])

    # Iterate through the attachments for the current internet gateway.
    for attachment in igw['Attachments']:
        # Print the VpcId and State of the attachment.
        print(attachment['VpcId'], attachment['State'])