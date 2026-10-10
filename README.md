# Thai Mobility Data Warehouse

## Overview

Thai Mobility Data Warehouse is an end-to-end data engineering project designed to process, validate, store, and analyze GPS trajectory data from taxis operating in Thailand.

The project demonstrates how raw mobility data can be transformed into structured, reliable, and queryable datasets through a data engineering pipeline.

The goal is to build a data warehouse that supports SQL-based analysis of vehicle movements, travel patterns, and transportation activity.

**Project Status:** Work in Progress

## Project Objectives

- Build a reproducible data pipeline for processing raw GPS data.
- Ingest data from source files into a structured storage environment.
- Validate and clean records to improve data quality.
- Transform raw GPS observations into analytics-ready datasets.
- Design a relational data warehouse for efficient SQL querying.
- Analyze mobility patterns and generate meaningful insights.
- Implement logging, data integrity checks, and automated processing.

## Planned Data Pipeline

```text
Raw GPS Dataset
       |
       v
Data Ingestion
       |
       v
Raw Data Storage
       |
       v
Data Validation & Cleaning
       |
       v
Data Transformation
       |
       v
Data Warehouse
       |
       v
SQL Analytics & Reporting
```

### 1. Data Ingestion

Read raw GPS records from source files and transfer them into a designated storage location.

File integrity checks using SHA-256 hashes help verify that files remain unchanged during ingestion.

### 2. Data Validation & Cleaning

Inspect incoming records for data quality issues, including:

- Missing or malformed values
- Invalid latitude and longitude coordinates
- Incorrect timestamps
- Invalid GPS status indicators
- Out-of-range numerical values

Invalid records will be identified and handled according to defined validation rules.

### 3. Data Transformation

Convert validated GPS records into structured datasets suitable for analytical processing.

Planned transformations include timestamp standardization, derived attributes, and aggregations to support mobility analysis.

### 4. Data Warehouse

Design and implement a relational data warehouse to organize processed mobility data.

The warehouse will support efficient SQL queries, aggregations, and analysis of vehicle activity over time.

### 5. Data Analytics

Use SQL to explore transportation patterns and answer questions such as:

- How does vehicle activity vary by hour or day?
- Which geographic areas experience higher taxi activity?
- What are the distributions of recorded vehicle speeds?
- How do vehicle movement patterns change over time?

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data ingestion, validation, and transformation |
| SQL | Data querying and analytical transformations |
| PostgreSQL (planned) | Relational data warehouse |
| Git & GitHub | Version control and project documentation |
| SHA-256 | File integrity verification |

Additional technologies may be introduced as the project develops.

## Dataset

The project uses sample GPS probe records containing vehicle identifiers, timestamps, geographic coordinates, speed, heading, GPS validity indicators, and vehicle status attributes.

These records provide the foundation for exploring mobility data processing and analytical warehouse design.

## Development Roadmap

- [x] Inspect raw CSV records and identify column data types
- [x] Implement initial GPS record validation
- [x] Implement file copying into a designated output directory
- [ ] Complete SHA-256 file integrity verification
- [ ] Develop a reusable data ingestion pipeline
- [ ] Implement systematic data quality checks
- [ ] Build data transformation processes
- [ ] Design the warehouse schema
- [ ] Load processed data into PostgreSQL
- [ ] Develop analytical SQL queries
- [ ] Add pipeline automation and logging
- [ ] Document analytical results and project findings

## Expected Outcome

The completed project aims to demonstrate a practical end-to-end data engineering workflow, from raw data ingestion to structured storage and SQL-based analysis.

It is developed as a hands-on learning project to strengthen skills in Python, SQL, data processing, database design, and data pipeline development.

## Author

Computer Engineering student developing practical data engineering skills through project-based learning.
