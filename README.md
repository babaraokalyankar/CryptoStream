# Cryptocurrency Kafka Real-Time Data Engineering and Machine Learning Project

## Introduction
This project demonstrates an **End-To-End Data Engineering Pipeline** for processing real-time cryptocurrency market data using **Apache Kafka**, **AWS Cloud Services**, and modern data tools. The pipeline ingests live cryptocurrency prices, processes streams, stores data in a data lake, enables SQL analytics, and incorporates machine learning models for market trend predictions and incorporates machine learning models for market trend predictions.It integrates two ML models:

RNN: For market trend forecasting.

XGBoost: For predicting cryptocurrency prices using large-scale data. 

## Architecture Digram :
![Architecture](ArchitectureDigram.jpg)


## Technology Stack
- **Programming Language**: Python 3.8+
- **Stream Processing**: Apache Kafka
- **Cloud Services** (AWS):
  - S3 (Data Lake Storage)
  - EC2 (Kafka Server)
  - Glue (Data Catalog)
  - Athena (SQL Analytics)
  - IAM (Security Configuration)
- **Machine Learning**:
  - RNN Model and XGBoost with **PySpark** on AWS for cryptocurrency price predictions
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

**AWS Athena Query:**
  
   Daily Price Volatility Analysis
  
   ![Athena Query](q1.png)
   ![Athena Query](r1.png)

## Machine Learning Models
- **RNN**:  Recurrent Neural Networks used for sequential data analysis and market trend forecasting.
- **XGBoost**: A gradient boosting algorithm used for predictive analysis, applied to the processed cryptocurrency data for price predictions.
  
**RNN Model**
  ![RNN Model](cryptoRNN.png)

**XGBoost Model Using Pyspark**
  ![XGBoost Model](pyspark.png)


