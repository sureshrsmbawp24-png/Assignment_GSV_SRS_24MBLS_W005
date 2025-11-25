import streamlit as st
import pandas as pd
import pickle
import os

# --- 1. Load the trained model ---
# Added error handling in case the file is missing
filename = 'greencalogistic_regression_model.pkl'

try:
    with open(filename, 'rb') as file:
        loaded_model = pickle.load(file)
except FileNotFoundError:
    st.error(f"Error: The file '{filename}' was not found. Please ensure it is in the same directory as this script.")
    st.stop()

# --- 2. Define the exact column names expected by the model ---
# Note: These strings CAN have spaces/hyphens, but the variables we create later CANNOT.
columns = [
    'Exp_biodiversity_landscape_protection__GDP', 
    'Exp_environment_protection__GDP', 
    'Exp_environmental_protection_NEC__GDP', 
    'Exp_on_environmental_protection_R_and_D__GDP', 
    'Exp_pollution_abatement__GDP', 
    'Exp_waste_management__GDP', 
    'Exp_waste_water_management__GDP', 
    'Environmental_Taxes__GDP', 
    'Taxes_Energy__GDP', 
    'Taxes_Pollution__GDP', 
    'Taxes_Resources__GDP', 
    'Taxes_Transport__GDP', 
    'Carbon_stocks_forests_MT', 
    'Index_carbon_stocks_forests', 
    'Index_forest_extent', 
    'Land_area_1000HA', 
    'Share_forest_area__', 
    'Implicit Fossil_Fuel_Subsidies__GDP', 
    'Explicit_Fossil_Fuel_Subsidies__GDP', 
    'Renewable_Electricity_Generation_GWh', 
    'Non-Renewable_Electricity_Generation_GWh'
]

# --- 3. Define the prediction function ---
def predict_comparative_advantage(features):
    """
    Predicts the comparative_advantage based on input features.
    """
    prediction = loaded_model.predict(features)
    return prediction

# --- 4. Create the Streamlit app ---
st.title("Low Carbon Tech Comparative Advantage Prediction")
st.write("Please provide the following information:")

# --- 5. Get user input ---
# Note: Variable names use underscores (_) but labels can use spaces.
# We use 0.0 (floats) for min/max to ensure consistency.

Exp_biodiversity_landscape_protection__GDP = st.number_input("Exp_biodiversity_landscape_protection__GDP", min_value=0.0, max_value=1.1)
Exp_environment_protection__GDP = st.number_input("Exp_environment_protection__GDP", min_value=0.0, max_value=4.0)
Exp_environmental_protection_NEC__GDP = st.number_input("Exp_environmental_protection_NEC__GDP", min_value=-0.4, max_value=3.0)
Exp_on_environmental_protection_R_and_D__GDP = st.number_input("Exp_on_environmental_protection_R_and_D__GDP", min_value=0.0, max_value=0.01, format="%.4f")
Exp_pollution_abatement__GDP = st.number_input("Exp_pollution_abatement__GDP", min_value=0.0, max_value=0.7)
Exp_waste_management__GDP = st.number_input("Exp_waste_management__GDP", min_value=0.0, max_value=0.8)
Exp_waste_water_management__GDP = st.number_input("Exp_waste_water_management__GDP", min_value=-0.1, max_value=0.6)
Environmental_Taxes__GDP = st.number_input("Environmental_Taxes__GDP", min_value=0.0, max_value=5.0)
Taxes_Energy__GDP = st.number_input("Taxes_Energy__GDP", min_value=0.0, max_value=4.0)
Taxes_Pollution__GDP = st.number_input("Taxes_Pollution__GDP", min_value=0.0, max_value=0.4)
Taxes_Resources__GDP = st.number_input("Taxes_Resources__GDP", min_value=0.0, max_value=5.0)
Taxes_Transport__GDP = st.number_input("Taxes_Transport__GDP", min_value=0.0, max_value=1.7)
Carbon_stocks_forests_MT = st.number_input("Carbon_stocks_forests_MT", min_value=0.0, max_value=52021.0)
Index_carbon_stocks_forests = st.number_input("Index_carbon_stocks_forests", min_value=62.0, max_value=343.0)
Index_forest_extent = st.number_input("Index_forest_extent", min_value=66.0, max_value=280.0)
Land_area_1000HA = st.number_input("Land_area_1000HA", min_value=6.0, max_value=1638000.0)

