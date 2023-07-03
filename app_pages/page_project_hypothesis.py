import streamlit as st


def page_project_hypothesis_body():

    st.write("### Project Hypothesis")

    st.info(
        f"Based on our comprehensive data analysis, where we examined various "
        f" variables and conducted correlation studies,"
        f"we have found strong evidence supporting the following hypotheses:"
    )

    # conclusions taken from "02 - Sale Price Study" notebook
    st.success(
        f"**Hypothesis 1**: The quality of the house has a significant "
        f"impact on its sale price.\n"
        f" * Both Pearson (0.791) and Spearman (0.810) correlation methods "
        f"reveal a substantial positive correlation between the overall "
        f"quality of the house (OverallQual) and its sale price. This"
        f" suggests that houses with higher quality ratings tend to "
        f"command higher prices.\n\n"

        f"**Hypothesis 2**: The year of construction affects the sale "
        f" price of a property. \n"
        f"* The year of construction (YearBuilt) shows a moderate positive "
        f"correlation with the sale price. Pearson correlation coefficient "
        f"(0.523) suggests that more recently built houses tend to have "
        f"higher prices.\n\n"

        f"**Hypothesis 3**: The size of the house influences its sale price.\n"
        f"* Variables such as ground living area (GrLivArea), garage area "
        f"(GarageArea), total basement square footage (TotalBsmtSF),"
        f" and first floor square footage (1stFlrSF) exhibit strong positive "
        f"correlations with the sale price. The Pearson correlation "
        f"coefficients for these variables range from 0.605 to 0.709, "
        f"indicating that larger houses tend to have higher sale prices."
    )

    st.info(
        f"**Key Findings**: Factors Influencing Houses Prices\n\n"
        f"Overall, by analyzing these correlations and considering the top "
        f"correlated variables, we have confirmed our hypotheses that the "
        f"quality of the house and the size of the property play significant "
        f"roles in determining the sale price. Additionally, newer houses tend"
        f" to command higher prices compared to older ones. The correlation "
        f"coefficients and visualizations provide robust evidence to support"
        f" these findings."
    )