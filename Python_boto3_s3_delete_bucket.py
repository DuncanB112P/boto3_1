# Import the boto3 library, which allows interaction with AWS services.
import boto3

# Define a function to empty an S3 bucket.
def empty_bucket(client, bucket):
    # List objects in the specified S3 bucket using the boto3 client.
    response = client.list_objects_v2(Bucket=bucket)
    
    # Check if there are any objects in the bucket.
    if 'Contents' in response:
        # Create a list of objects to be deleted.
        objects = [{'Key': content['Key']} for content in response['Contents']]
        
        # Use the s3 client to delete the objects in the list.
        response = s3.delete_objects(
            Bucket=bucket,
            Delete={
                'Objects': objects
            }
        )
        
        # Continue deleting objects while there are more to be deleted (using continuation tokens).
        while response.get('NextContinuationToken'):
            # List more objects with a continuation token.
            response = client.list_objects_v2(Bucket=bucket, ContinuationToken=response['NextContinuationToken'])
            
            # Create a new list of objects to be deleted.
            objects = [{'Key': content['Key']} for content in response['Contents']]
            
            # Use the s3 client to delete the new list of objects.
            response = s3.delete_objects(
                Bucket=bucket,
                Delete={
                    'Objects': objects
                }
            )

# Create an S3 client using boto3.
s3 = boto3.client('s3')

# Specify the name of the S3 bucket to be emptied and deleted.
bucket = 'sduncan-boto3-10182023'

# Call the empty_bucket function to remove all objects from the specified bucket.
empty_bucket(s3, bucket)

# Finally, delete the empty S3 bucket.
response = s3.delete_bucket(
    Bucket=bucket
)