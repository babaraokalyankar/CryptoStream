from kafka import KafkaConsumer
import json
import boto3
import time

# AWS S3 client setup
s3 = boto3.client(
    's3',
    aws_access_key_id='****************', 
    aws_secret_access_key='***************************'
)

# Kafka consumer configuration
consumer = KafkaConsumer(
    'crypto-data',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Real-time upload to S3
for message in consumer:
    data = message.value
    print(f"Received: {data}")

    # Generate a unique filename for each message
    timestamp = int(time.time())
    s3_key = f"real-time-data/{timestamp}.json"

    # Upload the message to S3
    s3.put_object(
        Bucket='crypto-data-bucket-123',
        Key=s3_key,
        Body=json.dumps(data)
    )
    print(f"Uploaded {s3_key} to S3!")