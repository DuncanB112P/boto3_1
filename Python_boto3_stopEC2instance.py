import boto3

ec2 = boto3.client('ec2')

instance_id = 'i-002d1060237a5be33'

def stop_instance(client, instance_id):
    response = ec2.stop_instances(
        InstanceIds=[
            instance_id,
        ],
    )
    print('Instance', instance_id, 'Stopped')


def start_instance(client, instance_id):
    response = ec2.start_instances(
        InstanceIds=[
            instance_id,
        ],
    )
    print('Instance', instance_id, 'Started')


def terminate_instance(client, instance_id):
    response = ec2.terminate_instances(
        InstanceIds=[
            instance_id,
        ],
    )
    
    print('Instance', instance_id, 'Terminated')



if __name__ == '__main__':
    instance_id = 'i-002d1060237a5be33'
    ec2 = boto3.client('ec2')
    terminate_instance(ec2, instance_id)