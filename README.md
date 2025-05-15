This is just a project done during Professor Jefferson Lobato's Django course.

## Getting Started

1- Highly recommended to create a virtual environment for installing dependencies:

```bash
python3 -m venv venv
```

2- You need to install the dependencies:

```bash
pip3 install -r requirements.txt
```

3- Now you need to configure the '.env' file.

- Just rename the '.env.example' file to '.env' and fill the fields with necessary informations.

- Choose and configure your database by filling in the required fields

- For this project, it used the 'PostgreSQL'.

4- In this step, you need to apply the database migrations.

```bash
python3 manage.py migrate
```

5- Create a _super user_ (OPTIONAL):

- Use the command below and fill in the fields that will appear. Email is optional.

```bash
python3 manage.py createsuperuser
```

6- Finally, run the server:

```bash
python3 manage.py runserver
```

The server will be started at [http://localhost:8000](http://localhost:8000).

## Learn More

Django Course - Jefferson Lobato.

- [Click here](https://www.youtube.com/watch?v=ZNFVFTqaL60&list=PLLVddSbilcumgeyk0z6ko5U_FYPfbRO2C&index=1) to access the lessons of the course used in this project.
