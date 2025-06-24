from fastapi import FastAPI
import asyncpg
import os
import uvicorn

# Create FastAPI app
app = FastAPI(title="Simple PostgreSQL Backend")

# Database connection variable
db_connection = None

@app.on_event("startup")
async def startup():
    """Connect to database when app starts"""
    global db_connection
    try:
        # Connect to PostgreSQL
        db_connection = await asyncpg.connect(
            host=os.getenv("POSTGRES_HOST", "localhost"),
            port=os.getenv("POSTGRES_PORT", "5432"),
            user=os.getenv("POSTGRES_USER", "postgres"),
            password=os.getenv("POSTGRES_PASSWORD", "password"),
            database=os.getenv("POSTGRES_DB", "myapp")
        )
        print("Connected to PostgreSQL!")
        
        # Test connection
        result = await db_connection.fetchval("SELECT 'Hello from PostgreSQL!'")
        print(f"Database says: {result}")
        
    except Exception as e:
        print(f"Database connection failed: {e}")

@app.on_event("shutdown")
async def shutdown():
    """Close database connection when app stops"""
    global db_connection
    if db_connection:
        await db_connection.close()
        print("Database connection closed")

@app.get("/")
async def home():
    """Simple home page"""
    if db_connection:
        return {"message": "Database is connected "}
    else:
        return {"message": "Database is not connected "}

# Run the app
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)