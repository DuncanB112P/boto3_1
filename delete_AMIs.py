import boto3

ec2 = boto3.client('ec2')

response = ec2.deregister_image(ImageId='ami-0b4663f3d7e305939')

print(response)