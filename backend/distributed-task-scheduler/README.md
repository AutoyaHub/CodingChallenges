# 🔄 Distributed Task Scheduler Challenge

[![Difficulty](https://img.shields.io/badge/Difficulty-⭐⭐⭐⭐⭐-red.svg)]()
[![Category](https://img.shields.io/badge/Category-Backend-blue.svg)]()
[![Duration](https://img.shields.io/badge/Duration-8--12%20hours-orange.svg)]()
[![Skills](https://img.shields.io/badge/Skills-Distributed%20Systems%20|%20FastAPI%20|%20Message%20Queues-purple.svg)]()

## 🎯 Overview

Build a production-ready distributed task scheduling system that manages and executes tasks across multiple worker nodes. This challenge tests your understanding of distributed systems, message queues, fault tolerance, and scalable architecture design.

## 🏗️ System Architecture

```mermaid
graph TB
    subgraph "Frontend Layer"
        ST[Streamlit Dashboard]
    end
    
    subgraph "API Layer"
        API[FastAPI Scheduler]
    end
    
    subgraph "Message Queue"
        MQ[Redis/RabbitMQ]
    end
    
    subgraph "Worker Nodes"
        W1[Worker 1]
        W2[Worker 2]
        W3[Worker N]
    end
    
    subgraph "Storage"
        DB[(Database)]
        LOGS[Log Storage]
    end
    
    ST --> API
    API --> MQ
    API --> DB
    MQ --> W1
    MQ --> W2
    MQ --> W3
    W1 --> DB
    W2 --> DB
    W3 --> DB
    W1 --> LOGS
    W2 --> LOGS
    W3 --> LOGS
```

## 🎯 Requirements

### Core Functionality
- [ ] **Task Distribution**: Central scheduler receives and distributes tasks
- [ ] **Worker Management**: Dynamic worker registration and health monitoring
- [ ] **Message Queue**: Reliable task communication using Redis/RabbitMQ
- [ ] **Parallel Execution**: Workers execute tasks concurrently
- [ ] **Result Reporting**: Workers report task completion and results
- [ ] **Fault Tolerance**: Handle worker failures and task reassignment
- [ ] **Scheduler Recovery**: System recovery from scheduler failures
- [ ] **Task Persistence**: Maintain task consistency across failures

### Technical Requirements
- [ ] **FastAPI Backend**: RESTful API with async support
- [ ] **Streamlit Frontend**: Real-time dashboard for monitoring
- [ ] **Message Queue**: Redis Pub/Sub or RabbitMQ integration
- [ ] **Logging**: Comprehensive logging for debugging and monitoring
- [ ] **Testing**: Unit tests for critical components
- [ ] **Documentation**: Architecture overview and setup instructions
- [ ] **Scalability**: Handle large task volumes and dynamic scaling

### Bonus Features (Optional)
- [ ] **Task Dependencies**: Support for task dependency graphs
- [ ] **Priority Scheduling**: Priority-based task execution
- [ ] **Load Balancing**: Intelligent task distribution
- [ ] **Metrics & Monitoring**: Performance metrics and alerting
- [ ] **Web Dashboard**: Enhanced UI beyond basic Streamlit

## 📋 API Specification

### Task Management Endpoints

#### Submit Task
```http
POST /api/tasks
Content-Type: application/json

{
    "task_id": "unique-task-id",
    "task_type": "processing",
    "payload": {
        "data": "task-specific-data",
        "parameters": {}
    },
    "priority": 1,
    "dependencies": [],
    "timeout": 300
}
```

#### Get Task Status
```http
GET /api/tasks/{task_id}

Response:
{
    "task_id": "unique-task-id",
    "status": "pending|running|completed|failed",
    "worker_id": "worker-123",
    "created_at": "2024-01-01T00:00:00Z",
    "started_at": "2024-01-01T00:01:00Z",
    "completed_at": "2024-01-01T00:05:00Z",
    "result": {},
    "error": null
}
```

#### List Tasks
```http
GET /api/tasks?status=pending&limit=10&offset=0
```

### Worker Management Endpoints

#### Register Worker
```http
POST /api/workers/register
Content-Type: application/json

{
    "worker_id": "worker-123",
    "capabilities": ["processing", "analysis"],
    "max_concurrent_tasks": 5
}
```

#### Worker Heartbeat
```http
POST /api/workers/{worker_id}/heartbeat
Content-Type: application/json

{
    "status": "active",
    "current_tasks": ["task-1", "task-2"],
    "system_info": {
        "cpu_usage": 45.2,
        "memory_usage": 67.8,
        "disk_usage": 23.1
    }
}
```

#### List Workers
```http
GET /api/workers
```

## 🏗️ Project Structure

```
backend/distributed-task-scheduler/
├── README.md                   # This file
├── requirements.txt            # Python dependencies
├── docker-compose.yml          # Multi-service setup
├── .env.example               # Environment variables template
├── app/
│   ├── __init__.py
│   ├── main.py                # FastAPI application entry point
│   ├── config.py              # Configuration settings
│   ├── models/
│   │   ├── __init__.py
│   │   ├── task.py            # Task data models
│   │   └── worker.py          # Worker data models
│   ├── api/
│   │   ├── __init__.py
│   │   ├── tasks.py           # Task API endpoints
│   │   └── workers.py         # Worker API endpoints
│   ├── services/
│   │   ├── __init__.py
│   │   ├── scheduler.py       # Task scheduling logic
│   │   ├── message_queue.py   # Message queue interface
│   │   └── worker_manager.py  # Worker lifecycle management
│   ├── database/
│   │   ├── __init__.py
│   │   ├── connection.py      # Database connection
│   │   └── repositories.py    # Data access layer
│   └── utils/
│       ├── __init__.py
│       ├── logging_config.py  # Logging configuration
│       └── monitoring.py      # Health checks and metrics
├── worker/
│   ├── __init__.py
│   ├── worker_node.py         # Worker implementation
│   ├── task_executor.py       # Task execution engine
│   └── health_monitor.py      # Worker health monitoring
├── streamlit_app.py           # Frontend dashboard
├── tests/
│   ├── __init__.py
│   ├── test_scheduler.py      # Scheduler tests
│   ├── test_worker.py         # Worker tests
│   ├── test_api.py            # API endpoint tests
│   └── integration/
│       ├── __init__.py
│       └── test_e2e.py        # End-to-end tests
└── docs/
    ├── architecture.md        # System architecture
    ├── deployment.md          # Deployment guide
    └── api_reference.md       # API documentation
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Redis or RabbitMQ
- PostgreSQL (optional, can use SQLite for development)
- Docker & Docker Compose (recommended)

### Quick Start with Docker

1. **Clone and Setup**
```bash
git clone <repository-url>
cd backend/distributed-task-scheduler
cp .env.example .env
```

2. **Start Services**
```bash
docker-compose up -d redis postgres
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Start the Scheduler**
```bash
uvicorn app.main:app --reload --port 8000
```

5. **Start Workers**
```bash
# Terminal 1
python worker/worker_node.py --worker-id worker-1

# Terminal 2
python worker/worker_node.py --worker-id worker-2
```

6. **Start Dashboard**
```bash
streamlit run streamlit_app.py
```

### Manual Setup

<details>
<summary>Click to expand manual setup instructions</summary>

1. **Install Redis**
```bash
# Ubuntu/Debian
sudo apt-get install redis-server

# macOS
brew install redis
```

2. **Start Redis**
```bash
redis-server
```

3. **Follow steps 3-6 from Quick Start**

</details>

## 🧪 Testing

### Running Tests
```bash
# Unit tests
pytest tests/ -v

# Integration tests
pytest tests/integration/ -v

# Coverage report
pytest tests/ --cov=app --cov-report=html
```

### Test Scenarios
- [ ] **Task Submission**: Verify task creation and queuing
- [ ] **Worker Registration**: Test worker lifecycle management
- [ ] **Task Execution**: Ensure tasks are properly executed
- [ ] **Failure Recovery**: Test worker and scheduler failure scenarios
- [ ] **Concurrency**: Verify parallel task execution
- [ ] **Load Testing**: Performance under high task volumes

## 📊 Monitoring & Observability

### Streamlit Dashboard Features
- **Real-time Task Queue**: Live view of pending, running, and completed tasks
- **Worker Status**: Active workers, health, and resource utilization
- **System Metrics**: Throughput, latency, error rates
- **Task History**: Completed tasks with execution times and results
- **System Health**: Overall system status and alerts

### Logging
- **Structured Logging**: JSON-formatted logs for easy parsing
- **Log Levels**: DEBUG, INFO, WARNING, ERROR, CRITICAL
- **Correlation IDs**: Track requests across services
- **Performance Metrics**: Response times and resource usage

## 🔧 Configuration

### Environment Variables
```bash
# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=false

# Database
DATABASE_URL=postgresql://user:pass@localhost/taskdb

# Message Queue
REDIS_URL=redis://localhost:6379/0
RABBITMQ_URL=amqp://user:pass@localhost:5672/

# Worker Configuration
MAX_WORKERS=10
TASK_TIMEOUT=300
HEARTBEAT_INTERVAL=30

# Monitoring
LOG_LEVEL=INFO
METRICS_ENABLED=true
```

## 🏆 Evaluation Criteria

| Criterion | Weight | Description |
|-----------|---------|-------------|
| **Architecture** | 25% | System design, component separation, scalability |
| **Fault Tolerance** | 20% | Error handling, recovery mechanisms, reliability |
| **Code Quality** | 20% | Clean code, maintainability, best practices |
| **Performance** | 15% | Efficiency, concurrency, resource usage |
| **Testing** | 10% | Test coverage, test quality, integration tests |
| **Documentation** | 10% | README quality, code comments, API docs |

## 💡 Implementation Tips

### Task Scheduling
- Use priority queues for task ordering
- Implement task dependencies with directed acyclic graphs (DAG)
- Consider task retry policies and exponential backoff

### Worker Management
- Implement heartbeat mechanism for health monitoring
- Handle graceful worker shutdown and task reassignment
- Use connection pooling for database access

### Message Queue
- Choose between Redis Pub/Sub vs RabbitMQ based on requirements
- Implement message acknowledgment for reliability
- Consider message persistence for critical tasks

### Monitoring
- Implement circuit breakers for external dependencies
- Use async operations for better performance
- Monitor queue depth and processing rates

## 🔗 Advanced Features

### Task Dependencies
```python
# Example: Task B depends on Task A completion
{
    "task_id": "task-b",
    "dependencies": ["task-a"],
    "task_type": "analysis",
    "payload": {"input": "result_from_task_a"}
}
```

### Priority Scheduling
```python
# Higher priority tasks execute first
{
    "task_id": "urgent-task",
    "priority": 10,  # 1-10 scale
    "task_type": "critical_analysis"
}
```

## 📚 Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Redis Documentation](https://redis.io/documentation)
- [RabbitMQ Tutorial](https://www.rabbitmq.com/tutorials/tutorial-one-python.html)
- [Distributed Systems Patterns](https://microservices.io/patterns/)

---

<div align="center">
  <strong>Build scalable, fault-tolerant systems! 🚀</strong><br>
  <em>Design for failure, scale for success.</em>
</div>