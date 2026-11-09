from fastapi import FastAPI

app = FastAPI(title="Recommendation Service")

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "recommendation-service"}

@app.get("/recommendations/{user_id}")
async def get_recommendations(user_id: str):
    return {"recommendations": [{"id": "1", "name": "Recommended Product"}]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8004)
