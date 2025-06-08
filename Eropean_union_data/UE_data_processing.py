import pandas as pd

# Load the Excel file
excel_file = pd.ExcelFile('UE_data.xlsx')

# List to store processed sheets
dfs = []

# Fixed header
fixed_columns = ['country', '2014', '2015', '2016', '2017', '2018', '2020', '2021', '2023', '2024']

# Loop through each sheet
for sheet_name in excel_file.sheet_names:
    if sheet_name.startswith('Sheet'): 
        # Read metadata
        metadata = pd.read_excel(excel_file, sheet_name=sheet_name, nrows=10)
        
        # Extract metadata values
        number_of_persons_employed = metadata.iloc[4, 2]
        economic_activity = metadata.iloc[5, 2]
        information_society_indicator = metadata.iloc[6, 2]
        print('information_society_indicator', information_society_indicator)
        # Read actual data
        df = pd.read_excel(excel_file, sheet_name=sheet_name, skiprows=17, header=None)
        
        # Drop empty rows/columns
        df = df.dropna(how='all')
        df = df.dropna(axis=1, how='all')
        
        # Set fixed header
        df.columns = fixed_columns

        # Add metadata columns
        df['number of persons employed'] = number_of_persons_employed
        df['economic activity'] = economic_activity
        df['information society indicator'] = information_society_indicator
        
        # Add to list
        dfs.append(df)

# Concatenate all
final_df = pd.concat(dfs, ignore_index=True)
final_df.to_excel('final_output.xlsx', index=False)

# Display result
print(final_df.head())
