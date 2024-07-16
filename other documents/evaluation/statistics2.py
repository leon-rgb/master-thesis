import os
import pandas as pd
from scipy.stats import wilcoxon

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
column_name = 'semantic similarities' 

# Extract the semantic similarity values
similarity_values_1 = data1[column_name].dropna().values
similarity_values_2 = data2[column_name].dropna().values

# Ensure both datasets have the same length by removing mismatched rows
min_length = min(len(similarity_values_1), len(similarity_values_2))
similarity_values_1 = similarity_values_1[:min_length]
similarity_values_2 = similarity_values_2[:min_length]

# Perform Wilcoxon signed-rank test
stat, p_value = wilcoxon(similarity_values_1, similarity_values_2)

# Output the results
print(f"Wilcoxon signed-rank test statistic: {stat}")
print(f"P-value: {p_value}")
