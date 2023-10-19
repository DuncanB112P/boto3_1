import boto3

s3 = boto3.client('s3')
bucket = 'sduncan-boto3-10182023'
keys = ['test_text_upload.txt', 'folder.txt.folder/']


def delete_object(client, bucket, key):
    response = s3.delete_object(
        Bucket=bucket,
        Key=key
    )
    
    return response
    
    
    
    
    
def delete_objects(client, bucket, keys):
    objects = [{'Key': key} for key in keys]
    
    response = s3.delete_objects(
        Bucket=bucket,
        Delete={
            'Objects': objects
            }
            
    )
    
    return response



delete_objects(s3, bucket, keys)


