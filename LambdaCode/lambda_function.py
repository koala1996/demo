import json

def lambda_handler(event, context):
    msg = 'helloWorld its me! peter'
    return{
        'body':json.dumps(msg)
    }