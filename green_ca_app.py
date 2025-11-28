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
# We have restored special characters like '%' and '&' here because
# the TRAINED MODEL likely expects these specific strings.
columns = [
    'Exp_biodiversity_landscape_protection_%GDP',  # Restored %
    'Exp_environment_protection__GDP', 
    'Exp_environmental_protection_NEC__GDP', 
    'Exp_on_environmental_protection_R&D__GDP',    # Restored &
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
st.write("Please provide the following information (ranges are shown in parentheses):")

# --- 5. Get user input ---
# Added (Min: X, Max: Y) to every label for clarity.

Exp_biodiversity_landscape_protection__GDP = st.number_input(
    "Exp_biodiversity_landscape_protection_%GDP (Min: 0.0, Max: 1.1)", 
    min_value=0.0, max_value=1.1
)

Exp_environment_protection__GDP = st.number_input(
    "Exp_environment_protection__GDP (Min: 0.0, Max: 4.0)", 
    min_value=0.0, max_value=4.0
)

Exp_environmental_protection_NEC__GDP = st.number_input(
    "Exp_environmental_protection_NEC__GDP (Min: -0.4, Max: 3.0)", 
    min_value=-0.4, max_value=3.0
)

Exp_on_environmental_protection_R_and_D__GDP = st.number_input(
    "Exp_on_environmental_protection_R&D__GDP (Min: 0.0, Max: 0.01)", 
    min_value=0.0, max_value=0.01, format="%.4f"
)

Exp_pollution_abatement__GDP = st.number_input(
    "Exp_pollution_abatement__GDP (Min: 0.0, Max: 0.7)", 
    min_value=0.0, max_value=0.7
)

Exp_waste_management__GDP = st.number_input(
    "Exp_waste_management__GDP (Min: 0.0, Max: 0.8)", 
    min_value=0.0, max_value=0.8
)

Exp_waste_water_management__GDP = st.number_input(
    "Exp_waste_water_management__GDP (Min: -0.1, Max: 0.6)", 
    min_value=-0.1, max_value=0.6
)

Environmental_Taxes__GDP = st.number_input(
    "Environmental_Taxes__GDP (Min: 0.0, Max: 5.0)", 
    min_value=0.0, max_value=5.0
)

Taxes_Energy__GDP = st.number_input(
    "Taxes_Energy__GDP (Min: 0.0, Max: 4.0)", 
    min_value=0.0, max_value=4.0
)

Taxes_Pollution__GDP = st.number_input(
    "Taxes_Pollution__GDP (Min: 0.0, Max: 0.4)", 
    min_value=0.0, max_value=0.4
)

Taxes_Resources__GDP = st.number_input(
    "Taxes_Resources__GDP (Min: 0.0, Max: 5.0)", 
    min_value=0.0, max_value=5.0
)

Taxes_Transport__GDP = st.number_input(
    "Taxes_Transport__GDP (Min: 0.0, Max: 1.7)", 
    min_value=0.0, max_value=1.7
)

Carbon_stocks_forests_MT = st.number_input(
    "Carbon_stocks_forests_MT (Min: 0.0, Max: 52021.0)", 
    min_value=0.0, max_value=52021.0
)

Index_carbon_stocks_forests = st.number_input(
    "Index_carbon_stocks_forests (Min: 62.0, Max: 343.0)", 
    min_value=62.0, max_value=343.0
)

Index_forest_extent = st.number_input(
    "Index_forest_extent (Min: 66.0, Max: 280.0)", 
    min_value=66.0, max_value=280.0
)

Land_area_1000HA = st.number_input(
    "Land_area_1000HA (Min: 6.0, Max: 1638000.0)", 
    min_value=6.0, max_value=1638000.0
)

Share_forest_area__ = st.number_input(
    "Share_forest_area__ (Min: 0.0, Max: 93.03)", 
    min_value=0.0, max_value=93.03
)

Implicit_Fossil_Fuel_Subsidies__GDP = st.number_input(
    "Implicit Fossil_Fuel_Subsidies__GDP (Min: 0.13, Max: 21.0)", 
    min_value=0.13, max_value=21.0
)

Explicit_Fossil_Fuel_Subsidies__GDP = st.number_input(
    "Explicit_Fossil_Fuel_Subsidies__GDP (Min: 0.0, Max: 9.7)", 
    min_value=0.0, max_value=9.7
)

Renewable_Electricity_Generation_GWh = st.number_input(
    "Renewable_Electricity_Generation_GWh (Min: 2.3, Max: 515000.0)", 
    min_value=2.3, max_value=515000.0
)

Non_Renewable_Electricity_Generation_GWh = st.number_input(
    "Non-Renewable_Electricity_Generation_GWh (Min: 0.0, Max: 734500.0)", 
    min_value=0.0, max_value=734500.0
)

# --- 6. Create a dataframe with the user input ---
# MAPPING: Map the clean Python variables (values) to the DIRTY/ORIGINAL column names (keys)
# This ensures the model receives the exact strings it was trained on (e.g., with "R&D" and "%").
input_data_dict = {
    'Exp_biodiversity_landscape_protection_%GDP': Exp_biodiversity_landscape_protection__GDP, # Key restored to %
    'Exp_environment_protection__GDP': Exp_environment_protection__GDP,
    'Exp_environmental_protection_NEC__GDP': Exp_environmental_protection_NEC__GDP,
    'Exp_on_environmental_protection_R&D__GDP': Exp_on_environmental_protection_R_and_D__GDP, # Key restored to &
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
    'Implicit Fossil_Fuel_Subsidies__GDP': Implicit_Fossil_Fuel_Subsidies__GDP,
    'Explicit_Fossil_Fuel_Subsidies__GDP': Explicit_Fossil_Fuel_Subsidies__GDP,
    'Renewable_Electricity_Generation_GWh': Renewable_Electricity_Generation_GWh,
    'Non-Renewable_Electricity_Generation_GWh': Non_Renewable_Electricity_Generation_GWh
}

# Create DataFrame
input_df = pd.DataFrame([input_data_dict])

# Ensure columns are in the exact order the model expects
# If 'columns' list above has typos, this line will filter out data, so we double-check.
try:
    input_df = input_df[columns]
except KeyError as e:
    st.error(f"Key Error: The code is trying to find a column that doesn't exist in the dictionary. Details: {e}")
    st.stop()

# --- 7. Make a prediction ---
if st.button("Predict Comparative Advantage"):
    try:
        prediction = predict_comparative_advantage(input_df)
        
        st.subheader("Result:")
        if prediction[0] == 0:
            st.error("Low Comparative Advantage (0)")
        else:
            st.success("High Comparative Advantage (1)")
            
    except ValueError as e:
        # This catches the specific error you were seeing (feature mismatch)
        st.error("Error: Feature Name Mismatch.")
        st.write("The model expects specific column names that don't match the inputs.")
        st.write(f"Technical details: {e}")
        
        # DEBUG HELPER: Print what the model actually wants
        if hasattr(loaded_model, 'feature_names_in_'):
            st.warning("The model was trained with these exact feature names. Please verify your code uses these:")
            st.write(loaded_model.feature_names_in_)
