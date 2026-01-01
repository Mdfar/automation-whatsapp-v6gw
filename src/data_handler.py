import pandas as pd

def load_contact_data(file_path): """ Cleans and prepares Excel data for automation """ df = pd.read_excel(file_path) # Ensure phone numbers are strings and sanitized df['Number'] = df['Number'].astype(str).str.replace('+', '').str.replace(' ', '') return df