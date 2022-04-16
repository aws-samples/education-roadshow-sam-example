# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import os
import json
import boto3
from dynamodb_json import json_util as djson

ddb = boto3.client('dynamodb')

def lambda_handler(event, context):
    response = {"success": False}
    try:
        data = ddb.scan(TableName=os.environ["TABLE"])
        response = data["Items"]
        marshalled = djson.loads(response)
    except Exception as e:
        print(e)
    return {
        "statusCode": 200,
        "body": json.dumps(marshalled)
    }