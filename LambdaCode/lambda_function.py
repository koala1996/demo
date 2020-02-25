import json

def lambda_handler(event, context):
    msg = 'helloWorld its me! mario 2'
    return{
        'body':json.dumps(msg)
    }