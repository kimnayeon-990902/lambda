import json

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": "Hello, AWS Lambda!"
    }


    # 들어오는 이벤트 로그
    print("Event:", event)

    # 응답 메시지
    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "message": "Hello from AWS Lambda!",
            "input": event
        })
    }

    return response
