# Distributed Task Scheduler App Challenge

## Overview
This challenge requires building an application having distributed task scheduler system in Python that manages and executes tasks across multiple worker nodes.

## Objective
Your goal is to create a central scheduler to receive task requests and distribute them to available worker nodes.

## Requirements
- **Python 3.8+**
- **FastAPI**
- **Streamlit**
- **Uvicorn** as the ASGI server for running FastAPI

## Getting Started

### Setup
1. Fork or clone this repository to begin working on your solution.
2. Install the required dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the FastAPI server by navigating to the project directory and running:
   ```bash
   uvicorn app.main:app --reload
   ```
4. Open a new terminal window and launch the Streamlit interface:
   ```bash
   streamlit run streamlit_app.py
   ```

### Project Structure
- `app/`: Contains the FastAPI application.
  - `main.py`: The entry point for the FastAPI app.
  - `submission.py`: Module responsible for handling the task distribution.
- `streamlit_app.py`: Script for the Streamlit frontend application.
- `requirements.txt`: Specifies project dependencies.

## Challenge Tasks
1. **FastAPI Backend**:
   - Implement an endpoint to receive different tasks.
   - Use a message queue system (e.g., RabbitMQ, Redis Pub/Sub) for communication between scheduler and workers.
   - Develop worker nodes that register with the scheduler on startup. Workers should execute tasks in parallel, report results, and handle task failures.
   - Implement mechanisms for handling worker failures (e.g., task reassignment, retries).
   - Ensure scheduler recovery from failures and maintain task consistency.
   - Include logging for task execution, worker status, and errors.
   - Design for scalability to handle a large number of tasks and dynamically scale worker nodes.
   - Provide clear documentation on system architecture, components, and deployment.
   - Include unit tests to validate critical components (scheduler, workers, communication).

2. **Streamlit Frontend**:
   - Develop a web-based dashboard for visualizing task progress and worker status.

3. **Integration**:
   - Ensure seamless communication and functionality between the Streamlit frontend and FastAPI backend.

4. **Bonus (Optional)**:
   - Support task dependencies and priority scheduling.
   - Develop a web-based dashboard for visualizing task progress and worker status.

## Submission

- Fork this repository and commit your implementation.
- Include a README.md.
- Overview of architecture and key components.
- Setup and deployment instructions.
- Explanation of design decisions and challenges faced.
- Potential improvements or additional features.

## Evaluation Criteria
- **Functionality**: The app must successfully distribute the tasks.
- **Code Quality**: Code should be clean, well-structured, and easy to maintain.
- **User Experience**: The Streamlit UI should be intuitive and straightforward for users.
- **Documentation**: Your code should be well-documented, and your README.md should clearly explain how to set up and run your application.