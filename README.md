# Automated Machine Learning Project

This project is an automated machine learning pipeline that takes raw CSV datasets,
preprocesses them, and prepares them for model training. Built as part of a learning project.

## Project Structure
```
Automated_MachineLearning_Project/
├── ml_engine/
│   ├── __init__.py
│   └── preprocessing.py
├── uploads/
│   ├── Credit Card Defaulter Prediction.csv
│   ├── amazon_sales_dataset.csv
│   ├── bmw_global_sales_2018_2025.csv
│   └── starbucks_customer_ordering_patterns.csv
├── test_processing.py
└── .gitignore
```

## How to Set Up

Step 1 - Clone the repository
git clone https://github.com/Aishwarya26GM/Automated_MachineLearning_Project.git
cd Automated_MachineLearning_Project

Step 2 - Create a virtual environment
python -m venv .venv

Step 3 - Activate the virtual environment
On Windows:
.\.venv\Scripts\Activate.ps1

Step 4 - Install the required libraries
pip install -r requirements.txt

## How to Run

python test_processing.py

## Datasets Used

- Credit Card Defaulter Prediction
- Amazon Sales Dataset
- BMW Global Sales 2018 to 2025
- Starbucks Customer Ordering Patterns

## Tools and Technologies

- Python 3.12
- Pandas
- Scikit-learn