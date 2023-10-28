import boto3

def create_instance(client, ami_id, kp_name, sg_id, user_data=None):
    response = ec2.run_instances(
            ImageId=ami_id,
        InstanceType='t2.micro',
        KeyName=kp_name,
        MaxCount=1,
        MinCount=1,
        SecurityGroupIds=[
            sg_id,
        ],
        UserData = user_data
    )

    print(response['Instances'][0]['InstanceId'])


ec2 = boto3.client('ec2')

ami_id =  'ami-0fc5d935ebf8bc3bc'
kp_name = 'key from boto3'
sg_id = 'sg-06d8586e99730ac54'
user_data='''#!/bin/bash
        apt update -y
        apt-get install -y apache2
        sytemctl start apache2
        systemctl enable apache2'''


    
create_instance(ec2, ami_id, kp_name, sg_id, user_data)
