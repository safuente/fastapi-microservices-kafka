
# FastAPI Kafka Microservices

This project demonstrates a microservices setup using **FastAPI** and **Kafka**, containerized with **Docker Compose**.

## Services

- **microservice-a**: Kafka producer (FastAPI)
- **microservice-b**: Kafka consumer (FastAPI)
- **Kafka + Zookeeper**: Messaging backend

## Requirements

- Docker
- Docker Compose
- Make (optional)

## Usage

### Development Mode

Runs with hot reload and mounted volumes:

```bash
make up
```

### Production Mode

Runs without hot reload or mounted volumes:

```bash
make up-prod
```

## Docker Compose Files

### `docker-compose.yml`

Base services configuration, including Kafka, Zookeeper, and both FastAPI microservices.

### `docker-compose.prod.yml`

Overrides for production: no volume mounts, no `--reload`, clean and optimized for deployment.

## Makefile Commands

```bash
make up          # Start dev environment
make up-prod     # Start production environment
make test-produce  # Send a test message to the producer
make logs-a      # View producer logs
make logs-b      # View consumer logs
make down        # Stop and remove containers/volumes
make clean       # Prune unused Docker resources
```

