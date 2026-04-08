# Decoupled AWS S3 Data Pipeline & Headless Architecture

## Architectural Overview
Data engineering pipeline designed to process, structure, and serve massive datasets (600GB+) with $0 idle server costs. By decoupling the heavy data layer from the frontend application, we achieve infinite scalability via AWS CloudFront.

## Pipeline Features
* **Automated Data Hydration:** Python automation that processes cloud-stored assets locally using smart sampling to prevent local disk exhaustion.
* **Metadata Extraction:** Dynamically extracts EXIF data to construct chronological JSON manifests.
* **Serverless Edge Delivery:** Terraform definitions for S3 buckets locked behind CloudFront Origin Access Control (OAC).

## The Business Value
Guarantees 99.999% data durability, eliminates server CPU overload during millions of concurrent read requests, and reduces idle CapEx to zero.
