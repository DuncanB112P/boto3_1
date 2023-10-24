import boto3

ec2 = boto3.client('ec2')

rtb_id = 'rtb-045a5cd268ec26252'

subnet_id = 'subnet-0c6926991878281b1'


association = ec2.associate_route_table(
    RouteTableId=rtb_id,
    SubnetId=subnet_id,
)

print(association['AssociationId'])