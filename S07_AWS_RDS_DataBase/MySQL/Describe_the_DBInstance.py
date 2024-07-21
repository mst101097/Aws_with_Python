import boto3
from pprint import pprint
rds_client = boto3.client('rds',region_name='us-east-1')

response = rds_client.describe_db_instances(
    DBInstanceIdentifier="mstdbinstance"
)


pprint(response)


'''
{'DBInstances': [{'ActivityStreamStatus': 'stopped',
                  'AllocatedStorage': 20,
                  'AssociatedRoles': [],
                  'AutoMinorVersionUpgrade': True,
                  'AvailabilityZone': 'us-east-1a',
                  'BackupRetentionPeriod': 1,
                  'BackupTarget': 'region',
                  'CACertificateIdentifier': 'rds-ca-rsa2048-g1',
                  'CertificateDetails': {'CAIdentifier': 'rds-ca-rsa2048-g1',
                                         'ValidTill': datetime.datetime(2025, 7, 21, 4, 33, 26, tzinfo=tzutc())},
                  'CopyTagsToSnapshot': False,
                  'CustomerOwnedIpEnabled': False,
                  'DBInstanceArn': 'arn:aws:rds:us-east-1:375253976385:db:mstdbinstance',
                  'DBInstanceClass': 'db.t3.micro',
                  'DBInstanceIdentifier': 'mstdbinstance',
                  'DBInstanceStatus': 'available',
                  'DBName': 'mstdb',
                  'DBParameterGroups': [{'DBParameterGroupName': 'default.mysql8.0',
                                         'ParameterApplyStatus': 'in-sync'}],
                  'DBSecurityGroups': [],
                  'DBSubnetGroup': {'DBSubnetGroupDescription': 'default',
                                    'DBSubnetGroupName': 'default',
                                    'SubnetGroupStatus': 'Complete',
                                    'Subnets': [{'SubnetAvailabilityZone': {'Name': 'us-east-1c'},
                                                 'SubnetIdentifier': 'subnet-f60e2ba9',
                                                 'SubnetOutpost': {},
                                                 'SubnetStatus': 'Active'},
                                                {'SubnetAvailabilityZone': {'Name': 'us-east-1f'},
                                                 'SubnetIdentifier': 'subnet-cb2f3dc5',
                                                 'SubnetOutpost': {},
                                                 'SubnetStatus': 'Active'},
                                                {'SubnetAvailabilityZone': {'Name': 'us-east-1e'},
                                                 'SubnetIdentifier': 'subnet-ce9cf0ff',
                                                 'SubnetOutpost': {},
                                                 'SubnetStatus': 'Active'},
                                                {'SubnetAvailabilityZone': {'Name': 'us-east-1a'},
                                                 'SubnetIdentifier': 'subnet-cf97b0ee',
                                                 'SubnetOutpost': {},
                                                 'SubnetStatus': 'Active'},
                                                {'SubnetAvailabilityZone': {'Name': 'us-east-1b'},
                                                 'SubnetIdentifier': 'subnet-c809e184',
                                                 'SubnetOutpost': {},
                                                 'SubnetStatus': 'Active'},
                                                {'SubnetAvailabilityZone': {'Name': 'us-east-1d'},
                                                 'SubnetIdentifier': 'subnet-34603852',
                                                 'SubnetOutpost': {},
                                                 'SubnetStatus': 'Active'}],
                                    'VpcId': 'vpc-80ccb9fd'},
                  'DbInstancePort': 0,
                  'DbiResourceId': 'db-ZNS7KUH2W7JPIVMBKQWOINBPYQ',
                  'DedicatedLogVolume': False,
                  'DeletionProtection': False,
                  'DomainMemberships': [],
                  'Endpoint': {'Address': 'mstdbinstance.coejywpn3aup.us-east-1.rds.amazonaws.com',
                               'HostedZoneId': 'Z2R2ITUGPM61AM',
                               'Port': 3306},
                  'Engine': 'mysql',
                  'EngineVersion': '8.0.35',
                  'IAMDatabaseAuthenticationEnabled': False,
                  'InstanceCreateTime': datetime.datetime(2024, 7, 21, 4, 34, 15, 675000, tzinfo=tzutc()),
                  'IsStorageConfigUpgradeAvailable': False,
                  'LatestRestorableTime': datetime.datetime(2024, 7, 21, 12, 40, tzinfo=tzutc()),
                  'LicenseModel': 'general-public-license',
                  'MasterUsername': 'admins',
                  'MonitoringInterval': 0,
                  'MultiAZ': False,
                  'NetworkType': 'IPV4',
                  'OptionGroupMemberships': [{'OptionGroupName': 'default:mysql-8-0',
                                              'Status': 'in-sync'}],
                  'PendingModifiedValues': {},
                  'PerformanceInsightsEnabled': False,
                  'PreferredBackupWindow': '04:13-04:43',
                  'PreferredMaintenanceWindow': 'sun:05:21-sun:05:51',
                  'PubliclyAccessible': True,
                  'ReadReplicaDBInstanceIdentifiers': [],
                  'StorageEncrypted': False,
                  'StorageThroughput': 0,
                  'StorageType': 'gp2',
                  'TagList': [],
                  'VpcSecurityGroups': [{'Status': 'active',
                                         'VpcSecurityGroupId': 'sg-567fb449'}]}],
 'ResponseMetadata': {'HTTPHeaders': {'content-length': '4523',
                                      'content-type': 'text/xml',
                                      'date': 'Sun, 21 Jul 2024 12:45:57 GMT',
                                      'strict-transport-security': 'max-age=31536000',
                                      'x-amzn-requestid': '899b26a9-4392-4105-9e72-fe658eba3e5a'},
                      'HTTPStatusCode': 200,
                      'RequestId': '899b26a9-4392-4105-9e72-fe658eba3e5a',
                      'RetryAttempts': 0}}


'''