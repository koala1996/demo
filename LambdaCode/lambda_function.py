import json

def lambda_handler(event, context):
    msg = 'helloWorld its me! mario'
    return{
        'body':json.dumps(msg)
    }