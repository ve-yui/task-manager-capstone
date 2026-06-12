**Task Manager Capstone**
Overview
This project is a simple task management application written in Python. Users can create, view, update, and manage tasks through a command-line interface.

The project demonstrates object-oriented programming principles, modular design, testing, version control, documentation generation, and containerization.

**Features**
Create tasks
View tasks
Update task status
Store task information
Unit testing with pytest

**Project Structure**
main.py - Application entry point
task.py - Task class definition
task_manager.py - Task management functionality
test_task_manager.py - Unit tests

**Installation**
Clone the repository:
git clone <repository-url>

Navigate to the project folder:
cd task-manager-capstone

Create and activate a virtual environment:
python -m venv venv

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Running the Application
python main.py

Running Tests
pytest

**Docker**
Build the Docker image:
docker build -t task-manager .

Run the container:
docker run task-manager

**Documentation**
Project documentation is generated using Sphinx and can be found in the docs folder.

