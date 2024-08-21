import boto3
from pprint import pprint
# region_name ='us-east-1'
ec2_client = boto3.client('ec2')

#describe method
response  = ec2_client.describe_instances()

pprint(response)







'''
Describe Instance

{'Reservations': [{'Groups': [],
                   'Instances': [{'AmiLaunchIndex': 0,
                                  'Architecture': 'x86_64',
                                  'BlockDeviceMappings': [{'DeviceName': '/dev/xvda',
                                                           'Ebs': {'AttachTime': datetime.datetime(2024, 8, 17, 6, 20, 30, tzinfo=tzutc()),
                                                                   'DeleteOnTermination': True,
                                                                   'Status': 'attached',
                                                                   'VolumeId': 'vol-0148839737f8e7ab3'}}],
                                  'CapacityReservationSpecification': {'CapacityReservationPreference': 'open'},
                                  'ClientToken': '0e539af6-1657-4505-9167-02e1417cc36c',
                                  'CpuOptions': {'CoreCount': 1,
                                                 'ThreadsPerCore': 1},
                                  'CurrentInstanceBootMode': 'legacy-bios',
                                  'EbsOptimized': False,
                                  'EnaSupport': True,
                                  'EnclaveOptions': {'Enabled': False},
                                  'HibernationOptions': {'Configured': False},
                                  'Hypervisor': 'xen',
                                  'ImageId': 'ami-0c8e23f950c7725b9',
                                  'InstanceId': 'i-061cb872c7a3d9d1a',
                                  'InstanceType': 't2.micro',
                                  'KeyName': 'Django',
                                  'LaunchTime': datetime.datetime(2024, 8, 20, 16, 52, 51, tzinfo=tzutc()),
                                  'MaintenanceOptions': {'AutoRecovery': 'default'},
                                  'MetadataOptions': {'HttpEndpoint': 'enabled',
                                                      'HttpProtocolIpv6': 'disabled',
                                                      'HttpPutResponseHopLimit': 2,
                                                      'HttpTokens': 'required',
                                                      'InstanceMetadataTags': 'disabled',
                                                      'State': 'applied'},
                                  'Monitoring': {'State': 'disabled'},
                                  'NetworkInterfaces': [{'Attachment': {'AttachTime': datetime.datetime(2024, 8, 17, 6, 20, 29, tzinfo=tzutc()),
                                                                        'AttachmentId': 'eni-attach-0f4ac7a905a53ab68',
                                                                        'DeleteOnTermination': True,
                                                                        'DeviceIndex': 0,
                                                                        'NetworkCardIndex': 0,
                                                                        'Status': 'attached'},
                                                         'Description': '',
                                                         'Groups': [{'GroupId': 'sg-567fb449',
                                                                     'GroupName': 'default'}],
                                                         'InterfaceType': 'interface',
                                                         'Ipv6Addresses': [],
                                                         'MacAddress': '12:aa:1e:d8:45:b1',
                                                         'NetworkInterfaceId': 'eni-03b86e5f1925c97e9',
                                                         'OwnerId': '375253976385',
                                                         'PrivateDnsName': 'ip-172-31-92-130.ec2.internal',
                                                         'PrivateIpAddress': '172.31.92.130',
                                                         'PrivateIpAddresses': [{'Primary': True,
                                                                                 'PrivateDnsName': 'ip-172-31-92-130.ec2.internal',
                                                                                 'PrivateIpAddress': '172.31.92.130'}],
                                                         'SourceDestCheck': True,
                                                         'Status': 'in-use',
                                                         'SubnetId': 'subnet-cf97b0ee',
                                                         'VpcId': 'vpc-80ccb9fd'}],
                                  'Placement': {'AvailabilityZone': 'us-east-1a',
                                                'GroupName': '',
                                                'Tenancy': 'default'},
                                  'PlatformDetails': 'Linux/UNIX',
                                  'PrivateDnsName': 'ip-172-31-92-130.ec2.internal',
                                  'PrivateDnsNameOptions': {'EnableResourceNameDnsAAAARecord': False,
                                                            'EnableResourceNameDnsARecord': False,
                                                            'HostnameType': 'ip-name'},
                                  'PrivateIpAddress': '172.31.92.130',
                                  'ProductCodes': [],
                                  'PublicDnsName': '',
                                  'RootDeviceName': '/dev/xvda',
                                  'RootDeviceType': 'ebs',
                                  'SecurityGroups': [{'GroupId': 'sg-567fb449',
                                                      'GroupName': 'default'}],
                                  'SourceDestCheck': True,
                                  'State': {'Code': 80, 'Name': 'stopped'},
                                  'StateReason': {'Code': 'Client.UserInitiatedShutdown',
                                                  'Message': 'Client.UserInitiatedShutdown: '
                                                             'User initiated '
                                                             'shutdown'},
                                  'StateTransitionReason': 'User initiated '
                                                           '(2024-08-20 '
                                                           '17:13:41 GMT)',
                                  'SubnetId': 'subnet-cf97b0ee',
                                  'Tags': [{'Key': 'Name', 'Value': 'Django'}],
                                  'UsageOperation': 'RunInstances',
                                  'UsageOperationUpdateTime': datetime.datetime(2024, 8, 17, 6, 20, 29, tzinfo=tzutc()),
                                  'VirtualizationType': 'hvm',
                                  'VpcId': 'vpc-80ccb9fd'}],
                   'OwnerId': '375253976385',
                   'ReservationId': 'r-0fe9c7021ed3e8497'}],
 'ResponseMetadata': {'HTTPHeaders': {'cache-control': 'no-cache, no-store',
                                      'content-length': '4297',
                                      'content-type': 'text/xml;charset=UTF-8',
                                      'date': 'Wed, 21 Aug 2024 02:48:32 GMT',
                                      'server': 'AmazonEC2',
                                      'strict-transport-security': 'max-age=31536000; '
                                                                   'includeSubDomains',
                                      'vary': 'accept-encoding',
                                      'x-amzn-requestid': '9cc32378-e82e-4d73-bf07-caf022b14398'},
                      'HTTPStatusCode': 200,
                      'RequestId': '9cc32378-e82e-4d73-bf07-caf022b14398',
                      'RetryAttempts': 0}}
'''
