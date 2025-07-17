# 🚀 Serverless Data Processing and Machine Learning Pipeline

## 📌 Project Overview

This project demonstrates a complete **serverless architecture** for scalable **ETL (Extract, Transform, Load)** and **machine learning model development** using:

- **Azure Synapse Serverless SQL**
- **Azure Databricks (Community Edition)**
- **Azure DevOps**
- **Azure Data Lake Storage Gen2**
- **MLflow for experiment tracking**

It simulates a real-world production-grade **data engineering and ML workflow**, leveraging CI/CD automation, modular architecture, and on-demand clusters.

---

## 🗂️ Dataset

**Dataset Name:** NYC Yellow Taxi Trip Data  
**Source:** NYC TLC Open Data  
**Size:** ~2 GB  
**File Format:** CSV  

### Key Features:
- `tpep_pickup_datetime`, `tpep_dropoff_datetime` – Trip timing  
- `trip_distance` – Distance covered  
- `fare_amount`, `tip_amount`, `total_amount` – Fare details  
- `passenger_count` – Number of passengers  
- `PULocationID`, `DOLocationID` – Pickup and dropoff zones  
- `payment_type` – Mode of payment

---

## Architecture

### High-Level Components

1. **Bronze Layer (Raw Ingestion):**
   - CSV ingested into ADLS using Synapse Serverless SQL or Databricks.

2. **Silver Layer (Cleaning + Transformation):**
   - Data cleansing, type casting, enrichment, and filtering using Spark SQL and PySpark.

3. **Gold Layer (ML Ready Features):**
   - Feature engineering, vectorization, scaling, and clustering with KMeans.

4. **ML Model Training & Tracking:**
   - Trained using Spark MLlib
   - Evaluation using Silhouette Score
   - Logged and tracked with MLflow

5. **CI/CD + Automation:**
   - Git integration using **Azure DevOps Repos**
   - ML pipeline orchestration and job triggering using Azure Functions and DevOps YAML pipelines

---

## Machine Learning

### Model: KMeans Clustering
- **Goal:** Segment customers/trips into distinct groups
- **Features Used:**
  - `trip_distance`
  - `fare_amount`
  - `passenger_count`

### Steps Involved:
1. Feature Selection & Engineering  
2. Vector Assembling & Standard Scaling  
3. Train/Test Split  
4. KMeans Model Training (k=4)  
5. Prediction & Evaluation (Silhouette Score)  
6. MLflow Tracking  
7. Output saved to ADLS (Gold)

---

## CI/CD Automation

### DevOps Lifecycle
- Source code stored in **Azure DevOps Git Repos**
- Jobs triggered using **Azure Pipelines**
- Infrastructure defined using **ARM Templates**
- ML runs tracked with **MLflow UI**

---

## Demo & Screenshots

Due to credit exhaustion in our Azure account, we recorded screenshots and notebooks as part of the final review. The working pipeline can be viewed in:
- **Azure DevOps Repository**
- **Azure Notebooks & MLflow Tracking UI**
- **Synapse Serverless SQL scripts**

---

## 📦 Directory Structure

