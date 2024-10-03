# Task: Add the zip file to Source s3 BUCKET and receive the unzipped filed to Destination BUCKET in a FOLDER. Folder name should be same as Zip file

# Overview:

```sh
    Trigger: Lambda will be triggered whenever a ZIP file is uploaded to the source S3 bucket.
    Lambda Function: The Lambda function will download the ZIP file, unzip it, and upload the extracted files to a folder in the destination S3 bucket.
    IAM Role: The Lambda function will need permissions to read from the source bucket and write to the destination bucket.
```

# Step 1: Create S3 buckets

```sh
    Create two s3 buckets, One source and second destination.
    Give names: source-s3-bucket-for-zip and destination-bucket-for-zip
```

# Step 2: Create a Lambda Function

``` sh
    Go to the AWS Lambda Console and click Create function.
    Runtime: Choose Python 3.x 

    Click Create function.
```

# Step 3: Add the code to lambda code section

``` sh
    You can copy the code from the Zip2Unzip.py file from this repository and paste it to your lambda.
```

# Step 4: Set Up Permissions for Lambda

``` sh
    Go to the IAM Console.
    Create a new role with AWS Lambda as the trusted entity.
    In the "Attach permissions policies" step, search for the AmazonS3FullAccess policy.
```

# Step 5: Add the Trigger to Lambda

```sh
    Go to Lambda
    Click on add Trigger
    Select S3
    Select Source S3 bucket
```

# Step 6: Add timeout 

```sh
    Go to Lambda Console:
        Navigate to the AWS Lambda Console.

    Select Lambda Function

    Configuration Tab:
        In the Configuration tab, find the General configuration section.

    Edit Timeout Settings:
        Adjust the Timeout field (enter the time in seconds). For example, set it to 120 seconds (2 minutes) 

```

# Best Practices for Timeout:

```sh
    Small ZIP Files (< 5 MB):
        For smaller files, a timeout of 30–60 seconds is typically sufficient.

    Medium ZIP Files (5–100 MB):
        For medium-sized files, consider setting the timeout to 120–300 seconds (2–5 minutes), 
        depending on how quickly your Lambda function processes the files.

    Large ZIP Files (> 100 MB):
        For large files, you might need to set the timeout to 600–900 seconds (10–15 minutes), 
        especially if your Lambda function needs to handle large volumes of data or unzipping takes significant time.
```