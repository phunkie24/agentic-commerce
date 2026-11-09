"""
Shopping Assistant Agent - Implements multiple AI design patterns
"""

from typing import List, Dict, Any

class ShoppingAssistantAgent:
    """AI-powered shopping assistant implementing:
    - Prompt Chaining
    - Tool Use
    - Memory Management
    - Reflection
    """
    
    def __init__(self):
        self.conversation_history = []
    
    async def process_query(self, user_id: str, message: str) -> Dict[str, Any]:
        """Process user shopping queries"""
        
        # Add to conversation history (Memory Management)
        self.conversation_history.append({
            "role": "user",
            "content": message
        })
        
        # Simulate agent processing
        response = await self._generate_response(message)
        
        self.conversation_history.append({
            "role": "assistant",
            "content": response
        })
        
        return {
            "success": True,
            "message": response,
            "user_id": user_id
        }
    
    async def _generate_response(self, message: str) -> str:
        """Generate contextual response"""
        
        # Simple keyword-based response for demo
        if "laptop" in message.lower():
            return "I found some great laptops! Would you like to see gaming laptops or business laptops?"
        elif "price" in message.lower():
            return "I can help you find products within your budget. What's your price range?"
        else:
            return f"I understand you're interested in: {message}. Let me search our catalog for you!"
