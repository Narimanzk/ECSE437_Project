# ECSE437: Software Delivery - Project

## Narry Zendehrooh Kermani: 260700556
## Kyjauna Marshall: 260802473
## Introduction
A simple application for fetching and inserting movies using Rest API with unit test and integration test. 

## Requirements
- Application is developed in Python 3.9
- You can install the packages using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

## How to Use

**To run the application locally, you need to setup a database instance and implement an endpoint for the external movie client.**

### To run all tests
```bash
pytest test
```

### To run only unit tests
```bash
pytest test/ -k 'test and not integration'
```

### To run only integration tests
```bash
pytest test/ -k 'integration'
```

### Technologies used
- `FastAPI` and `uvicorn` for Rest API
- `unittest` for assertions and mocks
- `testcontainers` to initialize local-database for integration tests
- `Flask` for MockServer
- `pandas` for all dataframe operations
- `psycopg2` to create a connection