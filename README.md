# Global Warming Impact Analysis and Future Prediction

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

Machine learning model to predict the weather. It leverages historical weather data to forecast future weather conditions.

---

## Project Overview

This project is designed to:

- Analyze historical climate data and extract meaningful trends.
- Train machine learning models to predict Earth surface temperatures based on spatial and temporal features.
- Provide an interactive web application for users to test predictions using trained models.

---

## Key Components

### **1. Frontend**

- Built using **Nuxt.js** with **TailwindCSS** for responsive design, extended by **DaisyUI** for modern components.
- Features a user-friendly interface for users to input location and time data (latitude, longitude, year, and month) and receive predictions.
- Deployed on **Vercel** for fast and scalable hosting.
- Key files:
  - `frontend/nuxt.config.ts`: Configuration for the frontend application.
  - `frontend/pages/`: Main pages, including `index.vue` for predictions and `about.vue` for project details.
  - `frontend/components/`: Reusable UI components like `Hero.vue`, `Footer.vue`, and `Predictions.vue`.

### **2. Backend**

- Developed using **FastAPI** for serving predictions through RESTful endpoints.
- Handles model loading, input validation, and prediction generation.
- Containerized with **Docker** and deployed on **Google Cloud Platform** (GCP) using a Virtual Machine (VM).
- Key files:
  - `api/app.py`: Main FastAPI application logic.
  - `api/utils.py`: Helper functions for data processing and prediction.
  - `docker-compose.yml`: Configuration for deploying the backend with Docker.

### **3. Machine Learning**

- Models built using **scikit-learn** include:
  - Random Forest (highest accuracy with R² score of 0.9857).
  - K-Nearest Neighbor (KNN).
  - Support Vector Regression (SVR).
  - Linear Regression.
- Key workflows:
  - `notebooks/`: Jupyter notebooks for data preprocessing, modeling, and evaluation.
  - `src/modeling/`: Scripts for training and running predictions.
- Trained models are serialized and stored in the `models/` directory.

### **4. Data Handling**

- Historical climate data sourced from the [Berkeley Earth Surface Temperature dataset](https://berkeleyearth.org/data/).
- Data pipeline processes raw data into clean, usable formats for modeling.
- Key files:
  - `data/processed/global_temperature_final.csv`: Final processed dataset.
  - `src/dataset.py`: Script for data loading and preparation.

### **5. Deployment**

- **Backend**: Hosted on GCP with Docker for scalability and reliability.
- **Frontend**: Deployed on Vercel.
- CI/CD: Automated deployment pipelines configured via GitHub Actions (`.github/workflows/backend-deploy.yml`).

---

## Key Notebooks

Below is an overview of the most significant notebooks:

### **`3.0-weather-prediction-models.ipynb`**

This is the primary notebook containing the core workflow for:

- Data Analysis
- Data Preprocessing
- Exploration of all models and variations
- Model training
- Model Evaluation
- Visualization of results

This notebook provides a comprehensive and detailed walkthrough of the project’s workflow

### **`4.0-simplified.ipynb`**

This notebook presents a cleaner and streamlined version of the workflow:

- The primary focus is on running the key steps efficiently.
- Exploration and detailed steps from `3.0-weather-prediction-models.ipynb` have been omitted.
- Uses modular Python code to call functions from dedicated scripts (`src/` folder), ensuring better reusability and organization.

---

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── frontend/          <- Nuxt.js frontend for user interaction.
│   ├── pages/
│   ├── components/
│   ├── assets/
│   ├── nuxt.config.ts
│   └── package.json
├── api/               <- Backend API built with FastAPI.
│   ├── app.py
│   ├── utils.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .dockerignore
├── .github/           <- CI/CD workflows for automated deployment.
│    └── workflows/
│        └── backend-deploy.yml
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for
│                         src and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   ├── paper          <- Written report of the project.
│   ├── presentation   <- Slides used to present project.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── src   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes src a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling - preprocessing
    │
    ├── modeling
    │   ├── __init__.py
    │   ├── predict.py          <- Code to run model inference with trained models
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

---
