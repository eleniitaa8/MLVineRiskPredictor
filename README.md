# VineRiskPredictor

**iGEM Tarragona Team** - Machine Learning Tisk Predction for Grape Disease

## Overview
We are a group of students from **iGEM Tarragona** participating in the iGEM conference. Our primary research focus is on developing a biosensor for detecting downy mildew (*Plasmopara viticola*) and powdery mildew (*Erysiphe necator*) infections in grapevines. To complement our biosensor, we are building a **Machine Learning** tool that predicts the **risk level** of infection (High, Moderate, Low) based on environmental, phenological, and treatment data.

## Project Objective
- **Develop** a predictive ML model to estimate infection risk in grapevines.  
- **Integrate** meteorological data (temperature, humidity, precipitation), phenological stage, and treatment history as input features.  
- **Output** a risk classification (High/Moderate/Low) to guide preventive measures.  
- **Complement** our biosensor by providing a holistic approach: ML-based early warning plus biosensor confirmation.

## Data Sources
This project uses the following open datasets:

1. **Grape Disease Dataset** (Mendeley Data, CC BY 4.0)  
   https://data.mendeley.com/datasets/94j4ws2325/1  
2. **Environmental IoT Data** (Zenodo – AgriDataValue, CC0)  
   https://zenodo.org/records/14989522  
3. **Proyecto GRAPEVINE** (Aragón Open Data, ODbL)  
   https://opendata.aragon.es/datos/catalogo/dataset/datos-del-proyecto-sobre-vinedos-grapevine#:~:text=GRAPEVINE%20%28https%3A%2F%2Fgrapevine,reducir%20la%20cantidad%20de%20fungicida

## Project Structure (planned)

```plaintext
VineRiskPredictor/
├── data/
│   ├── raw/               # Original CSV datasets
│   ├── processed/         # Cleaned and merged datasets
│   └── external/          # Data from external sources
├── notebooks/
├── src/
│   ├── eda.py                      # General functions to load and visualize data
│   ├── data_ingest.py              # Data loading and preprocessing, CSV merging
│   ├── clean.py                    # Data cleaning functions 
│   ├── feature_engineering.py      # Feature engineering functions
│   ├── train.py                    # Complete pipeline with model training and evaluation
|   ├── predict.py                  # Prediction functions
├── reports/
│   ├── figures/                    # Figures and plots
├── requirements.txt
├── environment.yml
├── README.md
└── .gitignore
```

## Next Steps
1. **Data Preparation**: Clean, align timestamps, and merge raw datasets.  
2. **Feature Engineering**: Generate phenological, meteorological, and treatment features.  
3. **Model Development**: Train baseline classifiers (Logistic Regression), then tree-based ensembles (XGBoost/LightGBM).  
4. **Evaluation & Interpretability**: Use stratified time-series CV, metrics (accuracy, F1, recall), and explainability tools (SHAP, LIME).  
5. **Deployment**: Package model in a Flask/FastAPI app; provide a simple web or CLI interface.

## License & Attribution
Por hacer. !!

---

*Prepared by iGEM Tarragona – May 2025* 