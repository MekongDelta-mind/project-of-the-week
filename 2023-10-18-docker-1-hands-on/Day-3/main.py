import pandas as pd
import zipfile
import os

csv_url = "https://s3.amazonaws.com/tripdata/202302-citibike-tripdata.csv.zip"

csv_name = '202302-citibike-tripdata.csv'
os.system(f"wget {csv_url} ")

zip_filename = '202302-citibike-tripdata.csv.zip'
with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
    zip_ref.extractall()
    print(f'{zip_filename} is extracted successfully')

raw_data = pd.read_csv(csv_name, iterator=True, chunksize=100000)
df = next(raw_data)

print(f'Shape of the dataframe: {df.shape}')
print(f"The details about the numarical columns in the dataframe")
print(df.describe)