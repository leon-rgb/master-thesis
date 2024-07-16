import os
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Define the current directory and file paths
current_directory = os.getcwd()
file_path = os.path.join(current_directory, "other documents", "evaluation", "experiment-data.xlsx")

# Load the data from both Excel files
data1 = pd.read_excel(file_path, sheet_name = 1)
data2 = pd.read_excel(file_path, sheet_name = 2)
data_frames = [data1, data2]

# Print headers to check the column names
#print("Headers for experiment-data.xlsx 1 ", data1.columns)
#print("Headers for experiment-data.xlsx 1 ", data2.columns)

# Function to calculate descriptive statistics
def calculate_statistics(df, column):
    stats_dict = {}
    stats_dict['mean'] = df[column].mean()
    stats_dict['median'] = df[column].median()
    stats_dict['mode'] = df[column].mode().values[0] if not df[column].mode().empty else np.nan
    stats_dict['std_dev'] = df[column].std()
    stats_dict['range'] = df[column].max() - df[column].min()
    stats_dict['frequency_distribution'] = df[column].value_counts().to_dict()
    return stats_dict

# Initialize a list to hold statistics for time columns
time_statistics = []
# Initialize a list to hold statistics for Q columns in data2
q_statistics = []

# Iterate through each dataframe
for i, df in enumerate(data_frames, start=1):
    # Drop unnamed columns
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    
    # Filter time columns
    time_columns = [col for col in df.columns if 'time' in col.lower()]
    
    # Calculate statistics for each time column
    for column in time_columns:
        stats = calculate_statistics(df, column)
        stats['Task'] = column
        time_statistics.append(stats)

# Create a DataFrame for the statistics
stats_df = pd.DataFrame(time_statistics)

# Generate LaTeX table
latex_table = stats_df[['Task', 'mean', 'median', 'mode', 'std_dev', 'range']].to_latex(index=False)

# Save the LaTeX table to a file
with open("time_statistics_table.tex", "w") as file:
    file.write(latex_table)

# Print LaTeX table string (optional)
print(latex_table)



# Drop unnamed columns
data2 = data2.loc[:, ~data2.columns.str.contains('^Unnamed')]

# Filter Q columns
q_columns = [col for col in data2.columns if 'Q' in col]

# Calculate statistics for each Q column
for column in q_columns:
    stats = calculate_statistics(data2, column)
    stats['Question'] = column
    q_statistics.append(stats)

# Create a DataFrame for the statistics
q_stats_df = pd.DataFrame(q_statistics)

# Define a format function for two decimal places
float_format = "{:.2f}".format

# Generate LaTeX table with formatted float values
latex_table_q = q_stats_df[['Question', 'mean', 'median', 'mode', 'std_dev']].to_latex(index=False, float_format=float_format)

# Save the LaTeX table to a file
with open("q_statistics_table.tex", "w") as file:
    file.write(latex_table_q)

# Print LaTeX table string (optional)
print(latex_table_q)





# Drop unnamed columns
data1 = data1.loc[:, ~data1.columns.str.contains('^Unnamed')]

# Filter time, attempts, and successful columns
time_columns = [col for col in data1.columns if 'time' in col.lower()]
attempts_columns = [col for col in data1.columns if 'attempts' in col.lower()]
successful_columns = [col for col in data1.columns if 'successful' in col.lower()]

# Create subplots for each task
fig, axes = plt.subplots(len(time_columns), 1, figsize=(10, len(time_columns) * 4))

# Plot distribution of times for each task using box plots on the same graph
plt.figure(figsize=(12, 8))
plt.boxplot([data1[col].dropna() for col in time_columns], labels=time_columns, vert=False)
plt.xlabel('Time')
plt.title('Distribution of Times for Each Task')
plt.savefig('distribution_of_times_boxplot.png')
plt.show()

# Plot bar chart of successful and unsuccessful participants for each task
success_counts = []
for column in successful_columns:
    success_counts.append(data1[column].value_counts())

success_df = pd.DataFrame(success_counts).T.fillna(0)
success_df.columns = successful_columns
success_df.plot(kind='bar', figsize=(10, 6))
plt.xlabel('Success Status')
plt.ylabel('Number of Participants')
plt.title('Number of Successful and Unsuccessful Participants for Each Task')
plt.savefig('success_bar_chart.png')
plt.show()

# Plot bar chart of the distribution of attempts for each task
attempts_counts = []
for column in attempts_columns:
    attempts_counts.append(data1[column].value_counts())

attempts_df = pd.DataFrame(attempts_counts).T.fillna(0)
attempts_df.columns = attempts_columns
attempts_df.plot(kind='bar', figsize=(10, 6))
plt.xlabel('Number of Attempts')
plt.ylabel('Frequency')
plt.title('Distribution of Attempts for Each Task')
plt.savefig('attempts_bar_chart.png')
plt.show()