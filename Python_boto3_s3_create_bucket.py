import boto3

s3 = boto3.client('s3')

response = s3.create_bucket(
    Bucket = 'sduncan-boto3-10182023'
)

print(response)
    