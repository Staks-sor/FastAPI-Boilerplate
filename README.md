<<<<<<< HEAD

# FastAPI Boilerplate

A dockerized FastAPI Boilerplate with JWT, Loguru logging middleware, Role based authorization, SQLAlchemy ORM with AsyncSession.

Some endpoints are added as demo purpose, like: auth, register and login.


## Dependencies
In this project [poetry](https://python-poetry.org/) is used as package dependency manager. Below python packages are used in this project.

- python = "^3.11"
- uvicorn = {extras = ["standard"], version = "^0.20.0"}
- fastapi = {extras = ["all"], version = "^0.89.1"}
- json-log-formatter = "^0.5.1"
- alembic = "^1.9.2"
- databases = {extras = ["aiomysql"], version = "^0.7.0"}
- loguru = "^0.6.0"
- cryptography = "^38.0.1"
- bcrypt = "^4.0.0"
- sqlalchemy = "^1.4.46"
- pyjwt = "^2.6.0"
- mysqlclient = "^2.1.1"

## How To Run Locally

Clone the project

```bash
  git clone https://github.com/theshohidul/FastAPI-Boilerplate.git
```

Go to the project directory

```bash
  cd FastAPI-Boilerplate
```

To run this project locally, go to `/docker` folder and edit `.env` file if required. 
Then open a terminal inside the `/docker` folder and run the below command in the terminal.

```bash
  docker compose up 
```
After docker containers are up, you can access the application in: http://localhost:8080

Then  exec inside the docker app container and activate the venv, and go to /app/core/db/migrations - run below command: 
```bash
  alembic upgrade head
```

This will create all required tables.

## Contributing

Contributions are always welcome!


## Authors

- [@theshohidul](https://github.com/theshohidul)


## 🚀 About Me
I'm a full stack developer...

=======
# FastAPI-Boilerplate
>>>>>>> 1884bb005203a26226e853440ea05bf214802286
