import os
import pandas as pd
import matplotlib.pyplot as plt

# Define the current directory and file paths
current_directory = os.getcwd()
file_path = os.path.join(current_directory, "other documents", "evaluation", "experiment-data.xlsx")

# Load the data from the Excel file (assuming sheet_name=0)
data0 = pd.read_excel(file_path, sheet_name=0)

# Drop unnamed columns
data0 = data0.loc[:, ~data0.columns.str.contains('^Unnamed')]

# Extract columns of interest
columns_of_interest = ['familarity with smart homes', 'familarity with chatbots', 'category', 'age-group']
data_interest = data0[columns_of_interest]

# Plot frequency distributions for each categorical variable
plt.figure(figsize=(12, 10))

# Plot familiarity with smart homes
plt.subplot(221)
data_interest['familarity with smart homes'].value_counts().sort_index().plot(kind='bar', rot=0, color='darkgray')
plt.title('Frequency Distribution of Familiarity with Smart Homes')
plt.xlabel('Familiarity Level')
plt.ylabel('Frequency')

# Plot familiarity with chatbots
plt.subplot(222)
data_interest['familarity with chatbots'].value_counts().sort_index().plot(kind='bar', rot=0, color='darkgray')
plt.title('Frequency Distribution of Familiarity with Chatbots')
plt.xlabel('Familiarity Level')
plt.ylabel('Frequency')

# Plot job categories
plt.subplot(223)
data_interest['category'].value_counts().plot(kind='bar', rot=0, color='darkgray')
plt.title('Frequency Distribution of Job Categories')
plt.xlabel('Job Category')
plt.ylabel('Frequency')

# Plot age groups
plt.subplot(224)
data_interest['age-group'].value_counts().sort_index().plot(kind='bar', rot=0, color='darkgray')
plt.title('Frequency Distribution of Age Groups')
plt.xlabel('Age Group')
plt.ylabel('Frequency')

plt.tight_layout()
plt.savefig('frequency_distributions.png')
plt.show()
