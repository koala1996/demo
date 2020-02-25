import json

def lambda_handler(event, context):
    msg = 'helloWorld its me! Peter'
    return{
        'body':json.dumps(msg)
    }