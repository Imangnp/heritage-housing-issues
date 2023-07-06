import streamlit as st
import pandas as pd
from src.data_management import (
    load_house_prices_data,
    load_pkl_file,
    load_inherited_houses_data
)
from src.machine_learning.predictive_analysis_ui import predict_sale_price


def page_predict_price_body():

    # Load the necessary files to predict house prices
    version = 'v1'
    output_dir = "outputs/ml_pipeline/predict_sale_price"
    pipeline_path = f"{output_dir}/{version}/best_regressor_pipeline.pkl"
    X_train_path = f"{output_dir}/{version}/X_train.csv"

    df_inherited = load_inherited_houses_data()
    pipeline = load_pkl_file(pipeline_path)
    best_features = pd.read_csv(X_train_path).columns.to_list()

    st.write("### Predict House Sale Price")

    st.info(
        f"The client is interested in predicting the house sale price from "
        f"her four inherited houses and any other house in Ames, Iowa."
    )

    st.write(
        f"* The following table shows the features of four inherited houses."
    )

    # Display the data for the inherited houses
    st.write(df_inherited.head())
    df_inherited = df_inherited.filter(best_features)
    house_price_prediction = pipeline.predict(df_inherited).round(0)
    df_inherited['Predicted Sale Price'] = house_price_prediction

    st.write(
        f"* The table below displays the best features used for prediction and"
        f" the corresponding predicted sale prices for the four inherited"
        f" houses."
    )

    st.write(df_inherited.head())

    # calculate sum of inherited houses predicted prices
    sum_sale_prices = df_inherited['Predicted Sale Price'].sum()
    st.success(
        f"The total predicted sale price for all four houses is:  "
        f"**$ {sum_sale_prices}**\n"
    )

    st.write("---")

    # To predict the price of any other house located in Ames, Iowa
    st.write(
        f"### predict price of any other house in Ames, Iowa"
    )

    st.info(
        f"**A Tool for Predicting House Sale Prices**\n"
        f"* To calculate the predicted sale price of any house in Ames, Iowa, "
        f"you can simply input the relevant values and initiate the predictive"
        f" function by clicking the 'Predict Sale Price' button."
    )

    # Copied from Code Institute - Churnometer project
    # Generate Live Data
    X_live = DrawInputsWidgets()

    if st.button("Predict Sale Price"):
        predict_sale_price(X_live, best_features, pipeline)


# The following function is adapted from Code Institute - Churnometer Project.
def DrawInputsWidgets():

    # load data
    df = load_house_prices_data()
    percentageMin, percentageMax = 0.4, 2.0

    # Create input widgets for best features
    col1, col2, col3 = st.beta_columns(3)

    # create an empty DataFrame, which will be the live data
    X_live = pd.DataFrame([], index=[0])

    # draw the widget based on the variable type and set initial values

    with col1:
        feature = "GrLivArea"
        st_widget = st.number_input(
            label=feature,
            min_value=int(df[feature].min()*percentageMin),
            max_value=int(df[feature].max()*percentageMax),
            value=int(df[feature].median()),
            help="Above ground living area in square feet"
        )
        X_live[feature] = st_widget

    with col2:
        feature = "OverallQual"
        st_widget = st.number_input(
            label=feature,
            min_value=0,
            max_value=10,
            value=int(df[feature].median()),
            help="Overall Quality"
        )
        X_live[feature] = st_widget

    with col3:
        feature = "TotalBsmtSF"
        st_widget = st.number_input(
            label=feature,
            min_value=int(df[feature].min()*percentageMin),
            max_value=int(df[feature].max()*percentageMax),
            value=int(df[feature].median()),
            help="Total square feet of basement area"
        )
        X_live[feature] = st_widget

    return X_live
