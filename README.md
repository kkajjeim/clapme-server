## clapme
this is clamp repository

### 1. create and activate venv

```shell
python3 -m venv venv
source venv/bin/activate
```

### 2. install packages using pip

```shell
pip install -r requirements.txt
```

### 3. run server

```shell
cd clapme
FLASK_APP=__init__.py flask run
(or)
python3 __init__.py
```

### 4. schemas

- user
- routine
- success
- idea
- color


### 5. API

|endpoint           |method|description                          |
|-------------------|------|-------------------------------------|
|/signup            |POST  |sign up                              |
|/login             |POST  |sign in                              |
|/routine           |POST  |create new routine                   |
|                   |GET   |get routine information by id        |
|/routines          |GET   |get daily routine                    |
|                   |GET   |get all routines                     |
|/routine-materials |GET   |get routine ui helper datas          |
|/idea              |GET   |get random idea or idea list by type |


