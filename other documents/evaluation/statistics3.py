import os
import pandas as pd
from statsmodels.stats.contingency_tables import mcnemar

# Define the current directory and file paths
current_directory = os.getcwd()
file_path_1 = os.path.join(current_directory, "other documents", "evaluation", "shllama3.xlsx")
file_path_2 = os.path.join(current_directory, "other documents", "evaluation", "shllama3instruct.xlsx")

# Load the data from both Excel files
data1 = pd.read_excel(file_path_1)
data2 = pd.read_excel(file_path_2)

# Print headers to check the column names
print("Headers for shllama3.xlsx:", data1.columns)
print("Headers for shllama3instruct.xlsx:", data2.columns)

# Adjust the column name based on the inspection
column_name = 'is_json_correct'

# Extract the binary data for JSON correctness
json_correct_1 = data1[column_name].astype(int)  # Convert to integers if not already
json_correct_2 = data2[column_name].astype(int)  # Convert to integers if not already

# Create the contingency table
contingency_table = pd.crosstab(json_correct_1, json_correct_2)

print("Contingency Table:")
print(contingency_table)

# Perform McNemar's test
result = mcnemar(contingency_table, exact=True)
print(f"McNemar's test statistic: {result.statistic}")
print(f"P-value: {result.pvalue}")

# Interpretation of the results
alpha = 0.05
if result.pvalue < alpha:
    print("There is a significant difference between the models' JSON correctness.")
else:
    print("There is no significant difference between the models' JSON correctness.")
