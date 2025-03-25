# PedidosAPI

## Description
Pedidos API micro service for a DDD workshop

## Author
pliperkiller

## Requirements
- Python 3.8+
- pip

## Quick Start Guide

1. **Clone the repository**:
   ```sh
   $ git clone <repo-url>
   $ cd PedidosAPI
   ```

2. **Create a virtual environment**:
   ```sh
   $ python -m venv venv
   $ source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```sh
   $ pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Copy `.env.example` to `.env`
   - Update necessary configurations

5. **Run the application**:
   ```sh
   $ flask run
   ```

6. **Run tests**:
   ```sh
   $ pytest  # If using pytest
   $ python -m unittest discover  # If using unittest
   ```

## Installation

Clone the repository and create a virtual environment:
```sh
$ git clone <repo-url>
$ cd PedidosAPI
$ python -m venv venv
$ source venv/bin/activate  # On Windows use `venv\Scripts\activate`
$ pip install -r requirements.txt
```

## Configuration

Create a `.env` file based on `env.example` and adjust the necessary variables.

## Usage

Run the application:
```sh
$ flask run
```

If using Docker:
```sh
$ docker-compose up --build
```

## Project Structure

```sh
PedidosAPI/
│
├── src/                        # Source code
│   ├── domain/                 # Domain layer
│   ├── application/            # Application layer
│   ├── infrastructure/         # Infrastructure layer
│   └── app.py                  # Entry point
│
├── tests/                      # Tests
├── requirements.txt            # Dependencies
├── Dockerfile                  # Docker container
└── README.md                   # This file
```

## Testing

If you selected `pytest`:
```sh
$ pytest
```
If you selected `unittest`:
```sh
$ python -m unittest discover
```
