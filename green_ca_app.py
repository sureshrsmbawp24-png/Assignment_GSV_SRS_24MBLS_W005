import streamlit as st
import pandas as pd
import pickle

# Load the trained model
filename = r'greencalogistic_regression_model.pkl'
loaded_model = pickle.load(open(filename, 'rb'))

# Define the correct column names
columns = ['Exp_biodiversity_landscape_protection__GDP', 'Exp_environment_protection__GDP', 'Exp_environmental_protection_NEC__GDP', 'Exp_on_environmental_protection_R_and_D__GDP', 'Exp_pollution_abatement__GDP', 'Exp_waste_management__GDP', 'Exp_waste_water_management__GDP', 'Environmental_Taxes__GDP', 'Taxes_Energy__GDP', 'Taxes_Pollution__GDP', 'Taxes_Resources__GDP', 'Taxes_Transport__GDP', 'Carbon_stocks_forests_MT', 'Index_carbon_stocks_forests', 'Index_forest_extent', 'Land_area_1000HA', 'Share_forest_area__', 'Implicit Fossil_Fuel_Subsidies__GDP', 'Explicit_Fossil_Fuel_Subsidies__GDP', 'Renewable_Electricity_Generation_GWh', 'Non-Renewable_Electricity_Generation_GWh']

# Define the prediction function
def predict_comparative_advantage_in_exporting_low_carbon_technologies(features):
    """
    Predicts the comparative_advantage based on input features.
    """
    prediction = loaded_model.predict(features)
    return prediction

# Create the Streamlit app
st.title("comparative_advantage_in_exporting_low_carbon_technologies_Prediction")

# Get user input
st.write("Please provide the following information:")
Exp_biodiversity_landscape_protection__GDP = st.number_input("Exp_biodiversity_landscape_protection__GDP", min_value=0.0, max_value=1.1)
Exp_environment_protection__GDP = st.number_input("Exp_environment_protection__GDP", min_value=0, max_value=4)
Exp_environmental_protection_NEC__GDP = st.number_input("Exp_environmental_protection_NEC__GDP", min_value=-0.4, max_value=3)
Exp_on_environmental_protection_R_and_D__GDP = st.number_input("Exp_on_environmental_protection_R_and_D__GDP", min_value=0, max_value=0.01)
Exp_pollution_abatement__GDP = st.number_input("Exp_pollution_abatement__GDP", min_value=0, max_value=0.7)
Exp_waste_management__GDP = st.number_input("Exp_waste_management__GDP", min_value=0, max_value=0.8)
Exp_waste_water_management__GDP = st.number_input("Exp_waste_water_management__GDP", min_value=-0.1, max_value=0.6)
Environmental_Taxes__GDP = st.number_input("Environmental_Taxes__GDP", min_value=0, max_value=5)
Taxes_Energy__GDP = st.number_input("Taxes_Energy__GDP", min_value=0, max_value=4)
Taxes_Pollution__GDP = st.number_input("Taxes_Pollution__GDP", min_value=0, max_value=0.4)
Taxes_Resources__GDP = st.number_input("Taxes_Resources__GDP", min_value=0, max_value=5)
Taxes_Transport__GDP = st.number_input("Taxes_Transport__GDP", min_value=0, max_value=1.7)
Carbon_stocks_forests_MT = st.number_input("Carbon_stocks_forests_MT", min_value=0, max_value=52021)
Index_carbon_stocks_forests = st.number_input("Index_carbon_stocks_forests", min_value=62, max_value=343)
Index_forest_extent = st.number_input("Index_forest_extent", min_value=66, max_value=280)
Land_area_1000HA = st.number_input("Land_area_1000HA", min_value=6, max_value=1638000)
Share_forest_area__ = st.number_input("Exp_environment_protection__GDP", min_value=0, max_value=93.03)
Implicit Fossil_Fuel_Subsidies__GDP = st.number_input("Implicit Fossil_Fuel_Subsidies__GDP", min_value=0.13, , max_value=21)
Explicit_Fossil_Fuel_Subsidies__GDP = st.number_input("Explicit_Fossil_Fuel_Subsidies__GDP", min_value=0, max_value=9.7)
Renewable_Electricity_Generation_GWh = st.number_input("Renewable_Electricity_Generation_GWh", min_value=2.3, max_value=515000)
Non-Renewable_Electricity_Generation_GWh = st.number_input("Non-Renewable_Electricity_Generation_GWh", min_value=0, max_value=734500)

# Create a dataframe with the user input
input_data = pd.DataFrame([['Exp_biodiversity_landscape_protection__GDP', 'Exp_environment_protection__GDP', 'Exp_environmental_protection_NEC__GDP', 'Exp_on_environmental_protection_R_and_D__GDP', 'Exp_pollution_abatement__GDP', 'Exp_waste_management__GDP', 'Exp_waste_water_management__GDP', 'Environmental_Taxes__GDP', 'Taxes_Energy__GDP', 'Taxes_Pollution__GDP', 'Taxes_Resources__GDP', 'Taxes_Transport__GDP', 'Carbon_stocks_forests_MT', 'Index_carbon_stocks_forests', 'Index_forest_extent', 'Land_area_1000HA', 'Share_forest_area__', 'Implicit Fossil_Fuel_Subsidies__GDP', 'Explicit_Fossil_Fuel_Subsidies__GDP', 'Renewable_Electricity_Generation_GWh', 'Non-Renewable_Electricity_Generation_GWh']], columns=columns)

# Make a prediction
# Make a prediction
if st.button("predict_comparative_advantage_in_exporting_low_carbon_technologies"):
    prediction = predict_comparative_advantage_in_exporting_low_carbon_technologies(input_data)
    if prediction[0] == 0:
        st.write("Low comparative advantage: 0 (Low comparative advantage)")
    else:
        st.write("high comparative advantage: 1 (High comparative advantage)")
