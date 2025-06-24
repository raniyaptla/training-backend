# Simple Backend with PostgreSQL Connection

A minimal FastAPI application that establishes a connection to PostgreSQL database.

## Features

- **FastAPI** framework
- **PostgreSQL** connection using asyncpg
- **Docker** containerization
- **Connection testing** on startup

## Project Structure

```
backend/
├── main.py              # Main FastAPI application
├── requirements.txt     # Python dependencies
├── Dockerfile          # Docker configuration for the app
├── docker-compose.yml  # Multi-service Docker setup
├── .env               # Environment variables template
├── .dockerignore      # Docker ignore file
└── README.md          # This file
```

## API Endpoints

### General
- `GET /` - Root endpoint showing connection status

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `POSTGRES_HOST` | PostgreSQL host | localhost |
| `POSTGRES_PORT` | PostgreSQL port | 5432 |
| `POSTGRES_USER` | PostgreSQL username | postgres |
| `POSTGRES_PASSWORD` | PostgreSQL password | password |
| `POSTGRES_DB` | PostgreSQL database name | myapp |

## Quick Start

### Using Docker Compose (Recommended)

1. Clone the repository and navigate to the backend directory
2. Run the entire stack:
   ```bash
   docker-compose up --build
   ```

This will start:
- FastAPI app on port 8001
- PostgreSQL on port 5432

### Using Docker (App Only)

1. Build the Docker image:
   ```bash
   docker build -t backend-api .
   ```

2. Run the container:
   ```bash
   docker run -p 8001:8001 backend-api
   ```

### Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up environment variables in `.env` file

3. Run the application:
   ```bash
   python main.py
   ```

## Testing the API

Once the application is running, you can:

1. Visit `http://localhost:8001` to see the root endpoint
2. Check health status at `http://localhost:8001/health`
3. View interactive API docs at `http://localhost:8001/docs`
4. View alternative API docs at `http://localhost:8001/redoc`

### Example API Calls

### Example API Call

Check connection status:
```bash
curl "http://localhost:8001/"
```

## Development

- The application uses FastAPI's lifespan events to manage database connection
- Database connection is established on startup and closed on shutdown
- Connection is tested on startup to verify PostgreSQL is accessible
- Simple root endpoint shows connection status

## Production Considerations

- Update CORS origins to specific domains instead of allowing all
- Use proper secrets management for database passwords
- Implement proper logging and monitoring
- Add input validation and error handling
- Consider using connection pooling for better performance
- Add rate limiting and authentication as needed
