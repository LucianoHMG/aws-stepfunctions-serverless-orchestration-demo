import json

def lambda_handler(event, context):
    """
    Process data function for Step Functions demo.
    Validates and enriches input data.
    """
    try:
        data = event or {}
        data.setdefault("status", "PROCESSED")
        data.setdefault("timestamp", str(context.invoked_function_arn))
        
        return {
            "id": data.get("id", "unknown"),
            "payload": data,
            "statusCode": 200
        }
    except Exception as e:
        print(f"Error processing data: {str(e)}")
        raise
