# Steps to setup your django development environment 
1. **Install Virtual Environment**:
It's a good practice to create a virtual environment for your Django projects. Virtual environments isolate your project's dependencies from the system-wide Python installation, making it easier to manage dependencies for different projects.


* INSTALLING PYENV

> pyenv is a popular open-source tool that allows you to easily manage multiple versions of Python on your system. It provides a simple and convenient way to install, switch between, and manage different Python versions within isolated environments. This is particularly useful for developers who work on projects that require specific versions of Python or need to avoid conflicts between different Python applications.

```
https://realpython.com/intro-to-pyenv/#build-dependencies
```

2. Create your virtual environment and activate
```
1. pyenv virtualenv environment_name
2. pyenv actiate environment_name
3. pyenv deactivate en
```

> here virtual environments are nothing but python versions only it is just that they are created for isolated development of python projects and locally saved on your system just like any other python version that is installed on your system. It is like npm for python but has extended workload to the managment of several other python versions. you can check that our using the command :
```
pyenv versions
```

<div style="color:red">Always Ensure that you have activated your virtual environment.</div>
</br>


## Installing Django
```
pip install django

pip install black (code formattor)

django-admin startproject backend . (to create files)

python manage.py runserver (to run server)
```

> sometimes your code editor may not be able to connect your django files to your system file so it is always a good practice to select interpreter by pressing F1 and selecting corresponding interpreter.

## Setup PostgreSQL Database Adapter
```
pip install psycopg2
```

### now configure the database connection in settings.py
```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME":"fullstackcourse",
        "USER":"fullstackcourse",
        "PASSWORD":"fullstackcourse",
        "HOST":"localhost",
        "PORT":"5432",
    }
}
```





