import streamlit as st
from app_pages.multi_pages import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_sale_price_study import page_sale_price_study_body
from app_pages.page_predict_price import page_predict_price_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_ml_predict import page_ml_predict_body

app = MultiPage(app_name="Heritage Housing")  # Create an instance of the app

# Add app pages using .add_page()
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("House Sale Prices Study", page_sale_price_study_body)
app.add_page("Predict House Sale Price", page_predict_price_body)
app.add_page("Project Hypothesis", page_project_hypothesis_body)
app.add_page("ML: Predict Sale Price", page_ml_predict_body)

app.run()  # Run the app
