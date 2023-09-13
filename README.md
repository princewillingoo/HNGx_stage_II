# HNGx_stage_II - REST API CRUD

## About

This repository contains the source code to illustrate a fundamental understanding of REST API principles and how to execute basic CRUD (Create, Read, Update, Delete) operations.

### Problem Statement

- Build a basic REST API for CRUD operations on a **person** resource.
- Interface the API with a database of your preference.
- Implement parameter handling for tasks like adding or retrieving a person by their identity.
- Create UML diagrams to document the system's design and database structure.
- Develop an automated testing script to validate each API function.
- Host the entire project on GitHub.
- Provide well-structured documentation in the repository.
- Include details on request/response formats, setup instructions, and API usage examples in the documentation.

## Built with

- Python
- FastAPI
- SQlite

## Getting Started

### Prerequisite

Make sure you have [Python3](https://www.python.org/downloads/) installed on your machine.

### Local Setup

Detailed instructions for setting up the project on a local development environment.

1. Run `git clone <repo link>` to clone this repo

2. Creat and activate a virtual environment

   [Setup virtual environment on Windows or Linux](https://docs.python.org/3/library/venv.html#module-venv)

   ```bash
   python -m venv env
   source env/bin/activate # Linux
   env\Scripts\activate.bat # Windows
   ```

3. Install project dependencies

    ```bash
    pip install -r requirements.txt
    ```

4. Database Setup

    Upon statring your local server. The application takes care of setting up a database with a filename `lite.db` for you.

    SQlite does not require complex setup process which makes it suitable for a project of the nature.

5. Start local server

   ```bash
    uvicorn app.main:app --host "0.0.0.0" --port 80
    ```

6. Navigate to <http://localhost:80/>
_**Viola !!**_ :smile:

## Live Demo

<https://hngx-task-two-zjqf.onrender.com>

## Resources

For a more extensive crud api checkout, <https://github.com/princewilling/fastapi-crud-api>.

# Thank You
