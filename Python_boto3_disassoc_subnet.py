import boto3

ec2 = boto3.client('ec2')

rt_assocID = 'rtbassoc-0bac1b517967e67a1'

response = ec2.disassociate_route_table(
    AssociationId=rt_assocID,
)

print(response)