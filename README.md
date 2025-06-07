# 🏡 API de Simulação de Financiamento Imobiliário

[](https://www.python.org/)
[](https://fastapi.tiangolo.com/)
[](https://opensource.org/licenses/MIT)

This API is designed to simulate real estate financing, calculating key values like down payment, financed amount, total savings required, and estimated monthly installments. Built with **Python** and **FastAPI**, it focuses on a clear, modular architecture and automatic documentation.

-----

## 📚 Table of Contents

## 📚 Table of Contents

* [🚀 Key Features](#key-features)
* [🛠️ Technologies Used](#technologies-used)
* [⚙️ Setup and Local Execution](#setup-and-local-execution)
* [🐳 Docker Deployment](#docker-deployment)
* [📝 API Documentation and Usage](#api-documentation-and-usage)
* [✅ Tests](#tests)
* [👨‍💻 Code Maintenance Guidelines](#code-maintenance-guidelines)
* [📄 License](#license)

-----

## 🚀 Key Features

The API provides a single, powerful endpoint for loan simulation:

  * **`POST /simulacao`**: Calculates the details of a real estate financing based on input parameters.

-----

## 🛠️ Technologies Used

  * **Backend:** [Python 3.9+](https://www.python.org/) with [FastAPI](https://fastapi.tiangolo.com/)
  * **Web Server:** [Uvicorn](https://www.uvicorn.org/) (ASGI Server)
  * **Data Validation:** [Pydantic](https://pydantic.dev/)
  * **Dependency Management:** [Pip](https://pip.pypa.io/en/stable/) and [Venv](https://docs.python.org/3/library/venv.html)
  * **Containerization:** [Docker](https://www.docker.com/)

-----

## ⚙️ Setup and Local Execution

Follow these steps to get the API up and running on your local machine.

### 1\. Prerequisites

Make sure you have the following installed:

  * [**Python 3.9+**](https://www.python.org/downloads/)
  * [**Git**](https://git-scm.com/downloads)
  * [**Docker Desktop**](https://www.docker.com/products/docker-desktop) (for Windows/macOS) or [**Docker Engine**](https://docs.docker.com/engine/install/) (for Linux)

### 2\. Clone the Repository

Start by cloning the project to your local directory:

```bash
git clone https://github.com/seu-usuario/simulador-compra-imovel.git # Update with your repository link
cd simulador-compra-imovel
```

### 3\. Set Up Virtual Environment (`venv`)

Using a virtual environment is best practice for isolating project dependencies.

```bash
# From the project root (simulador-compra-imovel/)
python -m venv venv
```

### 4\. Activate Virtual Environment

Activate your `venv` to ensure you're using the correct Python environment:

  * **Linux/macOS (Bash/Zsh):**

    ```bash
    source venv/bin/activate
    ```

  * **Windows (PowerShell):**

    ```powershell
    .\venv\Scripts\Activate
    ```

  * **Windows (Command Prompt - CMD):**

    ```cmd
    .\venv\Scripts\activate.bat
    ```

    **Note:** The activation command might vary slightly depending on your shell (e.g., `fish` shell users might need `source venv/bin/activate.fish`). You'll know it's active when you see `(venv)` in your terminal prompt.

### 5\. Install Dependencies

With your virtual environment active, install all required packages:

```bash
pip install -r requirements.txt
```

### 6\. Run the API (Local Python Environment)

To start the API server locally using your Python environment:

```bash
uvicorn app.main:app --reload
```

  * The API will be available at: `http://127.0.0.1:8000`
  * Access the **interactive documentation (Swagger UI)** at: `http://127.0.0.1:8000/docs`
  * View the ReDoc documentation at: `http://127.0.0.1:8000/redoc`

-----

## 🐳 Docker Deployment

For consistent and isolated execution across different environments, this project supports Docker. Docker bundles the application and all its dependencies into a single, portable unit.

### 1\. Build the Docker Image

Navigate to the project root directory (where `Dockerfile` is located) and build the image:

```bash
docker build -t simulacao-api .
```

  * `-t simulacao-api`: Assigns a name (tag) to your image.
  * `.`: Specifies the current directory as the build context, telling Docker where to find the `Dockerfile` and other project files.

### 2\. Run the Docker Container (API)

After building the image, you can create and start a container from it. The `-p` flag maps the container's internal port to a port on your host machine, making the API accessible.

```bash
docker run -p 8000:8000 --name simulacao-api-container simulacao-api
```

  * `-p 8000:8000`: Maps port `8000` on your host machine to port `8000` inside the container.
  * `--name simulacao-api-container`: Assigns a memorable name to your container.
  * `simulacao-api`: The name of the Docker image you just built.

The container will run in the foreground, displaying application logs. To run it in the background, add the `-d` flag:

```bash
docker run -d -p 8000:8000 --name simulacao-api-container simulacao-api
```

### 3\. Access the API (Docker)

Once the container is running:

  * **API Principal:** `http://localhost:8000/` or `http://127.0.0.1:8000/`
  * **Interactive Documentation (Swagger UI):** `http://localhost:8000/docs`
  * **ReDoc Documentation:** `http://localhost:8000/redoc`

### 4\. Stop and Remove the Docker Container

To stop a running container:

```bash
docker stop simulacao-api-container
```

To remove a stopped container (freeing up resources):

```bash
docker rm simulacao-api-container
```

### 5\. Run Tests with Docker (Optional: Requires `docker-compose.yml` for simplified setup)

If you have a `docker-compose.yml` configured (as provided in previous discussions, with a `tests` service), you can run your tests inside a Docker container. This ensures your tests run in an isolated environment identical to your API's.

```bash
# From the project root where docker-compose.yml is located
docker compose run --rm tests
```

-----

## 📝 API Documentation and Usage

This API is **self-documenting** through the **OpenAPI (Swagger)** standard, providing a fully interactive interface to explore and test its endpoints. You can access it directly at `http://127.0.0.1:8000/docs` or `http://127.0.0.1:8000/redoc` when the API is running.

The API simulates real estate financing via a **`POST`** request to the `/simulacao` endpoint. This endpoint calculates essential financing details, including the down payment amount, the financed amount, the total savings required, and the estimated monthly installment. Input data validation is automatically handled, ensuring parameters are within expected ranges and types.

**Request Parameters (JSON Body):**

  * `valor_imovel` (float): The total value of the property. Must be a positive number.
  * `percentual_entrada` (float): The percentage of the property's value to be used as a down payment. Must be between 5 and 20 (inclusive).
  * `anos_contrato` (int): The number of years for the financing contract. Must be between 1 and 5 (inclusive).

**Responses:**

  * **`200 OK`**: Returns a JSON object containing the calculated financing details.
    **Example Response:**

    ```json
    {
      "valor_entrada": 20000.00,
      "valor_financiado": 380000.00,
      "total_a_guardar": 60000.00,
      "parcela_mensal": 1666.67
    }
    ```

  * **`422 Unprocessable Entity`**: Occurs if input parameters fail validation (e.g., `percentual_entrada` out of range, missing required field, incorrect data type). The JSON response body will contain detailed validation error messages.

  * **`500 Internal Server Error`**: Occurs if an unexpected error happens during the simulation processing on the server. This might indicate an issue with the calculation logic or infrastructure.

**Calculation Notes:**

  * `valor_entrada` = `valor_imovel` \* (`percentual_entrada` / 100)
  * `valor_financiado` = `valor_imovel` - `valor_entrada`
  * `total_a_guardar` = `valor_imovel` \* 0.15 (15% of the property value)
  * `parcela_mensal` = `total_a_guardar` / (`anos_contrato` \* 12)

-----

### Usage Example with cURL

You can test this endpoint using cURL in your terminal:

```bash
curl -X POST \
  http://127.0.0.1:8000/simulacao \
  -H 'Content-Type: application/json' \
  -d '{
    "valor_imovel": 400000,
    "percentual_entrada": 5,
    "anos_contrato": 3
  }'
```

-----

## ✅ Tests

This project includes **unit and integration tests** to ensure the robustness and correctness of its functionalities. We use **`pytest`** as our testing framework.

### How to Run Tests

1.  **Activate your virtual environment.**
2.  From the project root directory, execute:
    ```bash
    pytest
    ```
    This command will automatically discover and run all tests within the `tests/` directory (including unit and integration tests).

### Types of Tests

  * **Unit Tests (`tests/unit/`)**: Focus on validating small, isolated units of code. In this project, they verify:
      * The correct validation and structure of **Pydantic models** (`schemas`).
      * The accuracy of **calculations and business rules** within the service layer (`services`).
  * **Integration Tests (`tests/integration/`)**: Verify the interaction between different API components by simulating HTTP requests. They ensure that:
      * API endpoints respond correctly to various request types.
      * The integration between the router, services, and data models works as expected.

-----

## 👨‍💻 Code Maintenance Guidelines

To ensure the long-term quality, readability, and consistency of this codebase, please adhere to the following guidelines when contributing:

  * **Modular Architecture:** Always maintain the established modular structure with clear separation of concerns (e.g., `schemas`, `services`, `routers`). Each module should have a single, well-defined responsibility.

  * **Clear Code:** Write clean, concise, and self-documenting code. Prefer simple solutions over complex ones.

  * **Docstrings:** Provide comprehensive docstrings for all functions, classes, and methods, explaining their purpose, arguments, and return values. This is crucial for understanding the codebase.

  * **Naming Conventions:** Follow Python's [PEP 8](https://peps.python.org/pep-0008/) naming conventions (e.g., `snake_case` for functions and variables, `PascalCase` for classes).

  * **Error Handling:** Implement robust error handling mechanisms, ensuring that unexpected situations are gracefully managed and provide informative responses.

  * **Code Linting & Formatting:**

      * We use automatic code formatters and linters to maintain consistent style and catch potential issues early.
      * **Black** (code formatter): Ensures consistent code formatting automatically.
      * **isort** (import sorter): Organizes and sorts imports automatically.
      * **Flake8** (linter): Checks for style inconsistencies (PEP 8) and common programming errors.
      * **How to Run:** Ensure you have these tools installed in your virtual environment (`pip install flake8 black isort`). You can run them manually from the project root:
        ```bash
        black app/
        isort app/
        flake8 app/
        ```
      * **Pre-commit Hooks:** It's highly recommended to set up `pre-commit` hooks (`pip install pre-commit` then `pre-commit install`) to automatically run these checks before every `git commit`, preventing inconsistent code from entering the repository.

  * **Version Control & Git Flow:**

      * Utilize **Git** for all code changes.
      * Follow a **Git Flow** or a similar branching strategy (e.g., Feature Branch Workflow) to manage development. All new features or bug fixes should be developed in dedicated branches (e.g., `feature/nome-da-feature`, `bugfix/descricao-do-bug`) originating from `main` (or `develop`).
      * Ensure **small, atomic commits** with clear and descriptive commit messages that explain *what* was changed and *why*.
      * **Recommendation: Use Gitmojis\!** Consider incorporating [Gitmojis](https://gitmoji.dev/) into your commit messages. They provide a visual and standardized way to categorize the type and intent of each commit, making the commit history more readable and scannable. For example: `✨ feat: add new simulation endpoint` or `🐛 fix: correct calculation bug`.
      * **Rebase** your feature branches frequently with the main branch to avoid large merge conflicts.
      * Use **Pull Requests (PRs)** for all merges into `main` (or `develop`). PRs should include a clear description of the changes and link to any relevant issues. Code reviews are encouraged before merging.

-----

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/licenses/MIT) file for more details.