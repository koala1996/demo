import json

def lambda_handler(event, context):
    msg = 'helloWorld its me!'
    return{
        'body':json.dumps(msg)
    }