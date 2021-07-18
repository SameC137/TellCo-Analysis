import pandas as pd




def change_type(df):
    df["Start"]=pd.to_datetime(df["Start"], format='%m/%d/%Y %H:%M', errors='coerce')
    df["End"]=pd.to_datetime(df["End"], format='%m/%d/%Y %H:%M', errors='coerce')

    df['Handset Manufacturer'] = df['Handset Manufacturer'].astype('str')
    df['Last Location Name'] = df['Last Location Name'].astype('str')
    df['Bearer Id'] = df['Bearer Id'].apply(lambda x: '{:.0f}'.format(x))
    df['Bearer Id'] = df['Bearer Id'].astype('str')

    df['MSISDN/Number'] = df['MSISDN/Number'].astype('str')

    df['IMSI'] = df['IMSI'].astype('str')

    df['IMEI'] = df['IMEI'].astype('str')
    
def form_combination_columns(df):
    df['Total Data (Bytes)'] = df['Total DL (Bytes)'] + df['Total UL (Bytes)']
    df['Social Media (Bytes)'] = df['Social Media DL (Bytes)'] + df['Social Media UL (Bytes)']
    df['Google (Bytes)'] = df['Google DL (Bytes)'] + df['Google UL (Bytes)']
    df['Email (Bytes)'] = df['Email DL (Bytes)'] + df['Email UL (Bytes)']
    df['Youtube (Bytes)'] = df['Youtube DL (Bytes)'] + df['Youtube UL (Bytes)']
    df['Netflix (Bytes)'] = df['Netflix DL (Bytes)'] + df['Netflix UL (Bytes)']
    df['Gaming (Bytes)'] = df['Gaming DL (Bytes)'] + df['Gaming UL (Bytes)']
    df['Other (Bytes)'] = df['Other DL (Bytes)'] + df['Other UL (Bytes)']
