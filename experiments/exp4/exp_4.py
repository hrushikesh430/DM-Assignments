import pandas as pd
import math

def calculate_entropy(data, class_column):
    class_counts = data[class_column].value_counts()
    entropy = 0

    for count in class_counts:
        probability = count / len(data)
        entropy -= probability * math.log2(probability)

    return entropy

def calculate_information_gain(data, attribute, class_column):
    total_entropy = calculate_entropy(data, class_column)

    attribute_entropy = 0
    attribute_values = data[attribute].unique()

    for value in attribute_values:
        subset = data[data[attribute] == value]
        subset_entropy = calculate_entropy(subset, class_column)
        weight = len(subset) / len(data)
        attribute_entropy += weight * subset_entropy

    information_gain = total_entropy - attribute_entropy
    return information_gain

# Load data from CSV
file_path = 'input_data.csv'  # Replace with your CSV file path
data = pd.read_csv(file_path)
print(data.iloc[0])
# Replace 'Attribute' with the actual attribute/column name for which you want to calculate information gain
attribute = input("Enter attribute you need to find Info Gain of :")
attribute_name = attribute
# Replace 'PlayTennis' with the actual column name representing the class
class_column_name = 'PlayGame'

info_gain = calculate_information_gain(data, attribute_name, class_column_name)

print(f"Information Gain of '{attribute_name}': {info_gain}")
