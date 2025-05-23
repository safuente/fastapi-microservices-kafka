# Variables
PROJECT_NAME=fastapi-microservices-kafka
COMPOSE=docker-compose
PY=python3

# Start development environment with hot reload
up:
	@echo "Starting development environment..."
	$(COMPOSE) up --build

# Stop and remove all containers, volumes, and networks
down:
	@echo "Stopping and cleaning up containers and volumes..."
	$(COMPOSE) down -v

# Stop containers without removing volumes
stop:
	$(COMPOSE) down

# Rebuild images without using cache
rebuild:
	$(COMPOSE) build --no-cache

# Send a test message to the Kafka producer
test-produce:
	curl -X POST http://localhost:8001/produce \
	     -H "Content-Type: application/json" \
	     -d '{"content": "Test message from Makefile"}'

# View logs for the consumer microservice
logs-b:
	$(COMPOSE) logs -f microservice-b

# View logs for the producer microservice
logs-a:
	$(COMPOSE) logs -f microservice-a

# Clean up unused Docker data
clean:
	docker system prune -f

# Open a shell in the producer container
sh-a:
	$(COMPOSE) exec microservice-a sh

# Open a shell in the consumer container
sh-b:
	$(COMPOSE) exec microservice-b sh

# Start production environment
up-prod:
	@echo "Starting production environment..."
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml up --build -d
