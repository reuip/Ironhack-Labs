#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as _pd
'''Text about what it does

    Parameters
    ---------------
    p1 (type): desc

    Returns
    ---------------
    xyz

    '''


# # Count missing values

# In[2]:


def a_count_missing_values(dataframe):
    '''Takes a dataframe and returns information about missing values.

    Parameters
    ---------------
    dataframe (type): dataframe to analyze for missing values

    Returns
    ---------------
    Dataframe including column names, missing count, and missing %

    '''
    count_missing_val=dataframe.isnull().sum()
    count_all_val=len(dataframe)
    missing_ratio=(count_missing_val/count_all_val)*100
    data={'column':count_missing_val.index,"# missing values":count_missing_val.values,"% missing values":missing_ratio}
    count_missing_values_and_percent=_pd.DataFrame(data)
    count_missing_values_and_percent.reset_index(drop=True,inplace=True)

    return count_missing_values_and_percent


# In[3]:


# Drop rows/columns


# ## Drop Col/Row based on user-defined input

# In[4]:


def b_drop_by_input(dataframe,drop_list,axis=1):
    '''Drops all rows or columns from a database that are in the drop_list
    
    Parameters
    ---------------
    dataframe: The dataframe to drop rows/columns from
    drop_list (list): list of row indexes or column names to drop
    axis (int): Whether 0 (row) or 1 (column)

    Returns
    ---------------
    dataframe with defined rows or columns dropped

    '''
    
    dataframe.drop(drop_list, axis = axis, inplace = True) 
    return dataframe


# ## Drop Col/Row based on threshold

# In[5]:


def b_drop_by_threshold(dataframe,threshold,axis=1):
    '''Drops rows or columns from a database unless they have 'threshold' percent of values available.  
    You will receive a prompt before action is taken
    
    Parameters
    ---------------
    dataframe: The dataframe to drop rows/columns from
    threshold (int): Percent (written as .3 for 30%) of available data needed to keep record
    axis (int): Whether 0 (row) or 1 (column)

    Returns
    ---------------
    dataframe with rows or columns dropped that do not meet threshold

    '''
    if axis==0:
        curr_records=len(dataframe)
        drop_threshold=math.floor(len(dataframe.columns)*threshold)
    elif axis==1:
        curr_records=len(dataframe.columns)
        drop_threshold=math.floor(len(dataframe)*threshold)    
     
    print("Total records before drop",curr_records)

    df_temp=dataframe.copy()
    df_temp.dropna(axis=axis,thresh=drop_threshold,inplace=True)
    
    if axis==0:
        len_of_temp=len(df_temp)
    elif axis==1:
        len_of_temp=len(df_temp.columns)

    make_change=input(f"New file will contain {len_of_temp} records, commit? (y/n)")
    if make_change.lower()=="y":
        dataframe.dropna(axis=axis,thresh=drop_threshold,inplace=True)
    else:
        print("Changes not implemented")
    
    return dataframe


# # Clean categorical data

# In[6]:


def c_check_categorical(dataframe):
    '''For each categorical column in dataframe, finds unique values and return them in dictionary.
    Useful for determining whether a column has typos or inconsistency in the data.

    Parameters
    ---------------
    dataframe: dataframe to review

    Returns
    ---------------
    Dictionary of unique values per categorical column

    '''
    categorical_df=dataframe.select_dtypes(object)
    unique_dict={col: categorical_df[col].unique() for col in categorical_df}
    return unique_dict

def c_standardize_categorical(dataframe,replace_map):
    '''Updates categorical columns in a dataframe by replacing a list of 'wrong values' with a 'correct value'. 
    Used to clean up or standardize terms used for a categorical value (e.g. 'm', 'male', 'man' all to 'male')

    Parameters
    ---------------
    dataframe: Dataframe to apply changes to
    replace_map: Dictionary of wrong values to replace with correct values.  Nested dictionary using the following format:
    {column_name: {correct_value:[wrong_val1,wrong_val2]}}

    Returns
    ---------------
    Updated dataframe

    '''
    
    for key in replace_map.keys():
        for key2 in replace_map[key].keys():
            list_values=replace_map[key][key2]
            dataframe.loc[dataframe[str(key)].isin(list_values),key]=str(key2)
    return dataframe


# # Clean numerical data

# In[7]:


def d_nan_to_mean(dataframe,columns="all"):
    '''For each column containing numbers, replaces blank values with the mean of the column

    Parameters
    ---------------
    dataframe: dataframe to make changes to
    columns (list): List of columns to apply function to.  If blank, applies to all numerical columns

    Returns
    ---------------
    Updated dataframe

    '''
    #If column not defined, get all integer columns that contain NANs
    if columns=="all":
        col_list=dataframe.columns
        integers_with_nan=[]
        for i in col_list:
            if dataframe[i].isnull().values.any()==True:
                if dataframe[i].dtype!='O':
                    integers_with_nan.append(i)
    
    #If user defined column list, assign it to the integers_with_nan value
    else:
        integers_with_nan=columns
    
    #Loop through all columns in list, for each get the mean and fillna with mean
    for j in integers_with_nan:
        temp_mean=np.mean(dataframe[j])
        dataframe[j]=dataframe[j].fillna(temp_mean)
    
    return dataframe


# In[ ]:




