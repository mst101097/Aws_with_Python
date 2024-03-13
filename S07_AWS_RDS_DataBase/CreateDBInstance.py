import boto3
from pprint import pprint
rds_client = boto3.client('rds',region_name='us-east-1')

response = rds_client.create_db_instance(
    DBName = "mstdb",
    DBInstanceIdentifier="mstdb",
    AllocatedStorage=20,
    DBInstanceClass='db.t2.micro',
    Engine='MySQL',
    MasterUsername='admins',
    MasterUserPassword='password',
    Port=3306,
    EngineVersion='8.0.35',
    PubliclyAccessible=True,
    StorageType='gp2'

)

print(response)

# {'DBInstance': {'DBInstanceIdentifier': 'mstdb', 'DBInstanceClass': 'db.t2.micro', 'Engine': 'mysql', 'DBInstanceStatus': 'creating', 'MasterUsername': 'admins', 'DBName': 'mstdb', 'AllocatedStorage': 20, 'PreferredBackupWindow': '07:54-08:24', 'BackupRetentionPeriod': 1, 'DBSecurityGroups': [], 'VpcSecurityGroups': [{'VpcSecurityGroupId': 'sg-0c5e687678f3ac524', 'Status': 'active'}], 'DBParameterGroups': [{'DBParameterGroupName': 'default.mysql8.0', 'ParameterApplyStatus': 'in-sync'}], 'DBSubnetGroup': {'DBSubnetGroupName': 'default', 'DBSubnetGroupDescription': 'default', 'VpcId': 'vpc-0f3d16c1dd7c51e4f', 'SubnetGroupStatus': 'Complete', 'Subnets': [{'SubnetIdentifier': 'subnet-051228a729432bf08', 'SubnetAvailabilityZone': {'Name': 'us-east-1c'}, 'SubnetOutpost': {}, 'SubnetStatus': 'Active'}, {'SubnetIdentifier': 'subnet-05c0ddf274830be6b', 'SubnetAvailabilityZone': {'Name': 'us-east-1d'}, 'SubnetOutpost': {}, 'SubnetStatus': 'Active'}, {'SubnetIdentifier': 'subnet-0d7826b6ac430a34f', 'SubnetAvailabilityZone': {'Name': 'us-east-1b'}, 'SubnetOutpost': {}, 'SubnetStatus': 'Active'}, {'SubnetIdentifier': 'subnet-040cf633714816085', 'SubnetAvailabilityZone': {'Name': 'us-east-1f'}, 'SubnetOutpost': {}, 'SubnetStatus': 'Active'}, {'SubnetIdentifier': 'subnet-0061e5098d2e8f94d', 'SubnetAvailabilityZone': {'Name': 'us-east-1e'}, 'SubnetOutpost': {}, 'SubnetStatus': 'Active'}, {'SubnetIdentifier': 'subnet-00d8ea42efe124d63', 'SubnetAvailabilityZone': {'Name': 'us-east-1a'}, 'SubnetOutpost': {}, 'SubnetStatus': 'Active'}]}, 'PreferredMaintenanceWindow': 'thu:08:47-thu:09:17', 'PendingModifiedValues': {'MasterUserPassword': '****'}, 'MultiAZ': False, 'EngineVersion': '8.0.35', 'AutoMinorVersionUpgrade': True, 'ReadReplicaDBInstanceIdentifiers': [], 'LicenseModel': 'general-public-license', 'OptionGroupMemberships': [{'OptionGroupName': 'default:mysql-8-0', 'Status': 'in-sync'}], 'PubliclyAccessible': True, 'StorageType': 'gp2', 'DbInstancePort': 0, 'StorageEncrypted': False, 'DbiResourceId': 'db-GVTY25J6NQRBJNUTIP2DEIQ7WY', 'CACertificateIdentifier': 'rds-ca-rsa2048-g1', 'DomainMemberships': [], 'CopyTagsToSnapshot': False, 'MonitoringInterval': 0, 'DBInstanceArn': 'arn:aws:rds:us-east-1:642678036539:db:mstdb', 'IAMDatabaseAuthenticationEnabled': False, 'PerformanceInsightsEnabled': False, 'DeletionProtection': False, 'AssociatedRoles': [], 'TagList': [], 'CustomerOwnedIpEnabled': False, 'BackupTarget': 'region', 'NetworkType': 'IPV4', 'StorageThroughput': 0, 'CertificateDetails': {'CAIdentifier': 'rds-ca-rsa2048-g1'}, 'DedicatedLogVolume': False}, 'ResponseMetadata': {'RequestId': 'b5558843-ea0f-45cf-aabc-cfbef50ffb75', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'b5558843-ea0f-45cf-aabc-cfbef50ffb75', 'strict-transport-security': 'max-age=31536000', 'content-type': 'text/xml', 'content-length': '4028', 'date': 'Wed, 13 Mar 2024 03:06:39 GMT'}, 'RetryAttempts': 0}}