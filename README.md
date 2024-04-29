# Study App

Study App is a comprehensive application designed to enhance the learning experience for students. With features like hierarchical note-taking, a technical term glossary, and an event planner, Study App aims to organize and optimize your study sessions. Built with Django and leveraging vanilla HTML, CSS, and JS for the frontend, this application provides a robust platform for managing courses, domains, and entries; defining and accessing important technical terms; and planning events with timely email alerts.

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Django
- **Task Queue**: Celery
- **Message Broker**: Redis
- **Web Server**: Daphne
- **Database**: SQLite/Postgresql depending on the environment (development/production).

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8 or newer installed on your machine.
- A virtual environment manager like `virtualenv` or `pipenv`.
- A running instance of Redis for Celery to use. Instructions for installing Redis can be found [here](https://redis.io/download).
- A running instance of Postgresql for production. Instructions for installing Postgresql can be found [here](https://www.postgresql.org/download/).

## Setting Up

1. **Clone the repository**:
```
git clone https://github.com/nafdev01/study_system.git
```

2. **Navigate to your project directory**:
```
cd study_system
```
3. **Create and activate a virtual environment**:
```

python -m venv venv
source venv/bin/activate  # On Unix or MacOS
# venv\Scripts\activate  # On Windows
```

4. **Install the required packages**:
```
pip install -r requirements.txt
```

This command installs all necessary dependencies, including Django and Daphne, from the `requirements.txt` file.

5. **Configure the `.env` file** with your environment-specific settings. Use the `.env.example` file as a template.

#### OPTIONAL - If you are using Postgresql for production, update the `DATABASE_URL` in the `.env` file with your Postgresql connection string.

------
## PostgreSQL Setup
For the production environment, Study App uses PostgreSQL. Follow these steps to create a PostgreSQL user and database for the application:
1. **Log in to PostgreSQL**:
   First, log into the PostgreSQL command line interface:
```bash
sudo -u postgres psql
```
2. **Create User**:
   Create a user and set a password for it. Replace `study_user` with your desired username and `password` with a strong password:
```CREATE USER study_user WITH PASSWORD 'password';
```

3. **Create Database**:
   Create a database for your application and set the newly created user as the owner. Replace `study_db` with the name you wish to give to your database:
```bash
CREATE DATABASE study_db WITH OWNER study_user;
```
4. **Set Default Encoding, Transaction Isolation, and Timezone**:
   Ensure the database supports UTF-8 encoding, transactions are isolated correctly, and the timezone is set to UTC:
```bash
ALTER ROLE study_user SET client_encoding TO 'utf8';
ALTER ROLE study_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE study_user SET timezone TO 'UTC';
```

5. **Grant Permissions**:
   Grant all privileges on the database to your new user:
```bash
GRANT ALL PRIVILEGES ON DATABASE study_db TO study_user;
```

6. **Exit PostgreSQL**:
   Type `\q` and then press ENTER to quit psql.

Your PostgreSQL user and database are now configured and ready to be used with the Study App. Be sure to update your `.env` file with the database credentials:
```bash
DATABASE_URL="postgres://study_user:password@localhost/study_db"
```
6. **Run migrations**:
```
python manage.py migrate
```

7. **Create a superuser**:
```
python manage.py createsuperuser
```

8. **Start the Django development server**:
```
python manage.py runserver
```
## Starting Redis and Celery

To enable asynchronous task processing with Celery, follow these steps:

1. **Ensure Redis is Running**:

   Start the Redis server using the appropriate command for your installation. This is typically `redis-server`.

2. **Start Celery Worker**:

   Open a new terminal, navigate to your Django project directory, ensure the virtual environment is activated, and run:
    ```bash
    celery -A cert-study worker -l info
    ``` 
    
Now, your Study App is fully set up and capable of processing background tasks like email notifications efficiently, leveraging the power of Celery and Redis.

## Troubleshooting
Encountering issues while setting up the Study App? Here are some common problems and their solutions:
 - **Celery Worker Not Starting**: Ensure Redis is running and the Celery worker command is executed in the correct directory with the virtual environment activated.
 - **Database Connection Error**: Check your database credentials in the `.env` file and ensure the database server is running.
 - **Module Not Found**: If you encounter a `ModuleNotFoundError`, ensure all dependencies are installed in your virtual environment.
 - **Internal Server Error**: If you see an internal server error, set DEBUG=False in your .env file and check the Django console for any error messages and ensure all steps were followed correctly.
 - If you're still facing issues, please open an issue on GitHub with a detailed description of the problem, steps to reproduce it, and any relevant logs or error messages.
 
 ## Security Notice
 Security is paramount to the Study App project. We take it seriously and ask that you do the same. Here are a few guidelines:
- **Sensitive Information**: Never commit sensitive information to the repository. This includes passwords, API keys, and secret keys. Use environment variables and `.env` files to manage sensitive data.
- **Reporting Security Issues**: If you discover a security issue, please do not open a public issue. Instead, contact the project maintainers directly so we can address the vulnerability promptly and safely.

## Contribution Guidelines
We welcome contributions from everyone, whether it's bug fixes, new features, documentation improvements, or feedback. Please read our contribution guidelines for more information on how you can contribute to the Study App. By participating in this project, you're expected to uphold our community standards of respect, openness, and consideration. We're excited to see what you bring to the project!
