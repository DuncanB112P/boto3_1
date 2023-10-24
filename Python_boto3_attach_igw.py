# Import the boto3 library, which provides an interface to Amazon Web Services (AWS) services.
import boto3

# Create an EC2 (Elastic Compute Cloud) client using boto3.
ec2 = boto3.client('ec2')

# Define the Internet Gateway ID (igwID) and the VPC ID (vpc) for the attachment.
igwID = 'igw-03fff99e6621921a2'
vpc = 'vpc-01814578897290560'

# Use the EC2 client to attach an Internet Gateway to the specified VPC.
igw_attach = ec2.attach_internet_gateway(
    InternetGatewayId=igwID,
    VpcId=vpc
)

# Print the response, which may contain information about the attachment.
print(igw_attach)