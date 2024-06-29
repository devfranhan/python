import boto3
import os

def get_s3_client(access_key, secret_key):
    """
    Configure the S3 client with the given access and secret keys.
    """
    return boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)

def list_s3_objects(s3_client, bucket_name):
    """
    List all objects in the specified S3 bucket.
    """
    return s3_client.list_objects(Bucket=bucket_name)

def ensure_local_directory_exists(path):
    """
    Ensure the local directory exists; if not, create it.
    """
    if not os.path.exists(path):
        os.makedirs(path)

def download_s3_objects(s3_client, bucket_name, local_folder_path, objects):
    """
    Iterate over the objects in the bucket and download them to the local folder.
    """
    for obj in objects.get('Contents', []):
        object_key = obj['Key']
        local_file_path = os.path.join(local_folder_path, object_key)
        local_directory = os.path.dirname(local_file_path)
        
        ensure_local_directory_exists(local_directory)
        
        print(f'Downloading {object_key} to {local_file_path}')
        s3_client.download_file(bucket_name, object_key, local_file_path)
    print('Download completed!')

def main():
    """
    Main function to download files from S3 to a local folder.
    """
    # Configuration
    access_key = 'ACCESS_KEY'
    secret_key = 'SECRET_KEY'
    bucket_name = 'my.bucket.name'
    local_folder_path = "//path/to/local/folder"
    
    print(local_folder_path)
    
    # Configure the S3 client
    s3_client = get_s3_client(access_key, secret_key)
    
    # List all objects in the bucket
    response = list_s3_objects(s3_client, bucket_name)
    
    # Ensure the local folder exists
    ensure_local_directory_exists(local_folder_path)
    
    # Download objects from S3 to the local folder
    download_s3_objects(s3_client, bucket_name, local_folder_path, response)

if __name__ == "__main__":
    main()
