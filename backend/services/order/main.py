from fastapi import FastAPI

app = FastAPI(title="Order Service")

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "order-service"}

@app.post("/orders")
async def create_order(order: dict):
    return {"order_id": "12345", "status": "created"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8003)