# Fixed Label here (was duplicate of Exp_environment...)
Share_forest_area__ = st.number_input("Share_forest_area__", min_value=0.0, max_value=93.03)

# Fixed Variable Syntax: Removed spaces and double commas
Implicit_Fossil_Fuel_Subsidies__GDP = st.number_input("Implicit Fossil_Fuel_Subsidies__GDP", min_value=0.13, max_value=21.0)

Explicit_Fossil_Fuel_Subsidies__GDP = st.number_input("Explicit_Fossil_Fuel_Subsidies__GDP", min_value=0.0, max_value=9.7)
Renewable_Electricity_Generation_GWh = st.number_input("Renewable_Electricity_Generation_GWh", min_value=2.3, max_value=515000.0)

# Fixed Variable Syntax: Changed '-' to '_' in variable name (Python interprets - as minus)
Non_Renewable_Electricity_Generation_GWh = st.number_input("Non-Renewable_Electricity_Generation_GWh", min_value=0.0, max_value=734500.0)

# --- 6. Create a dataframe with the user input ---
# CRITICAL FIX: passed the variables (values), not the strings (names)
input_data_dict = {
    'Exp_biodiversity_landscape_protection__GDP': Exp_biodiversity_landscape_protection__GDP,
    'Exp_environment_protection__GDP': Exp_environment_protection__GDP,
    'Exp_environmental_protection_NEC__GDP': Exp_environmental_protection_NEC__GDP,
    'Exp_on_environmental_protection_R_and_D__GDP': Exp_on_environmental_protection_R_and_D__GDP,
    'Exp_pollution_abatement__GDP': Exp_pollution_abatement__GDP,
    'Exp_waste_management__GDP': Exp_waste_management__GDP,
    'Exp_waste_water_management__GDP': Exp_waste_water_management__GDP,
    'Environmental_Taxes__GDP': Environmental_Taxes__GDP,
    'Taxes_Energy__GDP': Taxes_Energy__GDP,
    'Taxes_Pollution__GDP': Taxes_Pollution__GDP,
    'Taxes_Resources__GDP': Taxes_Resources__GDP,
    'Taxes_Transport__GDP': Taxes_Transport__GDP,
    'Carbon_stocks_forests_MT': Carbon_stocks_forests_MT,
    'Index_carbon_stocks_forests': Index_carbon_stocks_forests,
    'Index_forest_extent': Index_forest_extent,
    'Land_area_1000HA': Land_area_1000HA,
    'Share_forest_area__': Share_forest_area__,
    'Implicit Fossil_Fuel_Subsidies__GDP': Implicit_Fossil_Fuel_Subsidies__GDP, # Mapped correctly to original column name
    'Explicit_Fossil_Fuel_Subsidies__GDP': Explicit_Fossil_Fuel_Subsidies__GDP,
    'Renewable_Electricity_Generation_GWh': Renewable_Electricity_Generation_GWh,
    'Non-Renewable_Electricity_Generation_GWh': Non_Renewable_Electricity_Generation_GWh # Mapped correctly to original column name
}

# Create DataFrame using the dictionary to ensure order and values are correct
input_df = pd.DataFrame([input_data_dict])

# Ensure columns are in the exact order the model expects
input_df = input_df[columns]

# --- 7. Make a prediction ---
if st.button("Predict Comparative Advantage"):
    prediction = predict_comparative_advantage(input_df)
    
    st.subheader("Result:")
    if prediction[0] == 0:
        st.error("Low Comparative Advantage (0)")
    else:
        st.success("High Comparative Advantage (1)")
