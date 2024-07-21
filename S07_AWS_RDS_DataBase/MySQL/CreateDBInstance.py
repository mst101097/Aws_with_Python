import boto3
from pprint import pprint
rds_client = boto3.client('rds',region_name='us-east-1')

response = rds_client.create_db_instance(
    DBName = "mstdb",
    DBInstanceIdentifier="mstdbinstance",
    AllocatedStorage=20,
    DBInstanceClass='db.t3.micro',
    Engine='mysql',
    MasterUsername='admins',
    MasterUserPassword='password',
    Port=3306,
    EngineVersion='8.0.35',
    PubliclyAccessible=True,
    StorageType='gp2'

)

print(response)

#{'DBInstance': {'DBInstanceIdentifier': 'mstdbinstance', 'DBInstanceClass': 'db.t3.micro', 'Engine': 'mysql', 'DBInstanceStatus': 'creating', 'MasterUsername': 'admins', 'DBName': 'mstdb', 'AllocatedStorage': 20, 'PreferredBackupWindow': '04:13-04:43', 'BackupRetentionPeriod': 1, 'DBSecurityGroups': [], 'VpcSecurityGroups': [{'VpcSecurityGroupId': 'sg-567fb449', 'Status': 'active'}], 'DBParameterGroups': [{'DBParameterGroupName': 'default.mysql8.0', 'ParameterApplyStatus': 'in-sync'}], 'DBSubnetGroup': {'DBSubnetGroupName': 'default', 'DBSubnetGroupDescription': 'default', 'VpcId': 'vpc-80ccb9fd', 'SubnetGroupStatus': 'Complete', 'Subnets': [{'SubnetIdentifier': 'subnet-f60e2ba9', 'SubnetAvailabilityZone': {'Name': 'us-east-1c'}, 'SubnetOutpost': {}, 'SubnetStatus': 'Active'}, {'SubnetIdentifier': 'subnet-cb2f3dc5', 'SubnetAvailabilityZone': {'Name': 'us-east-1f'}, 'SubnetOutpost': {}, 'SubnetStatus': 'Active'}, {'SubnetIdentifier': 'subnet-ce9cf0ff', 'SubnetAvailabilityZone': {'Name': 'us-east-1e'}, 'SubnetOutpost': {}, 'SubnetStatus': 'Active'}, {'SubnetIdentifier': 'subnet-cf97b0ee', 'SubnetAvailabilityZone': {'Name': 'us-east-1a'}, 'SubnetOutpost': {}, 'SubnetStatus': 'Active'}, {'SubnetIdentifier': 'subnet-c809e184', 'SubnetAvailabilityZone': {'Name': 'us-east-1b'}, 'SubnetOutpost': {}, 'SubnetStatus': 'Active'}, {'SubnetIdentifier': 'subnet-34603852', 'SubnetAvailabilityZone': {'Name': 'us-east-1d'}, 'SubnetOutpost': {}, 'SubnetStatus': 'Active'}]}, 'PreferredMaintenanceWindow': 'sun:05:21-sun:05:51', 'PendingModifiedValues': {'MasterUserPassword': '****'}, 'MultiAZ': False, 'EngineVersion': '8.0.35', 'AutoMinorVersionUpgrade': True, 'ReadReplicaDBInstanceIdentifiers': [], 'LicenseModel': 'general-public-license', 'OptionGroupMemberships': [{'OptionGroupName': 'default:mysql-8-0', 'Status': 'in-sync'}], 'PubliclyAccessible': True, 'StorageType': 'gp2', 'DbInstancePort': 0, 'StorageEncrypted': False, 'DbiResourceId': 'db-ZNS7KUH2W7JPIVMBKQWOINBPYQ', 'CACertificateIdentifier': 'rds-ca-rsa2048-g1', 'DomainMemberships': [], 'CopyTagsToSnapshot': False, 'MonitoringInterval': 0, 'DBInstanceArn': 'arn:aws:rds:us-east-1:375253976385:db:mstdbinstance', 'IAMDatabaseAuthenticationEnabled': False, 'PerformanceInsightsEnabled': False, 'DeletionProtection': False, 'AssociatedRoles': [], 'TagList': [], 'CustomerOwnedIpEnabled': False, 'BackupTarget': 'region', 'NetworkType': 'IPV4', 'StorageThroughput': 0, 'CertificateDetails': {'CAIdentifier': 'rds-ca-rsa2048-g1'}, 'DedicatedLogVolume': False}, 'ResponseMetadata': {'RequestId': 'b20683d0-b40b-4ac6-a887-907f2818d94b', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'b20683d0-b40b-4ac6-a887-907f2818d94b', 'strict-transport-security': 'max-age=31536000', 'content-type': 'text/xml', 'content-length': '4053', 'date': 'Sun, 21 Jul 2024 04:30:41 GMT'}, 'RetryAttempts': 0}}