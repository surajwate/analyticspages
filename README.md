# Analytics Pages

## Description

Analytics Pages is a Django-based web application designed to showcase data science projects. The application allows users to view, add, and manage projects, with features for user authentication and project details.

## Features

- User authentication (registration, login, logout)
- Add, update, and view data science projects
- Responsive design with Bootstrap
- Integration with PostgreSQL using Docker
- Continuous integration with GitHub Actions

## Prerequisites

- Python 3.9+
- Docker
- Docker Compose

## Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/yourusername/analyticspages.git
    cd analyticspages
    ```

2. **Create a `.env` File**:

    Create a `.env` file in the root directory with the following contents:

    ```plaintext
    SECRET_KEY=your-secret-key
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1
    POSTGRES_DB=yourdbname
    POSTGRES_USER=yourusername
    POSTGRES_PASSWORD=yourpassword
    DATABASE_URL=postgres://yourusername:yourpassword@db:5432/yourdbname
    ```

3. **Create and Activate Virtual Environment (if not using Docker)**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Project with Docker

1. **Build and Run Containers**:

    ```bash
    docker-compose up --build
    ```

2. **Apply Migrations**:

    ```bash
    docker-compose exec web python manage.py migrate
    ```

3. **Create a Superuser**:

    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```

4. **Access the Application**:

    Open your web browser and navigate to `http://localhost:8000`.

## Running Tests

1. **Run Tests with Docker**:

    ```bash
    docker-compose exec web pytest
    ```

2. **Run Tests Locally**:

    ```bash
    pytest
    ```

## Continuous Integration

We use GitHub Actions for continuous integration. The CI pipeline runs tests and checks for code quality on every push and pull request. The configuration is defined in the `.github/workflows/ci.yml` file.

## Community and Support

- **GitHub Discussions**: Join the conversation in our [Discussions](https://github.com/surajwate/analyticspages/discussions) section.
- **Wiki**: Check out our [Wiki](https://github.com/surajwate/analyticspages/wiki) for detailed documentation and guides.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add new feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Open a pull request

---

Feel free to suggest improvements or contribute to the project!
