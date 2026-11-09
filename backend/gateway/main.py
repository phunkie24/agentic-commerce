from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os

app = FastAPI(title="Agentic Commerce API Gateway")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatMessage(BaseModel):
    message: str
    user_id: str

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "api-gateway"}

@app.post("/api/chat/message")
async def chat_message(msg: ChatMessage):
    return {
        "success": True,
        "response": f"Received: {msg.message}",
        "user_id": msg.user_id
    }

@app.get("/api/products/search")
async def search_products(q: str):
    return {
        "products": [
            {"id": "1", "name": "Product 1", "price": 99.99},
            {"id": "2", "name": "Product 2", "price": 149.99}
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
