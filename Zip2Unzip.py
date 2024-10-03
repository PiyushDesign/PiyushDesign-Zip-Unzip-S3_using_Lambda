import boto3
import os
import zipfile
import tempfile

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Get the bucket name and file key from the S3 event
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    zip_key = event['Records'][0]['s3']['object']['key']
    
    # Define destination bucket
    destination_bucket = 'destination-bucket-for-zip'
    
    # Create a temporary directory to download and unzip files
    with tempfile.TemporaryDirectory() as tmpdirname:
        zip_path = os.path.join(tmpdirname, os.path.basename(zip_key))
        
        # Download the zip file from the source S3 bucket
        s3.download_file(source_bucket, zip_key, zip_path)
        
        # Unzip the file
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(tmpdirname)
        
        # Folder name based on the ZIP file (without extension)
        folder_name = os.path.splitext(os.path.basename(zip_key))[0]
        
        # Upload each file in the unzipped directory to the destination bucket
        for root, dirs, files in os.walk(tmpdirname):
            for file in files:
                file_path = os.path.join(root, file)
                s3_key = f"{folder_name}/{file}"
                
                # Upload the file to the destination bucket
                s3.upload_file(file_path, destination_bucket, s3_key)
                print(f"Uploaded {file} to s3://{destination_bucket}/{s3_key}")
    
    return {
        'statusCode': 200,
        'body': f"Successfully processed {zip_key}"
    }
