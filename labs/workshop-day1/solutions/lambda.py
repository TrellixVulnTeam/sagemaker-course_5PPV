import boto3
import json
import base64

sagemaker_runtime_client = boto3.client('runtime.sagemaker')


def lambda_handler(event, context):
    values = base64.b64decode(event['values'])
    return _predict_hourse_price(values)


def _predict_hourse_price(values):
    response = sagemaker_runtime_client.invoke_endpoint(
        EndpointName='linear-learner-2021-09-07-18-56-37-086',
        ContentType='text/csv',
        Body=values
    )
    result = response['Body'].read()
    return json.loads(result)
