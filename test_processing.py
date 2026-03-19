from ml_engine.preprocessing import preprocess_dataset

dataset_path = "uploads/bmw_global_sales_2018_2025.csv"

data = preprocess_dataset(dataset_path)

print("X_train",data["X_train"].shape)
print("X_test",data["X_test"].shape)
print("y_train:", data["y_train"].shape)
print("y_test:", data["y_test"].shape)