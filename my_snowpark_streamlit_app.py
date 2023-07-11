# Import required libraries
from snowflake.snowpark.session import Session
from snowflake.snowpark.functions import avg, sum, col,lit
import streamlit as st
import pandas as pd

# Create Session object
def create_session_object():
   connection_parameters = {
      "account": "kd58148.AWS_US_EAST_2",
      "user": "annelie",
      "password": "@Hy1sHeer",
      "role": "ACCOUNTADMIN",
      "warehouse": "COMPUTE_WC",
      "database": "TOURISM_DATA_ATLAS",  #ENVIRONMENT_DATA_ATLAS
      "schema": "TOURISM"
   }
   session = Session.builder.configs(connection_parameters).create()
   return session

# Create Snowpark DataFrames that loads data from Knoema: Environmental Data Atlas
def load_data(session):
    # CO2 Emissions by Country
    snow_df_co2 = session.table("TOURISM.DATA_ATLAS").filter(col('Indicator') == 'Tourism expenditures')
    #snow_df_co2 = snow_df_co2.group_by('Location Name').agg(sum('$16').alias("Total CO2 Emissions")).filter(col('Location Name') != 'World').sort('Location Name')

    # Forest Occupied Land Area by Country
    #snow_df_land = session.table("ENVIRONMENT.\"WBWDI2019Jan\"").filter(col('Series Name') == 'Forest area (% of land area)')
    #snow_df_land = snow_df_land.group_by('Country Name').agg(sum('$61').alias("Total Share of Forest Land")).sort('Country Name')

    # Total Municipal Waste by Country
    #snow_df_waste = session.table("ENVIRONMENT.UNENVDB2018").filter(col('Variable Name') == 'Municipal waste collected')
    #snow_df_waste = snow_df_waste.group_by('Location Name').agg(sum('$12').alias("Total Municipal Waste")).sort('Location Name')

    # Convert Snowpark DataFrames to Pandas DataFrames for Streamlit
    pd_df_co2 = snow_df_co2.to_pandas()
    #pd_df_land = snow_df_land.to_pandas()
    #pd_df_waste = snow_df_waste.to_pandas()
