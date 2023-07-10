from src.data_management import load_house_prices_data
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")


def page_sale_price_study_body():

    # load data
    df = load_house_prices_data()

    # hard copied from correlation study notebook
    relevant_variables = ['OverallQual', 'GrLivArea',
                          'GarageArea', 'TotalBsmtSF', '1stFlrSF', 'YearBuilt']

    st.write("### House Sale Prices Study")

    st.info(
        f"#### Business Requirement 1\n"
        f"* The client is interested in discovering how the house "
        f"attributes correlate with the sale price. Therefore, the "
        f"client expects data visualizations of the correlated "
        f"variables against the sale price to show that."
    )

    # inspect data
    if st.checkbox("Inspect House Prices Dataset"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"find below the first 10 rows.")

        st.write(df.head(10))

    st.write("---")

    # Correlation Study Summary
    st.write(
        f"* A correlation study was conducted in the notebook to better "
        f"understand how the variables are correlated to `SalePrice`.\n\n"
        f"The most correlated variables are: **{relevant_variables}**"
    )

    # Text based on "Sale Price Study" notebook - "Conclusions" section
    st.info(
        f" Based on the analysis of the correlation coefficients and "
        f"examination of the corresponding plots, it is indicated that:\n\n "
        f"* OverallQual: Higher overall quality ratings are associated with "
        f"higher sale prices.\n"
        f"* GrLivArea: Larger above ground living areas correspond to higher "
        f"sale prices.\n"
        f"* GarageArea: Houses with larger garage areas tend to have higher "
        f"sale prices.\n"
        f"* TotalBsmtSF: Houses with larger basement areas tend to have higher"
        f" sale prices.\n"
        f"* YearBuilt: Newer houses command higher prices compared to older"
        f" ones.\n"
        f"* 1ndFlrSF: Houses with larger first floor areas tend to have higher"
        f" sale prices.\n"
    )

    st.write(
        f"* Scatter plots showing correlation between each variable and the "
        f"'SalePrice':"
    )

    # Copied from "Sale Price Study" notebook - "EDA on selected variables"
    df_eda = df.filter(relevant_variables + ['SalePrice'])

    # Individual plots per variable
    if st.checkbox("Sale Price Correlation Per Variable"):
        sale_price_per_variable(df_eda, relevant_variables)

    st.write(
        f"* Heatmap showing the correlation between the relevant variables: "
    )

    # Plotting Heatmap
    if st.checkbox("Show Correlation Heatmap"):
        plot_heatmap(df_eda, relevant_variables)

    st.write(
        f"**Finding:**\n\n"
        f"Based on correlation and plot analysis, the following observations"
        f" have been made to address the first business question regarding the"
        f"  correlation between house attributes and the typical Sale Price:\n"
        f"* The *Sale Price* of a house tends to be higher for properties"
        f" with certain attributes. \n"
        f"* *Overall Quality* of the house has the strongest "
        f"correlation with Sale Price, indicating that houses with higher "
        f"quality generally command higher prices. \n"
        f"* Variables such as *Above Ground Living Area*, *Garage Area*, "
        f"*Total Basement Square Footage*, and *First Floor Square "
        f"Footage* also show strong positive correlations with"
        f" *Sale Price.* \n"
        f"* Other variables, such as *Year Built*, exhibit moderate "
        f"positive correlations with *Sale Price*."
    )


# Iterate over each relevant variable and plot its relationship with SalePrice
def sale_price_per_variable(df_eda, relevant_variables):
    target_var = 'SalePrice'
    for col in relevant_variables:
        plot_numerical(df_eda, col, target_var)
        st.write("\n\n")


# function created using "Sale Price Study" notebook - "Analyzing Correlations"
def plot_numerical(df_eda, col, target_var):

    fig = plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df_eda, x=col, y='SalePrice')
    plt.title(f"{col} vs SalePrice", fontsize=20, y=1.05)
    plt.xlabel(col)
    plt.ylabel('SalePrice')
    st.pyplot(fig)  # Display the matplotlib plot using Streamlit


def plot_heatmap(df_eda, relevant_variables):

    # Create a new DataFrame with the selected variables
    heatmap_vars = df_eda.copy()

    # Calculate the correlation matrix
    correlation_matrix = heatmap_vars.corr()

    # Plot the heat map
    fig = plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', square=True)
    plt.title("Correlation Matrix", fontsize=20)
    st.pyplot(fig)
