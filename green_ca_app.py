import streamlit as st
import pandas as pd
import pickle
import os

# --- 1. Load the trained model ---
filename = 'greencalogistic_regression_model.pkl'

try:
    with open(filename, 'rb') as file:
        loaded_model = pickle.load(file)
except FileNotFoundError:
    st.error(f"Error: The file '{filename}' was not found. Please ensure it is in the same directory as this script.")
    st.stop()

# --- 2. Define the descriptive column names (for mapping inputs) ---
# This list defines the keys used in input_data_dict and ensures the correct order.
descriptive_columns = [
    'Exp_biodiversity_landscape_protection_%GDP',
    'Exp_environment_protection__GDP', 
    'Exp_environmental_protection_NEC__GDP', 
    'Exp_on_environmental_protection_R&D__GDP',
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

# --- 3. Define the ID column names (as expected by the model) ---
# This list must match the order of the descriptive_columns list above, 
# based on the table provided in the user's image.
model_feature_ids = [
    'EP_0',  # Exp_biodiversity_landscape_protection_%GDP
    'EP_1',  # Exp_environment_protection__GDP
    'EP_2',  # Exp_environmental_protection_NEC__GDP
    'EP_3',  # Exp_on_environmental_protection_R&D__GDP
    'EP_4',  # Exp_pollution_abatement__GDP
    'EP_5',  # Exp_waste_management__GDP
    'EP_6',  # Exp_waste_water_management__GDP
    'ET_0',  # Environmental_Taxes__GDP
    'ET_1',  # Taxes_Energy__GDP
    'ET_2',  # Taxes_Pollution__GDP
    'ET_3',  # Taxes_Resources__GDP
    'ET_4',  # Taxes_Transport__GDP
    'FC_0',  # Carbon_stocks_forests_MT
    'FC_2',  # Index_carbon_stocks_forests
    'FC_3',  # Index_forest_extent
    'FC_4',  # Land_area_1000HA
    'FC_5',  # Share_forest_area__
    'FF_0',  # Implicit Fossil_Fuel_Subsidies__GDP
    'FF_1',  # Explicit_Fossil_Fuel_Subsidies__GDP
    'RE_0_0',  # Renewable_Electricity_Generation_GWh
    'RE_0_1'   # Non-Renewable_Electricity_Generation_GWh
]


# --- 4. Define the prediction function (now simpler) ---
def predict_comparative_advantage(features):
    """
    Predicts the comparative_advantage based on input features.
    """
    # The columns are already renamed outside this function, making this call safe.
    prediction = loaded_model.predict(features)
    return prediction

# --- 5. Create the Streamlit app ---
st.title("Low Carbon Tech Comparative Advantage Prediction")
st.write("Please provide the following information (ranges are shown in parentheses):")

# --- 6. Get user input (Variable names are clean, labels show ranges) ---

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

# --- 7. Create and prepare DataFrame for model ---
# MAPPING: Map the clean Python variables (values) to the DESCRIPTIVE column names (keys)
input_data_dict = {
    'Exp_biodiversity_landscape_protection_%GDP': Exp_biodiversity_landscape_protection__GDP,
    'Exp_environment_protection__GDP': Exp_environment_protection__GDP,
    'Exp_environmental_protection_NEC__GDP': Exp_environmental_protection_NEC__GDP,
    'Exp_on_environmental_protection_R&D__GDP': Exp_on_environmental_protection_R_and_D__GDP,
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

# Create DataFrame and ensure the order matches the model_feature_ids list
input_df = pd.DataFrame([input_data_dict])

# CRITICAL FIX: Reorder the DataFrame columns using the descriptive names list
try:
    input_df = input_df[descriptive_columns]
except KeyError as e:
    st.error(f"Internal Error: A descriptive column name is incorrect. Details: {e}")
    st.stop()

# CRITICAL FIX: Rename the columns to the short IDs the model expects
input_df.columns = model_feature_ids


# --- 8. Make a prediction ---
if st.button("Predict Comparative Advantage"):
    try:
        prediction = predict_comparative_advantage(input_df)
        
        st.subheader("Result:")
        if prediction[0] == 0:
            st.error("Low Comparative Advantage (0)")
        else:
            st.success("High Comparative Advantage (1)")
            
    except ValueError as e:
        st.error("Error: An unexpected error occurred during prediction. Check the data inputs.")
        st.write(f"Technical details: {e}")
