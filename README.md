# github-to-lambda-demo
This project showcases a fully automated CI/CD pipeline that deploys a Python-based AWS Lambda function directly from a GitHub repository using AWS CodeBuild and Amazon S3.

🔧 Key Features:
. GitHub Trigger: GitHub push events trigger the pipeline via webhook

. Custom Build Logic: buildspec.yml handles zipping and uploading the Lambda deployment package

. Direct S3 Upload: The zipped package is uploaded to S3 manually using CLI commands in the buildspec

. Lambda Update: The function is updated using the uploaded zip file from S3

🛠 Skills & Tools Used:
. AWS Lambda – Serverless compute platform

. AWS CodeBuild – Automates build and packaging

. Lambda Layers – Includes external dependencies like pandas

. IAM Permissions – Grants Lambda and S3 access to CodeBuild

. Amazon S3 – Stores the zipped Lambda package

. CloudWatch Logs – Debug and monitor Lambda and build logs

. GitHub Webhook – Automatically starts the pipeline on code changes

