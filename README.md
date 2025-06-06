# 🏡 API de Simulação de Financiamento Imobiliário

[](https://www.python.org/)
[](https://fastapi.tiangolo.com/)
[](https://opensource.org/licenses/MIT)

This API is designed to simulate real estate financing, calculating key values like down payment, financed amount, total savings required, and estimated monthly installments. Built with **Python** and **FastAPI**, it focuses on a clear, modular architecture and automatic documentation.

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

-----

## ⚙️ Setup and Local Execution

Follow these steps to get the API up and running on your local machine.

### 1\. Prerequisites

Make sure you have the following installed:

  * [**Python 3.9+**](https://www.python.org/downloads/)
  * [**Git**](https://git-scm.com/downloads)

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

### 6\. Run the API

To start the API server locally:

```bash
uvicorn app.main:app --reload
```

  * The API will be available at: `http://127.0.0.1:8000`
  * Access the **interactive documentation (Swagger UI)** at: `http://127.00.0.1:8000/docs`
  * View the ReDoc documentation at: `http://127.0.0.1:8000/redoc`

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

## 👨‍💻 Code Maintenance Guidelines

To ensure the long-term quality, readability, and consistency of this codebase, please adhere to the following guidelines when contributing:

  * **Modular Architecture:** Always maintain the established modular structure with clear separation of concerns (e.g., `schemas`, `services`, `routers`). Each module should have a single, well-defined responsibility.
  * **Clear Code:** Write clean, concise, and self-documenting code. Prefer simple solutions over complex ones.
  * **Docstrings:** Provide comprehensive docstrings for all functions, classes, and methods, explaining their purpose, arguments, and return values. This is crucial for understanding the codebase.
  * **Naming Conventions:** Follow Python's [PEP 8](https://peps.python.org/pep-0008/) naming conventions (e.g., `snake_case` for functions and variables, `PascalCase` for classes).
  * **Error Handling:** Implement robust error handling mechanisms, ensuring that unexpected situations are gracefully managed and provide informative responses.
  * **Version Control & Git Flow:**
      * Utilize **Git** for all code changes.
      * Follow a **Git Flow** or a similar branching strategy (e.g., Feature Branch Workflow) to manage development. All new features or bug fixes should be developed in dedicated branches (e.g., `feature/nome-da-feature`, `bugfix/descricao-do-bug`) originating from `main` (or `develop`).
      * Ensure **small, atomic commits** with clear and descriptive commit messages that explain *what* was changed and *why*.
      * **Recommendation: Use Gitmojis\!** Consider incorporating [Gitmojis](https://gitmoji.dev/) into your commit messages. They provide a visual and standardized way to categorize the type and intent of each commit, making the commit history more readable and scannable. For example: `✨ feat: add new simulation endpoint` or `🐛 fix: correct calculation bug`.
      * **Rebase** your feature branches frequently with the main branch to avoid large merge conflicts.
      * Use **Pull Requests (PRs)** for all merges into `main` (or `develop`). PRs should include a clear description of the changes and link to any relevant issues. Code reviews are encouraged before merging.

-----

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](https://www.google.com/search?q=LICENSE) file for more details.