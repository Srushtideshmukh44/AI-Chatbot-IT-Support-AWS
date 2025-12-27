import json

def lambda_handler(event, context):

    # ✅ Handle CORS preflight (OPTIONS request)
    if event.get("httpMethod") == "OPTIONS":
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "POST,OPTIONS"
            },
            "body": ""
        }

    body = {}
    if event.get("body"):
        body = json.loads(event["body"])

    user_message = body.get("message", "").lower()

    if "server" in user_message:
        reply = "It looks like the server is down. Please check EC2 instance status and security group rules."
    elif "application" in user_message:
        reply = "Please restart the application service and check application logs."
    elif "password" in user_message:
        reply = "For password reset, please use the self-service portal or contact IT admin."
    elif "disk" in user_message:
        reply = "Disk space seems full. Please clear old logs or increase disk size."
    elif "vpn" in user_message:
        reply = "Please check your internet connection and VPN credentials."
    else:
        reply = "Sorry, I couldn't understand the issue. Please contact IT support."

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "POST,OPTIONS"
        },
        "body": json.dumps({
            "reply": reply
        })
    }
