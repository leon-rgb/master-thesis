import os
import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import ttest_rel, ttest_1samp, wilcoxon
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

# Define the current directory and file paths
current_directory = os.getcwd()
file_path = os.path.join(current_directory, "other documents", "evaluation", "experiment-data.xlsx")

# Load the data from both Excel files
data1 = pd.read_excel(file_path, sheet_name = 1)
data2 = pd.read_excel(file_path, sheet_name = 2)
data_frames = [data1, data2]

# Define the neutral score
neutral_score = 3

print("Chatbot improves explainability and usability:")
# Perform tests for Q3, Q4, Q5 in data2
for col in ['Q3', 'Q4', 'Q5']:
    data_col = data2[col].dropna()
    
    # Check normality assumption for t-test
    if data_col.size >= 20:  # Using Central Limit Theorem approximation
        t_stat, p_ttest = ttest_1samp(data_col, neutral_score)
        test_used = 't-test'
    else:
        t_stat, p_ttest = wilcoxon(data_col - neutral_score)
        test_used = 'Wilcoxon test'
    
    print(f"Performing {test_used} for {col}:")
    print(f"  Test statistic: {t_stat:.4f}")
    print(f"  p-value: {p_ttest:.4f}")
    print("-------------------------------------------")


# Perform test for Q6 in data2 
col = 'Q6'
data_col = data2[col].dropna()

print("Preference for chatbot over traditional methods:")
# Check normality assumption for t-test
if data_col.size >= 20:  # Using Central Limit Theorem approximation
    t_stat, p_ttest = ttest_1samp(data_col, neutral_score)
    test_used = 't-test'
else:
    t_stat, p_ttest = wilcoxon(data_col - neutral_score)
    test_used = 'Wilcoxon test'

print(f"Performing {test_used} for {col}:")
print(f"  Test statistic: {t_stat:.4f}")
print(f"  p-value: {p_ttest:.4f}")
print("-------------------------------------------")



# Extract relevant columns for tasks from data1 (assuming data1 contains these columns)
task_columns = ['T1-time', 'T2-time', 'T3-time', 'T4-time', 'T5-time', 'T6-time']
data_tasks = data1[task_columns].dropna()
print("Task duration for device control vs. information retrieval:")

# Perform test
# Check normality assumption for t-test
if data_tasks.shape[0] >= 20:  # Using Central Limit Theorem approximation
    t_stat, p_ttest = ttest_rel(data_tasks['T5-time'], data_tasks['T1-time'] + data_tasks['T2-time'] + data_tasks['T3-time'] + data_tasks['T4-time'])
    test_used = 'paired t-test'
else:
    t_stat, p_ttest = wilcoxon(data_tasks['T5-time'] - (data_tasks['T1-time'] + data_tasks['T2-time'] + data_tasks['T3-time'] + data_tasks['T4-time']))
    test_used = 'Wilcoxon signed-rank test'

print(f"Performing {test_used} for T5 vs T1-T4:")
print(f"  Test statistic: {t_stat:.4f}")
print(f"  p-value: {p_ttest:.4f}")
print("-------------------------------------------")

# Perform test
# Check normality assumption for t-test
if data_tasks.shape[0] >= 20:  # Using Central Limit Theorem approximation
    t_stat, p_ttest = ttest_rel(data_tasks['T6-time'], data_tasks['T1-time'] + data_tasks['T2-time'] + data_tasks['T3-time'] + data_tasks['T4-time'])
    test_used = 'paired t-test'
else:
    t_stat, p_ttest = wilcoxon(data_tasks['T6-time'] - (data_tasks['T1-time'] + data_tasks['T2-time'] + data_tasks['T3-time'] + data_tasks['T4-time']))
    test_used = 'Wilcoxon signed-rank test'

print(f"Performing {test_used} for T6 vs T1-T4:")
print(f"  Test statistic: {t_stat:.4f}")
print(f"  p-value: {p_ttest:.4f}")
print("-------------------------------------------")