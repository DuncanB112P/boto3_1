import boto3
import os
from Python_boto3_s3_listobject_keys_v2 import list_objects_keys


def download_single_object(client, bucket, key, filename):
    client.download_file(bucket, key, filename)

if __name__ == '__main__':

    bucket = 'sduncan-boto3-10182023'
    key = 'ARCS30421/THE FINAL LECTURE.docx'
    filename = 'ARCS30421/THE FINAL LECTURE.docx'
    
    s3 = boto3.client('s3')
    
    keys = list_objects_keys(s3, bucket, 'folder/')
    
    for key in keys:
        if '/' == key[-1]:
            try:
                os.mkdir(key)
            except: pass
        else:
            download_single_object(s3, bucket, key, filename)