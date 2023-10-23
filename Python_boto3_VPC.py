# Import the boto3 library, which provides an interface to Amazon Web Services (AWS) services.
import boto3

# Create an EC2 (Elastic Compute Cloud) client using boto3.
ec2 = boto3.client('ec2')

# Use the EC2 client to describe VPCs (Virtual Private Clouds) and store the response.
response = ec2.describe_vpcs()

# Iterate through the list of VPCs in the response and print their VPC ID, CIDR block, and whether they are default.
for vpc in response['Vpcs']:
    print(vpc['VpcId'], vpc['CidrBlock'], vpc['IsDefault'])

# Iterate through the list of VPCs in the response again to check for tags.
for vpc in response['Vpcs']:
    # Check if the VPC has tags.
    if 'Tags' in vpc:
        # If the VPC has tags, iterate through its tags.
        for tag in vpc['Tags']:
            # Check if the tag's key is 'Name'.
            if 'Name' == tag['Key']:
                # If the key is 'Name', print the value associated with the 'Name' tag.
                print(tag['Value'])