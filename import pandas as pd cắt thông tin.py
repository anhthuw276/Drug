import pandas as pd

# Load the original Excel file
file_path = 'Drug_cleanedcc.xlsx'  # Replace with your file path if different
data = pd.read_excel(file_path)

# Filter rows where 'Condition' contains "Acute Bacterial Sinusitis"
condition_to_cut = "Acute Bacterial Sinusitis"
filtered_rows = data[data['Condition'].str.contains(condition_to_cut, na=False)]

# Remaining data after removing the filtered rows
remaining_data = data[~data['Condition'].str.contains(condition_to_cut, na=False)]

# Save the filtered rows to a new Excel file
filtered_file_path = 'Acute_Bacterial_Sinusitis.xlsx'
filtered_rows.to_excel(filtered_file_path, index=False)

# Save the remaining data to a new Excel file
updated_file_path = 'Drug_cleanedcccc_updated.xlsx'
remaining_data.to_excel(updated_file_path, index=False)

print(f"Filtered rows saved to: {filtered_file_path}")
print(f"Updated data saved to: {updated_file_path}")
