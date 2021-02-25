# imports
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split


def clean_data(df):
    '''
    This function will take in the iris dataframe, drop species_id, 
    rename species_name to species, and create dummy vars of species. 
    '''
    df = df.drop(columns=['species_id'])
    df = df.rename(columns={'species_name': 'species'})
    species_dummies = pd.get_dummies(df.species, drop_first=True)
    df = pd.concat([df, species_dummies], axis=1)
    return df

def split(df, stratify=None):
    '''
    This takes in one df and returns train, validate, and test.
    '''
    train_validate, test = train_test_split(df, test_size=.2, random_state=123, stratify=df[stratify])
    train, validate = train_test_split(train_validate, 
                                       test_size=.3, 
                                       random_state=123, stratify=train_validate[stratify]) 
    return train, validate, test

def prep_iris(df):
    '''
    This function takes in the iris dataframe, drops species_id,
    renames, species_name to species, creates, dummy vars of species, 
    and performs a train, validate, test split.
    '''
    df = clean_data(df)
    train, validate, test = split(df)
    return train, validate, test