# Import the boto3 library, which provides an interface to Amazon Web Services (AWS) services.
import boto3

# Create an EC2 (Elastic Compute Cloud) client using boto3.
ec2 = boto3.client('ec2')

# Define the CIDR block and VPC ID for the new subnet you want to create.
cidr_block = '12.0.1.0/24'
vpc_id = 'vpc-01814578897290560'

# Use the EC2 client to create a new subnet with the specified CIDR block and VPC ID.
subnet = ec2.create_subnet(CidrBlock=cidr_block, VpcId=vpc_id)

# Print the SubnetId of the newly created subnet.
print(subnet['Subnet']['SubnetId'])
