import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instance_types(
    Filters=[
        {
            'Name': 'free-tier-eligible',
            'Values': [
                'true',
            ]
        },
    ],
    )
        

for element in response['InstanceTypes']:
    print(element['InstanceType'], element['FreeTierEligible'])