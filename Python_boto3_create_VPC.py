# Import the boto3 library, which provides an interface to Amazon Web Services (AWS) services.
import boto3

# Create an EC2 (Elastic Compute Cloud) client using boto3.
ec2 = boto3.client('ec2')

# Use the EC2 client to create a new VPC (Virtual Private Cloud) with the specified CIDR block.
vpc = ec2.create_vpc(CidrBlock='12.0.0.0/16')

# Print the VpcId of the newly created VPC.
print(vpc['Vpc']['VpcId'])