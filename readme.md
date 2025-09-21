# FastAPI Boilerplate

This is a simple boilerplate for a FastAPI application, designed to help you quickly start building APIs with FastAPI.

## Features

- FastAPI setup with common configurations
- Example route with rate limiting using `slowapi`
- Easy to extend with additional routes, middleware, and services
- Basic project structure to keep your code organized

## Requirements

- Python 3.7+
- Install dependencies using `pip` or `pipenv`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sauciucrazvan/fastapi-boilerplate.git
   cd fastapi-boilerplate
   ```
2. Set up a virtual environment (optional but recommended):

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To run the app, use the following command:

    ```bash
    uvicorn main:app --reload
    ```

The app will be accessible at `http://localhost:8000`. You can view the interactive API documentation at `http://localhost:8000/docs`.

# Project Structure

    ```
    fastapi-boilerplate/
    │
    ├── api/ # API routes and logic
    │ ├── routes/ # All route definitions
    │ ├── app.py # Main FastAPI app
    │
    ├── main.py # Entry point for running the app
    ├── requirements.txt # Project dependencies
    └── README.md # This file
    ```
