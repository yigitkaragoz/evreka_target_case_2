import pandas as pd

# Load the data
waste_data = pd.read_csv('waste_data_timeseries.csv')
location_data = pd.read_csv('location_data.csv')

# Convert 'VisitDate' to datetime for processing
waste_data['VisitDate'] = pd.to_datetime(waste_data['VisitDate'])

# Cap fullness levels at 100% and create overflow flags
fullness_columns = [col for col in waste_data.columns if col.startswith('%')]
for col in fullness_columns:
    waste_data[f"{col}_overflow"] = waste_data[col] > 100
    waste_data[col] = waste_data[col].clip(upper=100)

# Calculate daily average fullness per location
waste_data['date'] = waste_data['VisitDate'].dt.date
daily_avg_fullness = waste_data.groupby(['SPID', 'date'])[fullness_columns].mean().reset_index()
daily_avg_fullness.to_csv('daily_avg_fullness.csv', index=False)

# Analyze peak collection times by hour
waste_data['hour'] = waste_data['VisitDate'].dt.hour
peak_collection_times = waste_data.groupby(['SPID', 'hour']).size().reset_index(name='visit_count')
peak_collection_times.to_csv('peak_collection_times.csv', index=False)

# Prepare location-based data for heatmap visualization by merging with location data
location_fullness = pd.merge(daily_avg_fullness, location_data[['SPID', 'Latitude', 'Longitude']], on='SPID', how='left')
location_fullness.to_csv('location_fullness.csv', index=False)

print("Data processing complete. Files generated: daily_avg_fullness.csv, peak_collection_times.csv, location_fullness.csv")
