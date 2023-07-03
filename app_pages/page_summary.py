import streamlit as st


def page_summary_body():

    st.write("### Quick Project Summary\n")

    st.write(
        f"This project is an ML app specifically developed for the "
        f"visualization and prediction of house prices in Ames, Iowa.\n\n"
        f"The app offers users the following functionalities:\n"
        f"* **Correlation Analysis:** The application allows users to identify"
        f" the correlation between house attributes and the sale price.\n"
        f"* **Sale Price Prediction:** The application provides a predictive "
        f"model that enables users to obtain accurate estimates for "
        f"the sale price.\n"
    )

    # text based on README file - "Dataset Content" section
    st.info(
        f"**Project Terms & Jargons**\n"
        f" * **Variables**: Refers to the different attributes of a house, "
        f"such as floor area, basement and garage.\n"
        f" * **Target Variable**: The target variable in this study is the "
        f"'SalePrice'. It represents the price at which a house was sold.\n\n"

        f"**Project Dataset**\n"
        f"* The dataset consists of properties that were sold in Ames, Iowa. "
        f"It contains details about 24 distinct features for each property,"
        f"which have the potential to impact the price. These features "
        f"encompass various aspects of the houses, including floor area, "
        f"basement, garage, kitchen and year built. We utilize this dataset "
        f"to conduct our study on correlated features, train our machine "
        f"learning model, and subsequently predict the sale prices of "
        f"properties in the area.\n"
        f"* The dataset encompasses houses constructed from 1872 to 2010, and "
        f"it has been obtained from "
        f"[Kaggle](https://www.kaggle.com/datasets/codeinstitute/"
        "housing-prices-data)"
        f".\n\n"
    )

    # Link to README file, users can have access to full project documentation
    st.write(
        f"For additional information, please visit and **read** the "
        f"**[Project's README file](https://github.com/Imangnp/"
        "heritage-housing-issues)**."
    )

    # copied from README file - "Business Requirements" section
    st.success(
        f"** The project has 2 business requirements:** \n \n "
        f"**1.** The client is interested in discovering how the house"
        f"attributes correlate with the sale price. Therefore, the client "
        f"expects data visualisations of the correlated variables against "
        f"the sale price to show that. \n\n "
        f"**2.** The client is interested in predicting the house sale price "
        f"from her four inherited houses and any other house in Ames, Iowa.")
