import json

def lambda_handler(event, context):
    """
    Error handling function for Step Functions demo.
    Catches and logs errors from the workflow.
    """
    try:
        # Log the error details
        error_info = event if isinstance(event, dict) else {"error": str(event)}
        
        print(f"Workflow error encountered: {json.dumps(error_info)}")
        
        return {
            "message": "Workflow error handled",
            "error_info": error_info,
            "statusCode": 500
        }
    except Exception as e:
        print(f"Error handling error: {str(e)}")
        return {
            "message": "Failed to handle workflow error",
            "statusCode": 500
        }
