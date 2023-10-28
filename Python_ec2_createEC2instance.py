import boto3

ec2 = boto3.client('ec2')

ami_id =  'ami-0b4663f3d7e305939'
kp_name = 'key from boto3'
sg_id = 'sg-06d8586e99730ac54'





response = ec2.run_instances(
    BlockDeviceMappings=[
        {
            'DeviceName': '/dev/sdh',
            'Ebs': {
                'VolumeSize': 100,
            },
        },
    ],
    ImageId=ami_id,
    InstanceType='t2.micro',
    KeyName=kp_name,
    MaxCount=1,
    MinCount=1,
    SecurityGroupIds=[
        sg_id,
    ],
    SubnetId='subnet-09f43c28c89cf7730',
)

print(response['Instances'][0]['InstanceId'])