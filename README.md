# PyStock

A lightweight command-line inventory management application writte in Python.

Pystock provides a simple interactive interface for managing products directly from the terminal. It is designed as a small, straightforward inventory system without external runtime dependencies

> **Status**: PyStock is currently under development. The interface and features may change before the first stable release.

## Features

- Add products to your inventory
- Update existing products
- Delete products
- Search for products using multiple identifiers
- Manage inventory through an interactive command-line interface
- Lightweight installation with no external runtime dependencies

## Requirements

- Python 3.14 or newer

## Installation

Clone the repository:

```bash
git clone https://github.com/oviwanazul124/PyStock.git
cd PyStock
```

Install the project

```bash
python -m pip install .
```

For local development, you can install it in editable mode:

```bash
python -m pip install -e
```

## Usage

PyStock provides an interactive menu for managing your inventory.

From the menu, you can perform operations such as:

- Adding a product
- Modifying a product
- Deleting a product
- Searching for products

## Project Structure

```
PyStock/
├── .github/
│   └── workflows/
├── src/
│   └── pystock/
├── tests/
├── pyproject.toml
└── README.md
```
The application source code lives under `src/pystock`, while automated test are kept under `tests`.
