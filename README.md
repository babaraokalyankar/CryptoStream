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
- SNo
- Name
- Symbol
- Date
- High
- Low
- Open
- Close
- Volume
- Marketcap


Sample Dataset: [Cryptocurrency Historical Prices](https://www.kaggle.com/datasets/sudalairajkumar/cryptocurrencypricehistory)
