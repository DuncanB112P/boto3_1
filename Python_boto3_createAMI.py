import boto3

ec2 = boto3.client('ec2')


instID = 'i-04e2e086cdaea90cc'

imgName = 'GotoAMI'


response = ec2.create_image(InstanceId = instID, Name = imgName)



print(response['ImageId'])