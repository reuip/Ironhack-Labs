#!/usr/bin/env python
# coding: utf-8

# # Contains functions for loading, cleaning, and merging files for data analysis

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


# # Load csvs

# ## One file

# In[2]:


def a_load_file(file_path,rem_dupes=True):
    '''Loads a single csv file into a dataframe.
    Performs basic cleaning functions on it (lowercase columns, rows). 

    Parameters
    ---------------
    file_path (path): Location of the dataframe
    rem_dupes (bool): Option to remove duplicate and blank rows on load.  Default is true.
    
    Returns
    ---------------
    Cleaned dataframe
    '''
    df=_pd.read_csv(file_path)
    df.columns=lowercase_columns(df)
    df.update(lowercase_rows(df))
    if rem_dupes==True:
        remove_duplicates(df)
    
    return df
    


# ## Multiple files in folder

# In[3]:


def a_load_folder(folder_path,rem_dupes=True):
    '''Loads all csv files from a folder into a list of dataframes. 
    Performs basic cleaning functions on them (lowercase columns, rows).

    Parameters
    ---------------
    folder_path (path): Location of the dataframes
    rem_dupes (bool): Option to remove duplicate and blank rows on load.  Default is true.

    Returns
    ---------------
    A list of dataframes
    '''
    import glob
    #Gather all csv files
    all_files = glob.glob(folder_path + "/*.csv")
    dataframe_list=[]
    file_count=len(all_files)
    
    #For each file, add it to a temporary dataframe, apply cleaning functions, then save to dataframe list
    for i in range(file_count):
        temp_df = _pd.read_csv(all_files[i])
        temp_df.columns=lowercase_columns(temp_df)
        temp_df.update(lowercase_rows(temp_df))
        if rem_dupes==True:
            remove_duplicates(temp_df)
        dataframe_list.append(temp_df)
        
    
    return dataframe_list


# # Lowercase columns and rows

# In[4]:


def b_lowercase_columns(dataframe):
    '''Lowercases column names for one dataframe. Useful for merging dataframes on column names.

    Parameters
    ---------------
    dataframe: dataframe to apply changes to

    Returns
    ---------------
    Updated column names as list
    '''
    lowercased_cols = [i.lower() for i in dataframe.columns]
    return lowercased_cols
    
def b_lowercase_rows(dataframe):
    '''Lowercases string values within one dataframe. Useful for standardizing categorical variables.

    Parameters
    ---------------
    dataframe: dataframe to apply changes to

    Returns
    ---------------
    Updated dataframe

    '''
    df=dataframe.applymap(lambda x:x.lower() if type(x) == str else x)
    return df


# # Align column names across documents

# In[1]:


def c_unique_col_find(dataframe_list):
    '''Determines which columns are missing in each file. To support merging dataframes, or renaming of columns before merging

    Parameters
    ---------------
    dataframe_list (list): Dataframes in list form

    Returns
    ---------------
    Dictionary with key=dataframe index and value=list of columns not present in that dataframe

    '''

    all_col_names=[]
    temp_col_names=[]
    unmatched_col_names=[]
    unmatched_col_dict={}
    
    #Get all column names in one list
    for df in dataframe_list:
        [all_col_names.append(col) for col in df.columns]
    
    #Remove duplicates
    unique_col_names=list(set(all_col_names))
    
    #Check which dataframes are missing which column names. Place these in a dictionary with key of dataframe number.
    df_num=1
    for df in dataframe_list:
        [temp_col_names.append(col) for col in df.columns]
        [unmatched_col_names.append(col) for col in unique_col_names if col not in temp_col_names]        
        unmatched_col_dict[df_num]=unmatched_col_names
        unmatched_col_names=[]
        temp_col_names=[]
        df_num+=1

    return unmatched_col_dict



def c_unique_col_rename(dataframe_list,rename_dict):
    '''Renames columns in a dataframe list using a rename dictionary. Used to harmonize column names for proper merging of multiple dataframes.

    Parameters
    ---------------
    dataframe_list (list): List of dataframes with columns to rename
    rename_dict (dictionary): Dict with Key=old column name, Value=new column name
    
    Returns
    ---------------
    Dataframe list with renamed columns

    '''
    for i in dataframe_list:
        i.rename(columns=rename_dict,inplace=True)
    return dataframe_list


# # Merge dataframes by row/column

# In[ ]:


def d_merge_dataframes(dataframe_list,axis=0, column=""):
    '''Merges multiple dataframes into one dataframe along a specific axis
    
    Parameters
    ---------------
    dataframe_list (list): List of dataframes to be merged
    axis (int): Axis to merge the files on. 0 for row, 1 for column
    column (string or list): When merging by column, the specific fields to merge on
    
    Returns
    ---------------
    One merged dataframe
    
    '''
    #---Error checking---#
    #Ensure dataframe list is a list, if not return single df
    if len(dataframe_list)<2:
        return dataframe_list
    
    
    #If merge by row, concat the lists together and return the dataframe
    if axis==0:
        combined_df=_pd.concat(dataframe_list,axis=0,ignore_index=True)
        return combined_df
    
    #If merge by column, merge based on column list
    elif axis==1:
        combined_df=dataframe_list[0]
        for i in range(1,len(dataframe_list)):
            combined_df=combined_df.merge(dataframe_list[i], on=column)
        return combined_df
    


# # Remove duplicates

# In[2]:


def e_remove_duplicates(dataframe):
    '''Removes duplicate rows and blank rows from the dataframe

    Parameters
    ---------------
    dataframe: Dataframe to evaluate

    Returns
    ---------------
    Cleaned dataframe 

    '''
    print("Rows before drop",len(dataframe))
    dataframe.drop_duplicates(inplace=True)
    #Removes rows if they are completely blank
    dataframe.dropna(how="all",axis=0, inplace=True)
    print("Rows after drop",len(dataframe))
    return dataframe


# In[ ]:




