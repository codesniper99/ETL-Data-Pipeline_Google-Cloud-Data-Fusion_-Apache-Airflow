# ETL Data Pipeline for Simulating Netflix Streaming Data

This repository contains an ETL (Extract, Transform, Load) pipeline designed to simulate Netflix streaming data. The pipeline extracts dummy data, stores it in Google Cloud Storage, processes it using Google Cloud Data Fusion and Google Cloud Dataprep, and loads it into Google BigQuery for visualization in Looker Studio. The entire process is automated using Apache Airflow.


![Data Flow](images/ETL%20Pipeline.jpg)

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Components](#components)
  - [Data Extraction](#data-extraction)
  - [Data Transformation](#data-transformation)
  - [Data Loading](#data-loading)
  - [Visualization](#visualization)
  - [Automation](#automation)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project demonstrates the use of various Google Cloud Platform (GCP) services to create an end-to-end data pipeline. The goal is to simulate a streaming service environment, similar to Netflix, and process the data to generate insights.

## Architecture

The pipeline consists of the following steps:

1. **Data Extraction**: Generate dummy streaming data using the Faker library.
2. **Data Storage**: Store the extracted data in Google Cloud Storage (GCS).
3. **Data Transformation**: Use Google Cloud Data Fusion to clean and transform the data.
4. **Data Loading**: Load the transformed data into Google BigQuery.
5. **Visualization**: Create interactive dashboards in Looker Studio.
6. **Automation**: Automate the entire process using Apache Airflow.

## Components

### Data Extraction

The data extraction process is implemented in the `extract.py` script. This script uses the `Faker` library to generate realistic dummy data representing users, their activities, and other relevant details.



### Data Transformation

Google Cloud Data Fusion is used to clean and transform the extracted data. The transformations ensure that the data is structured and ready for analysis.

### Data Loading

Transformed data is loaded into Google BigQuery, where it can be queried and analyzed. BigQuery offers a scalable and efficient way to handle large datasets.

### Visualization

Looker Studio (formerly Google Data Studio) is used to create interactive dashboards that visualize the data. These dashboards provide insights into user behavior, content popularity, and other key metrics.

### Automation

Apache Airflow orchestrates the entire ETL process. The `dag.py` script defines a Directed Acyclic Graph (DAG) that schedules and manages the tasks.

## Prerequisites

- Google Cloud Platform account
- Apache Airflow installed
- Google Cloud SDK installed and configured
- Python 3.x installed

## Setup

1. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/netflix-etl-pipeline.git
   cd netflix-etl-pipeline
   ```
2. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/netflix-etl-pipeline.git
   cd netflix-etl-pipeline
   ```
3. **Install the required Python packages:**
   ```
   pip install -r requirements.txt
   ```
4. **Set up Google Cloud Storage:**
   
    * Create a GCS bucket.
    * Update the bucket name in extract.py.
   
5. **Configure Google Cloud Data Fusion and BigQuery:**
   
   *   Set up a Data Fusion instance.
   * Create a BigQuery dataset.
6. **Configure Apache Airflow:**
   * Update the DAG configuration in dag.py with your project-specific details.