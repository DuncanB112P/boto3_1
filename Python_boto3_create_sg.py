import boto3

ec2 = boto3.client('ec2')

sg_name = 'boto3_sg'
descr = 'sg_example'
vpc = 'vpc-0197439ef63392c10'


response = ec2.create_security_group(
    Description=descr,
    GroupName=sg_name,
    VpcId=vpc,
)

print(response['GroupId'])