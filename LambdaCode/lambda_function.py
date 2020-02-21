import json

def lambda_function(event, context):
    msg = 'helloWorld !'
    return{
        'body':json.dumps(msg)
    }