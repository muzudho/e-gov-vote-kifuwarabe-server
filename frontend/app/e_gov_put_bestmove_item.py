"""
python.exe e_gov_put_bestmove_item.py
"""

import boto3


def put_bestmove(your_name, secret, bestmove, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Bestmove')
    response = table.put_item(
        Item={
            'yourName': your_name,
            'secret': secret,
            # 属性は定義してなくても追加できます
            'bestmove': bestmove,
        }
    )
    return response
