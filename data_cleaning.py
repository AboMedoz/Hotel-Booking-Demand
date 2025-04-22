import numpy as np
import pandas as pd

# https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand
df = pd.read_csv('hotel_bookings.csv')
print(df.head())
df.info()

print(np.sum(df.isna(), axis=0))

# Dropping company Column not applicable if we try to impute it
df = df.drop('company', axis=1)

df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])
df['arrival_date'] = pd.to_datetime(df['arrival_date_year'].astype('str') + '/' + df['arrival_date_month'].astype('str')
                                    + '/' + df['arrival_date_day_of_month'].astype('str'))
df = df.drop(['arrival_date_week_number', 'arrival_date_month', 'arrival_date_year', 'arrival_date_day_of_month'],
             axis=1)

# Fill NA Values with Mean
df['children'] = df['children'].fillna(value=df['children'].mean())
df['agent'] = df['agent'].fillna(value=df['agent']. mean())

df = df.dropna()

df.info()
print(df.shape)
