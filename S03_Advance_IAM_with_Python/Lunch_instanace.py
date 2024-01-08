import boto3

iam = boto3.client('iam')

# ec2_client = boto3.client('ec2')
ec2_client = boto3.client('ec2', region_name='us-east-1')

instance_profile_name = "MyNewEC2Profile"

response = ec2_client.run_instances(
    ImageId = 'ami-079db87dc4c10ac91',
    InstanceType ='t2.micro',
    MinCount = 1,
    MaxCount = 1,
    IamInstanceProfile={
        'Name': instance_profile_name
    }
)

# instanceID =  response['Instances'][0]['InstanceId']
# print('instanceID ->',instanceID)

print(response)
'''
{'Groups': [], 'Instances': [{'AmiLaunchIndex': 0, 'ImageId': 'ami-079db87dc4c10ac91', 'InstanceId': 'i-0d7cc1d860def1d3f', 'InstanceType': 't2.micro', 'LaunchTime': datetime.datetime(2024, 1, 8, 12, 52, 33, tzinfo=tzutc()), 'Monitoring': {'State': 'disabled'}, 'Placement': {'AvailabilityZone': 'us-east-1c', 'GroupName': '', 'Tenancy': 'default'}, 'PrivateDnsName': 'ip-172-31-28-216.ec2.internal', 'PrivateIpAddress': '172.31.28.216', 'ProductCodes': [], 'PublicDnsName': '', 'State': {'Code': 0, 'Name': 'pending'}, 'StateTransitionReason': '', 'SubnetId': 'subnet-051228a729432bf08', 'VpcId': 'vpc-0f3d16c1dd7c51e4f', 'Architecture': 'x86_64', 'BlockDeviceMappings': [], 'ClientToken': '1d7eb89b-70e1-4745-b726-a09ba33f4d3c', 'EbsOptimized': False, 'EnaSupport': True, 'Hypervisor': 'xen', 'IamInstanceProfile': {'Arn': 'arn:aws:iam::642678036539:instance-profile/MyNewEC2Profile', 'Id': 'AIPAZLIUYTA5S3CXBDNLO'}, 'NetworkInterfaces': [{'Attachment': {'AttachTime': datetime.datetime(2024, 1, 8, 12, 52, 33, tzinfo=tzutc()), 'AttachmentId': 'eni-attach-049800323cddfdc61', 'DeleteOnTermination': True, 'DeviceIndex': 0, 'Status': 'attaching', 'NetworkCardIndex': 0}, 'Description': '', 'Groups': [{'GroupName': 'default', 'GroupId': 'sg-0c5e687678f3ac524'}], 'Ipv6Addresses': [], 'MacAddress': '0a:bc:39:77:65:7b', 'NetworkInterfaceId': 'eni-05b22d4b7cec82a21', 'OwnerId': '642678036539', 'PrivateDnsName': 'ip-172-31-28-216.ec2.internal', 'PrivateIpAddress': '172.31.28.216', 'PrivateIpAddresses': [{'Primary': True, 'PrivateDnsName': 'ip-172-31-28-216.ec2.internal', 'PrivateIpAddress': '172.31.28.216'}], 'SourceDestCheck': True, 'Status': 'in-use', 'SubnetId': 'subnet-051228a729432bf08', 'VpcId': 'vpc-0f3d16c1dd7c51e4f', 'InterfaceType': 'interface'}], 'RootDeviceName': '/dev/xvda', 'RootDeviceType': 'ebs', 'SecurityGroups': [{'GroupName': 'default', 'GroupId': 'sg-0c5e687678f3ac524'}], 'SourceDestCheck': True, 'StateReason': {'Code': 'pending', 'Message': 'pending'}, 'VirtualizationType': 'hvm', 'CpuOptions': {'CoreCount': 1, 'ThreadsPerCore': 1}, 'CapacityReservationSpecification': {'CapacityReservationPreference': 'open'}, 'MetadataOptions': {'State': 'pending', 'HttpTokens': 'required', 'HttpPutResponseHopLimit': 2, 'HttpEndpoint': 'enabled', 'HttpProtocolIpv6': 'disabled', 'InstanceMetadataTags': 'disabled'}, 'EnclaveOptions': {'Enabled': False}, 'BootMode': 'uefi-preferred', 'PrivateDnsNameOptions': {'HostnameType': 'ip-name', 'EnableResourceNameDnsARecord': False, 'EnableResourceNameDnsAAAARecord': False}, 'MaintenanceOptions': {'AutoRecovery': 'default'}, 'CurrentInstanceBootMode': 'legacy-bios'}], 'OwnerId': '642678036539', 'ReservationId': 'r-0907a0725b834593a', 'ResponseMetadata': {'RequestId': '012f56ce-bd3d-4a76-9a81-dfc704b610a7', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '012f56ce-bd3d-4a76-9a81-dfc704b610a7', 'cache-control': 'no-cache, no-store', 'strict-transport-security': 'max-age=31536000; includeSubDomains', 'vary': 'accept-encoding', 'content-type': 'text/xml;charset=UTF-8', 'content-length': '5792', 'date': 'Mon, 08 Jan 2024 12:52:33 GMT', 'server': 'AmazonEC2'}, 'RetryAttempts': 0}}


'''