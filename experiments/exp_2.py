import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Read the CSV file
input_file_path = '/home/rexa/DM/Data-mining-algorithms/experiments/input_data.csv'
output_file_path_minmax = 'output_data_minmax.csv'
output_file_path_zscore = 'output_data_zscore.csv'

# Load the data into a DataFrame
df = pd.read_csv(input_file_path)

# Extract the column to be normalized
data_to_normalize = df[['value']]

# Get custom Min-Max range from the user
custom_min = float(input("Enter the  minimum value for Min-Max normalization: "))
custom_max = float(input("Enter the  maximum value for Min-Max normalization: "))

# Min-Max Normalization with custom range
scaler_minmax = MinMaxScaler(feature_range=(custom_min, custom_max))
minmax_normalized_data = scaler_minmax.fit_transform(data_to_normalize)
df_minmax = pd.DataFrame(minmax_normalized_data, columns=['value_minmax'])

# Save Min-Max normalized data to CSV
result_minmax = pd.concat([data_to_normalize, df_minmax], axis=1)
result_minmax.to_csv(output_file_path_minmax, index=False)

print(f"Min-Max normalized data (custom range) saved to {output_file_path_minmax}")

# Z-score Normalization
scaler_zscore = StandardScaler()
zscore_normalized_data = scaler_zscore.fit_transform(data_to_normalize)
df_zscore = pd.DataFrame(zscore_normalized_data, columns=['value_zscore'])

# Save Z-score normalized data to CSV
result_zscore = pd.concat([data_to_normalize, df_zscore], axis=1)
result_zscore.to_csv(output_file_path_zscore, index=False)

print(f"Z-score normalized data saved to {output_file_path_zscore}")
