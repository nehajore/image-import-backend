import boto3

s3_client = boto3.client(
    "s3",
    endpoint_url="http://localhost:9000",
    aws_access_key_id="minioadmin",
    aws_secret_access_key="minioadmin",
    region_name="us-east-1"
)

BUCKET_NAME = "images-bucket"

def upload_image_to_minio(file_bytes, file_name, content_type="image/jpeg"):
    object_path = f"images/{file_name}"

    s3_client.put_object(
        Bucket=BUCKET_NAME,
        Key=object_path,
        Body=file_bytes,
        ContentType=content_type
    )

    return f"http://localhost:9000/{BUCKET_NAME}/{object_path}"
