import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instances()

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(instance['InstanceId'], instance['InstanceType'], 
        instance['ImageId'], instance['VpcId'], instance['SubnetId'], 
        instance['State']['Name'], instance['PublicIpAddress'], 
        sep='\n')
    
    for SG in instance['SecurityGroups']:
        print(SG['GroupId'])
    
    if 'KeyName' in instance:
        print(instance['KeyName'])
        
    if 'IamInstanceProfile' in instance:
        print(instance['IamInstanceProfile']['Arn'], instance['IamInstanceProfile']['Id'])
        
    if 'Tags' in instance:
        for tag in instance['Tags']:
            if tag['Key'] == 'Name':
                print(tag['Value'])
                