# Premium Todo-List Application

A simple, yet powerful Todo-List application built with Flask and deployed on Kubernetes using Helm.

## Features

*   Create, edit, and delete todos
*   Mark todos as done
*   Clean and intuitive user interface
*   Containerized with Docker
*   Ready for production deployment on Kubernetes with Helm

## Tech Stack

*   **Backend:** Flask
*   **Database:** PostgreSQL
*   **Containerization:** Docker
*   **Deployment:** Kubernetes, Helm
*   **Frontend:** HTML, CSS

## Prerequisites

*   Python 3.12+
*   Docker
*   Kubernetes cluster (e.g., Minikube, Kind, or a cloud provider's Kubernetes service)
*   Helm 3

## Installation and Running the Application

### Running Locally with Flask

1.  **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd todo-domain-deployment
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up the environment variables:**

    Create a `.env` file in the root of the project and add the following variables:

    ```
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    DB_HOST=localhost
    DB_PORT=5432
    DB_NAME=your_db_name
    FLASK_SECRET_KEY=a_strong_secret_key
    ```

5.  **Run the application:**

    ```bash
    flask run
    ```

    The application will be available at `http://127.0.0.1:5000`.

### Running with Docker

1.  **Build the Docker image:**

    ```bash
    docker build -t premium-todo:v0.1.0 .
    ```

2.  **Run the Docker container:**

    Make sure you have a running PostgreSQL instance and update the `.env` file with the correct database credentials.

    ```bash
    docker run -p 5000:5000 --env-file .env premium-todo:v0.1.0
    ```

    The application will be available at `http://127.0.0.1:5000`.

## Kubernetes Deployment

The application can be deployed to a Kubernetes cluster using the provided Helm chart.

1.  **Navigate to the chart directory:**

    ```bash
    cd chart
    ```

2.  **Install the Helm chart:**

    You can customize the deployment by modifying the `values.yaml` file or by using the `--set` flag.

    ```bash
    helm install my-release . --set image.tag=v0.1.0
    ```

    This will deploy the application to your Kubernetes cluster.

## Configuration

The following environment variables are used to configure the application:

| Variable           | Description                               | Default      |
| ------------------ | ----------------------------------------- | ------------ |
| `DB_USER`          | PostgreSQL database user                  |              |
| `DB_PASSWORD`      | PostgreSQL database password              |              |
| `DB_HOST`          | PostgreSQL database host                  |              |
| `DB_PORT`          | PostgreSQL database port                  |              |
| `DB_NAME`          | PostgreSQL database name                  |              |
| `FLASK_SECRET_KEY` | Secret key for Flask sessions             | `supersecretkey` |

## API Endpoints

The application provides the following endpoints:

| Method | Endpoint          | Description                                |
| ------ | ----------------- | ------------------------------------------ |
| `GET`  | `/`               | Displays the list of all todos.            |
| `GET`  | `/new`            | Displays the form to create a new todo.    |
| `POST` | `/new`            | Creates a new todo.                        |
| `GET`  | `/edit/<todo_id>` | Displays the form to edit a todo.          |
| `POST` | `/edit/<todo_id>` | Updates a todo.                            |
| `GET`  | `/toggle/<todo_id>` | Toggles the `done` status of a todo.       |
| `POST` | `/delete/<todo_id>` | Deletes a todo.                            |