
import pandas as pd 
import numpy as np
from sklearn.linear_model import LinearRegression 
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor 

df = pd.read_excel("/Users/gympohnpimol/Desktop/Virtual-Internship-InsideSherpa/ANZ/ANZ_synthesised_transaction_dataset.xlsx")

"Modify Data"
df_salary = df[df["txn_description"] == "PAY/SALARY"].groupby("customer_id").mean()

salary = []
for id in df["customer_id"]:
    salary.append(int(df_salary.loc[id]["amount"]))
df["annual_salary"] = salary

df_customer = df.groupby("customer_id").mean()

"Predictive Analytics"
"Linear Regression"
n_train = int(len(df_customer)*0.8)
x_train = df_customer.drop("annual_salary", axis = 1).iloc[:n_train]
y_train = df_customer["annual_salary"].iloc[:n_train]
x_test = df_customer.drop("annual_salary", axis = 1).iloc[n_train:]
y_test = df_customer["annual_salary"].iloc[n_train:]

LR = LinearRegression()
LR.fit(x_train, y_train)
print(f"Linear Regression Training Score: {LR.score(x_train, y_train)}\n")
LR.predict(x_test)
print(f"Linear Regression Testing Score: {LR.score(x_test, y_test)}\n")

"Decision Tree - Classification and Regression"
df_new = df[["txn_description", "gender", "age", "merchant_state", "movement"]]
print(pd.get_dummies(df_new).head())
n_train_new = int(len(df)*0.8)
x_train_new = pd.get_dummies(df_new).iloc[:n_train_new]
y_train_new = df["annual_salary"].iloc[:n_train_new]
x_test_new = pd.get_dummies(df_new).iloc[n_train_new:]
y_test_new = df["annual_salary"].iloc[n_train_new:]

"Classification"
tree_class = DecisionTreeClassifier()
tree_class.fit(x_train_new, y_train_new)
print(f"DecisionTreeClassifier Training Score: {tree_class.score(x_train_new, y_train_new)}\n")
print(f"DecisionTreeClassifier Testing Score: {tree_class.score(x_test_new, y_test_new)}\n")

"Regression"
tree_reg = DecisionTreeRegressor()
tree_reg.fit(x_train_new, y_train_new)
print(f"DecisionTreeRegressor Training Score: {tree_reg.score(x_train_new, y_train_new)}\n")
print(f"DecisionTreeRegressor Testing Score: {tree_reg.score(x_test_new, y_test_new)}\n")