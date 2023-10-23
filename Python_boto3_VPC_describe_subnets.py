# Import the boto3 library, which provides an interface to Amazon Web Services (AWS) services.
import boto3

# Create an EC2 (Elastic Compute Cloud) client using boto3.
ec2 = boto3.client('ec2')

# Use the EC2 client to describe subnets and store the response.
response = ec2.describe_subnets()

# Iterate through the list of subnets in the response and print their CIDR block, Subnet ID, Availability Zone, and VPC ID.
for subnet in response['Subnets']:
    print(subnet['CidrBlock'], subnet['SubnetId'], subnet['AvailabilityZone'], subnet['VpcId'])