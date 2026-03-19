import os
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler


def preprocess_dataset(dataset_path):

    try:

        if not os.path.exists(dataset_path):
            raise FileNotFoundError("Dataset file not found")

        dataset = pd.read_csv(dataset_path)

        if dataset.empty:
            raise ValueError("Dataset is empty")

        if dataset.shape[1] < 2:
            raise ValueError("Dataset must contain features and a target column")

        print("Dataset loaded successfully")
        print("Shape:", dataset.shape)

        target_column = dataset.columns[-1]

        features = dataset.drop(columns=[target_column]).copy()
        target = dataset[target_column].copy()

        if target.isnull().all():
            raise ValueError("Target column is invalid")

        id_like_columns = [
            col for col in features.columns if "id" in col.lower()
        ]

        if id_like_columns:
            features = features.drop(columns=id_like_columns)

        for column in features.columns:

            if pd.api.types.is_numeric_dtype(features[column]):
                features[column] = features[column].fillna(features[column].mean())
            else:
                features[column] = features[column].fillna(features[column].mode()[0])

        if pd.api.types.is_numeric_dtype(target):
            target = target.fillna(target.mean())
        else:
            target = target.fillna(target.mode()[0])

        for column in features.columns:

            if not pd.api.types.is_numeric_dtype(features[column]):
                encoder = LabelEncoder()
                features[column] = encoder.fit_transform(features[column])

        if not pd.api.types.is_numeric_dtype(target):
            target = LabelEncoder().fit_transform(target)

        scaler = StandardScaler()
        scaled_features = scaler.fit_transform(features)

        X_train, X_test, y_train, y_test = train_test_split(
            scaled_features,
            target,
            test_size=0.2,
            random_state=42
        )

        return {
            "X_train": X_train,
            "X_test": X_test,
            "y_train": y_train,
            "y_test": y_test
        }

    except Exception as error:
        raise Exception(f"Preprocessing Error: {error}")