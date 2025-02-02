from kafka import KafkaProducer
import pandas as pd
import time
import json

# Kafka producer configuration
producer = KafkaProducer(
    bootstrap_servers='localhost:9092', 
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# List of CSV files
files = [
    'coin_Aave.csv', 'coin_BinanceCoin.csv', 'coin_Bitcoin.csv',
    'coin_Cardano.csv', 'coin_ChainLink.csv', 'coin_Cosmos.csv',
    'coin_CryptocomCoin.csv', 'coin_Dogecoin.csv', 'coin_EOS.csv',
    'coin_Ethereum.csv', 'coin_lota.csv', 'coin_Litecoin.csv',
    'coin_Monero.csv', 'coin_NEM.csv', 'coin_Polkadot.csv',
    'coin_Solana.csv', 'coin_Stellar.csv', 'coin_Tether.csv',
    'coin_Tron.csv'
]

# Function to send data to Kafka
def send_to_kafka(file):
    df = pd.read_csv(file)
    for _, row in df.iterrows():
        # Convert row to dictionary
        data = row.to_dict()
        # Send data to Kafka topic
        producer.send('crypto-data', data)
        print(f"Sent: {data}")
        time.sleep(1)  # Simulate real-time delay

# Send data from all files
for file in files:
    send_to_kafka(file)

producer.flush()