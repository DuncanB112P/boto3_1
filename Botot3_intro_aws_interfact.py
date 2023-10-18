impot boto3

# ways to interface with AWS - session, client, and resource

session = boto3.Session()

s3 = boto3.client('s3') # how it will be done most of the time
s3 = session.client('s3')

s3 = boto3.resource('s3')
s3 = session.resource('s3')
