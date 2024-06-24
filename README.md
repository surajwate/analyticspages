# Analytics Pages

## Description
Analytics Pages is a Django-based web application designed to showcase data science projects. The application allows users to view, add, and manage projects, with features for user authentication and project details.

## Features
- User authentication (registration, login, logout)
- Add, update, and view data science projects
- Admin interface for managing projects
- Dockerized setup for development and deployment
- PostgreSQL database

## Prerequisites
- Python 3.9+
- Docker and Docker Compose

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/analyticspages.git
cd analyticspages
```

### 2. Create a Virtual Environment and Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create a `.env` file in the root directory and add the following:
```
SECRET_KEY=your-secret-key
DEBUG=1
ALLOWED_HOSTS=localhost,127.0.0.1
POSTGRES_DB=analyticspages
POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_db_password
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

### 4. Run the Application Locally
```bash
python manage.py migrate
python manage.py runserver
```

Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Docker Setup

### 1. Build and Start Docker Containers
```bash
docker-compose up --build -d
```

### 2. Apply Database Migrations
```bash
docker-compose exec web python manage.py migrate
```

### 3. Create a Superuser (Optional)
```bash
docker-compose exec web python manage.py createsuperuser
```

### 4. Access the Application
- Application: [http://localhost:8000](http://localhost:8000)
- Admin Panel: [http://localhost:8000/admin](http://localhost:8000/admin)

## Running Tests
```bash
pytest
```

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
