# Dissonance curves



[![Github Actions Workflow](https://github.com/DiogoCarapito/dissonance_curves/actions/workflows/main.yaml/badge.svg)](https://github.com/DiogoCarapito/dissonance_curves/actions/workflows/main.yaml)

Dissonance curves

Inspired by minutephysics' video [The Physics Of Dissonance](https://www.youtube.com/watch?v=tCsl6ZcY9ag)
Reference: [Perception of musical consonance and dissonance: an outcome of neural synchronization](https://pmc.ncbi.nlm.nih.gov/articles/PMC2607353/) 

Python version: 3.12.5

Streamlit version: 1.40.0

## cheat sheet

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
