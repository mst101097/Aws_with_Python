'''
Problem
One of the first things most people want to do after they get signed up with AWS is to
launch an instance.
'''
import boto3
from botocore.exceptions import NoCredentialsError, ClientError

# Initialize the EC2 client
ec2_client = boto3.client('ec2', region_name='us-east-1')  # You can change the region as needed

def launch_ec2_instance():
    try:
        # Launch the EC2 instance
        response = ec2_client.run_instances(
            ImageId='ami-06b21ccaeff8cd686',  # Replace with your desired AMI ID
            InstanceType='t2.micro',  # Instance type
            MinCount=1,  # Number of instances to launch
            MaxCount=1,  # You can increase if you want multiple instances
            KeyName='mst_new',  # Replace with your EC2 Key Pair
            SecurityGroupIds=['sg-12345678'],  # Replace with your security group ID
            SubnetId='subnet-12345678',  # Replace with your subnet ID
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': 'MyFirstEC2Instance'
                        }
                    ]
                }
            ]
        )

        # Extract the instance ID of the launched instance
        instance_id = response['Instances'][0]['InstanceId']
        print(f"EC2 instance launched successfully with ID: {instance_id}")

        return instance_id

    except NoCredentialsError:
        print("Error: AWS credentials not found. Make sure they are set up properly.")
    except ClientError as e:
        print(f"ClientError: {e}")
    except Exception as e:
        print(f"Error launching EC2 instance: {e}")

# Launch the EC2 instance
instance_id = launch_ec2_instance()

# Example: You can stop the instance after launching, if needed
if instance_id:
    print(f"Stopping instance {instance_id}")
    ec2_client.stop_instances(InstanceIds=[instance_id])
