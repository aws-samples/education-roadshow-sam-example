<!-- 
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->

# Building a simple serverless application with SAM (Serverless Application Model)

This project contains two versions of a similar app. The app is a feedback application that accepts comments and evaluates them using Amazon Comprehend to see if the feedback is positive, negativwe, or somewhere in between.

## Prerequisites
* AWS account configured for [programatic access](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html)
* [AWS SAM CLI v1.46.0+](https://aws.amazon.com/serverless/sam/)
* Docker
* Python 3.9+ (If you want to modify the code)

# Version 1
This version deploys an Amazon DynamoDB database and three AWS lambda functions. When a comment is written to the database, DynamoDB streams invokes a Lambda to call Amazon Comprehend, evaluate the comment, and write the results back to the database.

[Deploy this version](./code/README.md)

# Version 2
This version takes a low-code approach and uses AWS Step Functions to communicate with Amazon Comprehend and writes the data to Amazon DynamoDB. This example takes it a step further. If the feedback is positive, the comments are translated to Spanish and German to be shared with friends.

[Deploy this version](./low-code/README.md)