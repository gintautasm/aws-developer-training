"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import s3

#import random_string() function 
from generateRandomString import random_string


suffix = '8zvd6kc5or'#random_string()


# Create an AWS resource (S3 Bucket)
bucket = s3.Bucket(f'my-bucket-{suffix}')

# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)
