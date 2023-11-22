import pandas as pd

# Read the CSV file
input_file_path = 'input_data.csv'

# Load the data into a DataFrame
df = pd.read_csv(input_file_path)

print(df.iloc[0])
# Calculate the 5-number summary
summary_stats = df.quantile([0, 0.25, 0.5, 0.75, 1])

# Rename the index for clarity
summary_stats.index = ['min', 'Q1', 'median', 'Q3', 'max']

# Print the 5-number summary
print("5-Number Summary:")
print(summary_stats)

# Save the 5-number summary to a new CSV file
output_file_path_summary = 'output_5_number_summary.csv'
summary_stats.to_csv(output_file_path_summary)

print(f"\n5-Number summary saved to {output_file_path_summary}")
