from fastapi import FastAPI

app = FastAPI(title="Analytics Service")

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "analytics-service"}

@app.get("/analytics/dashboard")
async def get_dashboard():
    return {"metrics": {"users": 100, "orders": 50}}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8005)
