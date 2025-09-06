# Vrum Backend

FastAPI backend application with PostgreSQL database.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start PostgreSQL database:
```bash
docker-compose up -d
```

3. Start the application:
```bash
python run.py
```

The API will be available at http://localhost:8000

## API Documentation

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Project Structure

- `app/` - Main application code
- `app/main.py` - FastAPI application entry point
- `app/database.py` - Database configuration
- `run.py` - Application runner script

## Docker

### Build and run with Docker Compose
```bash
docker-compose up --build
```

### Build Docker image
```bash
docker build -t vrum-backend .
```

### Run Docker container
```bash
docker run -p 8000:8000 vrum-backend
```
