
# Evreka Data Engineer Assessment Target Case 2

## Project Structure

- **analysis/**: Contains scripts used for data analysis and preprocessing.
  - `data_cleaning_process.py`: Script for cleaning and preprocessing waste data.

- **dashboard/**: Contains Power BI dashboard files.
  - `Evreka_Data_Engineer_Assessment.pbix`: Power BI dashboard to visualize waste data insights.

- **data/**: Stores datasets and processed data.
  - **output_pbi/**: Outputs used in Power BI dashboard.
    - `daily_avg_fullness.csv`: Contains daily average fullness metrics.
    - `location_fullness.csv`: Fullness data by location.
    - `peak_collection_times.csv`: Times of peak waste collection.
  - **waste_data_timeseries/**: Raw time-series data related to waste.
    - `location_data.csv`: Location metadata.
    - `waste_data_timeseries.csv`: Time-series waste data.
    - `README.md`: Detailed description of data fields and usage.

- **notebook/**: Jupyter notebook for data analysis.
  - `Evreka_Data_Engineer_PowerBI_Assessment.ipynb`: Notebook used for analyzing and preparing data for the Power BI dashboard.

## Usage

1. **Data Cleaning**: Run `data_cleaning_process.py` for preprocessing waste data before analysis.
2. **Dashboard**: Open `Evreka_Data_Engineer_Assessment.pbix` in Power BI for visualizing insights.
3. **Notebook**: Use `Evreka_Data_Engineer_PowerBI_Assessment.ipynb` to explore and analyze data.

