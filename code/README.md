<!-- 
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->

# Deploy the code solution
*Note: everythuing in here falls under the free tier. However, there is a possibility of minimal charge if you are out of the free tier for Amazon Comprehend*
* Change to root of the code project directory
* Build the project:
```
sam build --use-container
```
*Note: the `--use-container` flag is only required if you do not have python 3.9*
* Deploy the application:
```
sam deploy -g --stack-name sam-demo
```
Accept defaults on all options **except** the following where you need to choose yes.
```bash
ReadFunction may not have authorization defined, Is this okay? [y/N]: y
WriteFunction may not have authorization defined, Is this okay? [y/N]: y
```

# Test the application

## Create entry
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

## Read all entries
Using CURL:

```
curl '<your domain>'
```

# Cleanup

Delete all resources:
```
sam delete --stack-name sam-demo
```
Enter Y to all options