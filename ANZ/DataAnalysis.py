
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
from collections import Counter

df = pd.read_excel("/Users/gympohnpimol/Desktop/Virtual-Internship-InsideSherpa/ANZ/ANZ_synthesised_transaction_dataset.xlsx")

"Dropping irrelevant features"
col_to_delete = ["bpay_biller_code", "merchant_code"]
df.drop(col_to_delete, inplace = True, axis = 1)
df["date"] = pd.to_datetime(df["date"])
df = df.dropna()

"Exploratora Data Analysis"
date_values = df["date"].value_counts() # Total number of transactions on each day
customer_value = df["customer_id"].value_counts()

"""Histogram of Purchase Transaction amount"""
bill = sns.distplot(df.amount)
bill.set(xlabel = "Transaction Amount", ylabel = "Frequency", title = "Purchase Transaction amount")
sns.despine()
plt.show()

"""Visited Frequency"""
x = df["merchant_state"]
loc_count = Counter(x)
loc_df = pd.DataFrame.from_dict(loc_count, orient = "index")
loc_df = loc_df[0].sort_values(ascending=False)
loc_df.plot(kind = "bar")
plt.xlabel("State")
plt.ylabel("Frequency")
plt.title("Visited Frequency")
plt.show()

"""Balance per day"""
balances = df.groupby("date").sum()
plt.plot(balances.index, balances.balance)
plt.xlabel("Date")
plt.ylabel("Balance")
plt.title("Balance per day")
plt.show()

balances = df.groupby(df["date"].dt.strftime("%B"))["balance"]
balances = df.groupby(df["date"].dt.strftime("%W"))["merchant_state"]
# print(df)