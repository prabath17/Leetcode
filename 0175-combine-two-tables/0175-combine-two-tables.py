import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    result = pd.merge(person, address, on='personId', how='left')
    
    # Select required columns
    return result[['firstName', 'lastName', 'city', 'state']]