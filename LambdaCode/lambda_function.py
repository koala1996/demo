import json

def lambda_handler(event, context):
    msg = 'helloWorld !'
    return{
        'body':json.dumps(msg)
    }