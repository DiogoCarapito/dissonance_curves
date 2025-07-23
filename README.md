# streamlit_app_template

[![Github Actions Workflow](https://github.com/DiogoCarapito/streamlit_app_template/actions/workflows/main.yaml/badge.svg)](https://github.com/DiogoCarapito/streamlit_app_template/actions/workflows/main.yaml)

Streamlit python project template

Python version: 3.12.5

Streamlit version: 1.40.0

## cheat sheet

### setup

copy all files (folders, hidden and non-hidden files) to the higher directory
usefull if you clone the repo into your desired directory
ignore if clone and after change the name of the directory

```bash
mv streamlit_app_template/{*,.*} . && rm -r streamlit_app_template/
```

### venv

create and activate .venv

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

### Dockerfile

#### build

```bash
docker build -t Home:latest .
````

#### check image id

```bash
docker images
````

#### run with image id

```bash
docker run -p 8501:8501 Home:latest
````
