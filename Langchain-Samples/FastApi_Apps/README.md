# FastApi_Apps

This project demonstrates how to build a FastAPI application that exposes a Groq LLM (via Langchain) as an API using langserve for easy route management.

## Features

- **FastAPI**: Modern, fast web framework for building APIs.
- **Langchain & Groq**: Integrates Groq LLM models using Langchain for prompt-based responses.
- **langserve**: Simplifies exposing Langchain chains and models as API endpoints.
- **Streamlit Client**: A simple Streamlit app to interact with the API.

## Setup

1. **Clone the repository** and navigate to this folder.
2. **Python virtual Environments** (using uv or pip):
   ```bash
   cd FastApi_Apps
   uv init
   uv venv
   source .venv/bin/activate
   ```
   or
   ```bash
   cd FastApi_Apps
   python -v venv venv
   source .venv/bin/activate
   ```
3. **Install dependencies** (using uv or pip):
   ```bash
   uv add -r requirements.txt
   ```
   or
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**  
   Copy `.env` and fill in your `GROQ_API_KEY` and `LANGCHAIN_API_KEY`.

5. **Run the FastAPI server**:
   ```bash
   uvicorn app:app --reload
   ```
   The API will be available at `http://localhost:8000`.

6. **API Documentation**  
   Visit `http://localhost:8000/docs` for interactive Swagger UI.

## Endpoints

- **POST /groq_prompt/invoke**  
  Invoke the Groq LLM with a prompt.  
  Example request body:
  ```json
  {
    "input": {
      "topic": "What is quantum computing?"
    }
  }
  ```

## Streamlit Client

A simple client is provided in `streamlit_client.py` to interact with the API:

```bash
streamlit run streamlit_client.py
```

## File Structure

- `app.py` - Main FastAPI application exposing the Groq LLM API.
- `streamlit_client.py` - Streamlit client for testing the API.
- `requirements.txt` / `pyproject.toml` - Project dependencies.
- `.env` - Environment variables (API keys).

---

This project is a template for serving LLMs as APIs using FastAPI, Langchain, and langserve.
