import json

def hello(event, context):
    msg = 'helloWorld its me!'
    return {
        'body': json.dumps(msg)
    }