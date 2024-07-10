import pandas as pd

# Load the CSV file
csv_file = 'other documents\models.csv'
df = pd.read_csv(csv_file)

# Convert to LaTeX
latex_table = df.to_latex(index=False)

# Save the LaTeX table to a file
with open('table.tex', 'w') as f:
    f.write(latex_table)

print("LaTeX table has been saved to table.tex")
