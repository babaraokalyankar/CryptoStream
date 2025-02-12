# Cryptocurrency Kafka Real-Time Data Engineering Project

## Introduction
This project demonstrates an **End-To-End Data Engineering Pipeline** for processing real-time cryptocurrency market data using **Apache Kafka**, **AWS Cloud Services**, and modern data tools. The pipeline ingests live cryptocurrency prices, processes streams, stores data in a data lake, and enables SQL analytics.

![Project Architecture](https://via.placeholder.com/800x400.png?text=Cryptocurrency+Kafka+Data+Pipeline+Architecture)  
*Diagram 1: High-Level Architecture*

## Technology Stack
- **Programming Language**: Python 3.8+
- **Stream Processing**: Apache Kafka
- **Cloud Services** (AWS):
  - S3 (Data Lake Storage)
  - EC2 (Kafka Server)
  - Glue (Data Catalog)
  - Athena (SQL Analytics)
  - IAM (Security Configuration)
- **Data Tools**: Pandas, AWS CLI, Kafka-Python

## Dataset
Real-time cryptocurrency price data from multiple exchanges, containing:
- Timestamps
- Cryptocurrency symbols (BTC, ETH, etc.)
- Price in USD
- 24h Volume
- Market Cap
- Price change percentages

Sample Dataset: [CryptoCompare Historical Data](https://www.cryptocompare.com/api/)

## Architecture Overview

```plaintext
+-----------------+      +-------------+      +-----------+      +------------+
| Crypto Exchanges|      | Kafka       |      | AWS        |      | Analytics  |
| (REST API)      +----->+ Producer    +----->+ S3 Data    +----->+ with       |
| CoinGecko/      |      | (EC2)       |      | Lake       |      | Athena/GLUE|
| Binance/etc.    |      |             |      |            |      |            |
+-----------------+      +------+------+      +-----+------+      +------------+
                                |                   |
                          +-----v------+     +------v-----+
                          | Kafka      |     | Data       |
                          | Consumer   |     | Cataloging |
                          | (EC2)      |     | (Glue)     |
                          +------------+     +------------+
