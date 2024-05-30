# Write python code to read excel file from the folder Data and

import pandas as pd

# Load the survey data from the provided Excel file
file_path = 'Data/Survey_Data.xlsx'
data = pd.read_excel(file_path)