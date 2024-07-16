import os
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Verify the current working directory
current_directory = os.getcwd()
print(f"Current directory: {current_directory}")

# Define the path to the subdirectory containing the Excel files
subdirectory_path = os.path.join(current_directory, "other documents", "evaluation")

# List all files in the subdirectory for debugging
all_files = os.listdir(subdirectory_path)
print(f"All files in subdirectory: {all_files}")

# Step 1: Load the Excel files and extract similarity scores from column "F"
files = glob.glob(os.path.join(subdirectory_path, "*.xlsx"))

# Print the list of files found for debugging
print(f"Files found: {files}")

if not files:
    print("No .xlsx files found in the specified subdirectory.")
else:
    for file in files:
        print(f"\nProcessing file: {file}")
        df = pd.read_excel(file, usecols="F")
        similarity_scores = df.iloc[:, 0].dropna().tolist()

        # Convert to a NumPy array for convenience
        similarity_scores = np.array(similarity_scores)

        # Step 2: Calculate descriptive statistics
        mean_score = np.mean(similarity_scores)
        median_score = np.median(similarity_scores)
        std_dev_score = np.std(similarity_scores)
        range_score = np.ptp(similarity_scores)  # ptp: peak-to-peak (max - min)

        print(f"Mean: {mean_score}")
        print(f"Median: {median_score}")
        print(f"Standard Deviation: {std_dev_score}")
        print(f"Range: {range_score}")

        # Step 3: Create a histogram to visualize the distribution
        plt.hist(similarity_scores, bins=20, edgecolor='black')
        plt.title(f'Distribution of Similarity Scores for {os.path.basename(file)}')
        plt.xlabel('Similarity Score')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()

        # Alternatively, create a density plot
        plt.figure()
        density = plt.hist(similarity_scores, bins=20, density=True, alpha=0.6, color='g')
        plt.title(f'Density Plot of Similarity Scores for {os.path.basename(file)}')
        plt.xlabel('Similarity Score')
        plt.ylabel('Density')
        plt.grid(True)
        plt.show()

        # Step 4: Compute the percentage of responses above the threshold (0.65)
        threshold = 0.65
        above_threshold_percentage = np.sum(similarity_scores > threshold) / len(similarity_scores) * 100

        print(f"Percentage of responses above {threshold}: {above_threshold_percentage:.2f}%")
