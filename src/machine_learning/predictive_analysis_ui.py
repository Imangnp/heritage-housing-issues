import streamlit as st

# The following function is adapted from Code Institute - Churnometer Project.


def predict_sale_price(X_live, best_features, pipeline):
    # from live data, subset features related to this pipeline
    X_live_sale_price = X_live.filter(best_features)

    # predict
    sale_price_prediction = pipeline.predict(X_live_sale_price)

    sale_price_prediction = float(sale_price_prediction)
    sale_price = "$ {:.2f}".format(sale_price_prediction)

    # display the results
    statement = (
        f'The predicted sale price for the house based on the '
        f'provided feature values is: **{sale_price}**'
    )

    st.success(statement)
