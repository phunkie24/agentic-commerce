# Agentic Commerce - Quick Start Guide

## Prerequisites

- Docker Desktop (with at least 16GB RAM allocated)
- OpenAI API key
- (Optional) Anthropic API key
- (Optional) Pinecone API key

## Installation Steps

### 1. Configure Environment

```bash
# Copy environment template
cp .env.example .env

# Edit with your API keys
nano .env  # or use your preferred editor
```

**Required variables:**
- `OPENAI_API_KEY` - Your OpenAI API key
- `DB_PASSWORD` - Choose a secure password
- `SECRET_KEY` - Generate with: `openssl rand -hex 32`
- `JWT_SECRET` - Generate with: `openssl rand -hex 32`

### 2. Start the Platform

```bash
# Use the startup script (recommended)
./start.sh

# Or manually with docker-compose
docker-compose up -d
```

### 3. Verify Installation

```bash
# Check all services are running
docker-compose ps

# Test the API
curl http://localhost:8000/health

# Test the frontend
curl http://localhost:3000/health
```

### 4. Access the Application

Open your browser and navigate to:
- **Frontend**: http://localhost:3000
- **API Documentation**: http://localhost:8000/docs
- **Grafana Dashboard**: http://localhost:3001 (admin/admin)
- **RabbitMQ Management**: http://localhost:15672 (guest/guest)

## Testing the Shopping Assistant

1. Go to http://localhost:3000
2. Type a message like: "I need a laptop for programming"
3. The AI assistant will respond with product suggestions

## Common Commands

```bash
# View logs from all services
docker-compose logs -f

# View logs from specific service
docker-compose logs -f api-gateway

# Restart a service
docker-compose restart api-gateway

# Stop all services
docker-compose down

# Stop and remove all data (⚠️  CAUTION)
docker-compose down -v
```

## Troubleshooting

### Services won't start
```bash
# Check Docker resources
docker system df

# Rebuild from scratch
docker-compose down -v
docker-compose build --no-cache
docker-compose up -d
```

### Can't connect to API
```bash
# Check if gateway is healthy
curl http://localhost:8000/health

# Check gateway logs
docker-compose logs api-gateway
```

### Frontend shows errors
```bash
# Rebuild frontend
docker-compose up -d --build frontend

# Check nginx logs
docker-compose logs frontend
```

## Development Tips

### Hot Reload
Backend services have hot reload enabled. Just edit the Python files and changes will reflect automatically.

### Add New Dependencies
```bash
# Add to backend/requirements.txt
echo "new-package==1.0.0" >> backend/requirements.txt

# Rebuild the service
docker-compose up -d --build api-gateway
```

### Database Access
```bash
# Connect to PostgreSQL
docker-compose exec postgres psql -U agenticcommerce

# Run SQL commands
SELECT * FROM products;
```

## Next Steps

1. Read the full architecture document
2. Explore the API at http://localhost:8000/docs
3. Customize agents in `backend/agents/`
4. Add new services in `backend/services/`
5. Modify frontend in `frontend/src/`

## Support

- Check `DEPLOYMENT_GUIDE.md` for detailed troubleshooting
- Review architecture document for design patterns
- Check logs with `docker-compose logs -f`

Happy hacking! 🚀
