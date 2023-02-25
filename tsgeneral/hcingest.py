# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_ingest.ipynb.

# %% auto 0
__all__ = ['simple_validator', 'read', 'print_something']

# %% ../nbs/00_ingest.ipynb 3
def simple_validator(df,schema):
    """
    simple_validator is a simple function to validate a given dataframe  with given schema.
    data frame  rows converted into list of dictioners and validates with
    respect to the given schema and gives output a error dictionary.
    Input:
    df  - pandas dataframe
    schema - cerberus schema
    Output:
    if errors  - tuple with True and dictionary with detial errors 
    if no errors - tuple with True and empty dictionary 
    """
    print('this is the function simple_validator')

# %% ../nbs/00_ingest.ipynb 4
def read(file_type:str,file_path:str)-> tuple: 
    """
    This function read  helps  to read any of a csv,excel and parquet file,
    and returns a pandas dataframe.
    
    Parameters
    ----------
    file_type: file type must be one of csv,excel or parquet format.
    file: file path.
        
    Returns
    -------
        if   errors - function returns tuple with boolean value  "False" and dictionary with errors and empty dataframe
        if no errors - function returns tuple with boolean value  "True" and  empty dictionary and  dataframe

    """
    print('this is the function read')

# %% ../nbs/00_ingest.ipynb 5
def print_something():
    print('something')
