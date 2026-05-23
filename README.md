# Take-Home Assignement Question 1 (REST APIs)

## Overview
Simple implementation using FastAPI, accepts input CSV log file and outputs a report summary of the logs

Github: 

## Tech Stack
- Python 3.14.5
- FastAPI
- Uvicorn
- Pandas
- SciPy
- Chardet

## Project Structure
```text
project-root/
├── restapi/
    ├── Dockerfile
    ├── M6.csv
    ├── my_rest_api.py
    ├── test.py
├── docker-compose.yml
├── README.md
├── requirements.txt
```

## API Endpoint

### POST '/generateReport'
Accepts CSV file with log data, does processing on it and returns a report smmary of the logs

#### Input
- **Type:** CSV file
- **Field name:** `file`

#### Output
- **Type:** JSON
- A report summary for each numerical column:
    - max
    - min
    - mean
    - std
    - kurtosis

## How to Run
#### Navigate to project root
```bash
cd GroundupAI-Assignment1
```

#### Build and start application
```bash
docker compose up --build
```