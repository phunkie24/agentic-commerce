from fastapi import FastAPI

app = FastAPI(title="Product Service")

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "product-service"}

@app.get("/products/{product_id}")
async def get_product(product_id: str):
    return {"id": product_id, "name": "Sample Product", "price": 99.99}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
