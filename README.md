# Data Preprocessing Module - Automated ML Platform

This module handles dataset preparation for the Automated ML Platform.
It cleans, preprocesses, and splits raw CSV datasets into structured
data ready for model training.

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
```
git clone https://github.com/Aishwarya26GM/Automated_MachineLearning_Project.git
cd Automated_MachineLearning_Project
```

Step 2 - Create a virtual environment
```
python -m venv .venv
```

Step 3 - Activate the virtual environment
```
.\.venv\Scripts\Activate.ps1
```

Step 4 - Install the required libraries
```
pip install -r requirements.txt
```

## How to Run
```
python test_processing.py
```

## How It Works

The main function to call is:
```
processed_data = preprocess_dataset(dataset_path)
```

It returns the following:
```
X_train = processed_data["X_train"]
X_test  = processed_data["X_test"]
y_train = processed_data["y_train"]
y_test  = processed_data["y_test"]
```

## Error Handling

The module handles the following errors:

- Dataset file not found
- Empty dataset
- Missing target column
- Invalid dataset format

## Datasets Used for Testing

- Credit Card Defaulter Prediction
- Amazon Sales Dataset
- BMW Global Sales 2018 to 2025
- Starbucks Customer Ordering Patterns

## Tools and Technologies

- Python 3.12
- Pandas
- NumPy
- Scikit-learn

## Notes

- Do not modify the backend API files
- Do not add model training logic in this module
- Focus strictly on dataset preparation
- Output structure must match exactly as defined above

## Project Lead and Mentor

Ritesh Bonthalakoti
Team LearnDepth