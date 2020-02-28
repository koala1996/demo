import json

def lambda_handler(event, context):
    msg = 'helloWorld Demo'
    return{
        'body':json.dumps(msg)
    }