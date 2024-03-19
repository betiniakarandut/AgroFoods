# Agro Foods

## Description

This project is an agro foods grocery store. It gives the client the flexibility to Manage and Order his agro products and services.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [GitHub Workflows](#github-workflows)
4. [Linting](#linting)
5. [Contributing](#contributing)
6. [License](#license)

## Installation

To install and set up the project locally, follow these steps:

```bash
# Clone the repository
git clone https://github.com/betiniakarandut/AgroFoods.git

# Navigate to the project directory
cd AgroFoods

# Install dependencies
pip install -r requirements.txt
```

## Usage

To use the project, follow these instructions:

```bash
# Run the application
python app.py

# Access the application in your web browser at http://localhost:5000
```

## GitHub Workflows

This project utilizes GitHub workflows for automation. The following workflows are included:

- **Continuous Integration (CI)**: This workflow runs on every push to the `development` branch and checks code quality, runs tests, and ensures compatibility.
- **Deployment**: This workflow triggers on pushes to the `main` branch and handles deployment to our production environment.

## DATABASE CONNECTION CREDENTIALS
MySQL DB connection

- **host='localhost',**
- **password='@Betini2024',**
- **user='root',**
- **database='agrofoods'**

## Linting

Linting ensures code quality and consistency. The project uses the following linting tools:

- **mypy**: Static type checker for Python code.
- **flake8**: Python style guide checker.
- **eslint**: JavaScript linting tool.
- **stylelint**: CSS and SCSS linting tool.

## Contributing

Contributions to this project are welcome! To contribute, please follow these steps:

1. Fork the repository and create a new branch from `development`.
2. Make your changes and ensure they follow our coding standards and conventions.
3. Test your changes thoroughly.
4. Submit a pull request detailing the changes you've made and any relevant information.

## License

This project is licensed under the [MIT License](LICENSE).
