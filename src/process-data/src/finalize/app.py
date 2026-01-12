import json

def lambda_handler(event, context):
    """
    Finalize function for Step Functions demo.
    Consolidates results from parallel branches.
    """
    try:
        # Event can be a list of results from parallel branches
        result = event if isinstance(event, list) else [event]
        
        return {
            "message": "Workflow finalized successfully",
            "result": result,
            "statusCode": 200
        }
    except Exception as e:
        print(f"Error finalizing workflow: {str(e)}")
        raise
