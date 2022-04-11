<!-- 
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->

# Building a simple serverless application with SAM (Serverless Application Model)

This project builds a simple feedback application using AWS serverless. A user posts a simple string of text which is saved in an Amazon DynamoDB table. A Lambda function is then invoked to call Amazon Comprehend to evaluate if the string is positive, negative, or nutral.

## Prerequisites
* AWS account configured for [programatic access](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html)
* [AWS SAM CLI v1.46.0+](https://aws.amazon.com/serverless/sam/)
* Docker
* Python 3.9+ (If you want to modify the code)

## Deploying
*Note: everythuing in here falls under the free tier. However, there is a possibility of minimal charge if you are out of the free tier for Amazon Comprehend*
* Change to root of project directory
* Build the project:
```
sam build --use-container
```
* Deploy the application:
```
sam deploy -g
```
Accept defaults on all options **except** the following where you need to choose yes.
```bash
ReadFunction may not have authorization defined, Is this okay? [y/N]: y
WriteFunction may not have authorization defined, Is this okay? [y/N]: y
```

## Test the application

### Create entry
* Grab the **CommentUrl** from the output of the deployments
* Using CURL or Postman post a new comment to the endpoint with the following structure
```json
{
  "comment": "your comment here"
}
```

CURL example:
```
curl --location --request POST '<your domain>' --header 'Content-Type: application/json' --data-raw '{"comment":"your comment here"}'
```


curl 'https://q2t1gp5r01.execute-api.us-west-2.amazonaws.com/Prod/'

### Read all entries
Using CURL:

```
curl '<your domain>'
```

## Cleanup

Delete all resources:
```
sam delete --stack-name sam-demo
```
Enter Y to all options