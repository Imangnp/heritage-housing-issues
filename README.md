# Heritage Housing Issues

The Heritage Housing Issue project is a machine learning application designed to analyze historical data and relevant features to visualize and predict house prices in Ames, Iowa. The project follows a structured workflow, including data collection, data preparation, model training, and evaluation.

You can find the live link here: [Heritage Housing Issues](https://)

![Responsive](media/responsive.png)

---

# Table of contents

- [Dataset Content](#dataset-content)
- [Project Terms and Jargons](#project-terms-and-jargons)
- [Business Requirements](#business-requirements)
- [Project hypothesis and validation](#project-hypothesis-and-validation)
- [User Stories](#user-stories)
- [Rationale to map the business requirements to the Data Visualizations and ML tasks](#rationale-to-map-the-business-requirements-to-the-data-visualizations-and-ml-tasks)
- [ML Business Case](#ml-business-case)
- [Dashboard Design](#dashboard-design)
- [Unfixed Bugs](#unfixed-bugs)
- [Deployment to Heroku](#deployment-to-heroku)
- [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
- [Credits](#credits)

---

# Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace. 
* The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa, indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second-floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|


# Project Terms and Jargons
  - **Variables**: Refers to the different attributes of a house, such as floor area, basement and garage.
  - **Target Variable**: The target variable in this study is the 'SalePrice'. It represents the price at which a house was sold.


# Business Requirements
As a good friend, you are requested by your friend, who has received an inheritance from a deceased great-grandfather located in Ames, Iowa, to  help in maximising the sales price for the inherited properties.

Although your friend has an excellent understanding of property prices in her own state and residential area, she fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa. She found a public dataset with house prices for Ames, Iowa, and will provide you with that.

* 1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.
* 2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.


# Project hypothesis and validation
**Hypothesis 1**: The quality of the house has a significant impact on its sale price.
- Both Pearson (0.791) and Spearman (0.810) correlation methods reveal a substantial positive correlation between the overall quality of the house (OverallQual) and its sale price. This suggests that houses with higher quality ratings tend to command higher prices.

**Hypothesis 2**: The year of construction affects the sale price of a property.
- The year of construction (YearBuilt) shows a moderate positive correlation with the sale price. Pearson correlation coefficient (0.523) suggests that more recently built houses tend to have higher prices.

**Hypothesis 3**: The size of the house influences its sale price.
- Variables such as ground living area (GrLivArea), garage area (GarageArea), total basement square footage (TotalBsmtSF), and first floor square footage (1stFlrSF) exhibit strong positive correlations with the sale price. The Pearson correlation coefficients for these variables range from 0.605 to 0.709, indicating that larger houses tend to have higher sale prices.


# Rationale to map the business requirements to the Data Visualizations and ML tasks
* ### Business Requirement 1: Correlation Study and Data Visualization
  The client's objective is to gain insights into the factors influencing the sale price of houses.
  - Review and Inspect Dataset: In order to gain a comprehensive understanding of the dataset related to the houses, a thorough review and inspection of the data will be conducted.
  - Correlation Study: To understand how different variables relate to the "SalePrice" of houses, both Pearson and Spearman correlation coefficients will be calculated.
  - Select Most Correlated Variables: Based on the correlation study results, the most highly correlated variables with the "SalePrice" will be identified. These variables will be given priority for further analysis.
  - Data Visualization: Visualizations such as scatter plots, heatmaps, and pair plots will be used to to represent the correlations between each variable and the "SalePrice."
  - Hypothesis Validation: Findings from the correlation study and data visualizations will be used to validate hypotheses about the factors influencing house prices.

* ### Business Requirement 2: Predict House Prices
  The client's objective is to accurately predict house prices in Ames, Iowa. 
  - Data Cleaning and Feature Engineering: To prepare the data for the machine learning model, it is important to clean the data and perform feature engineering.
  - Regression Model Development: A regression model will be constructed using appropriate algorithms (random forest regression) to predict the sale price of houses.
  - Hyperparameter Tuning: To optimize the performance of the regression model, hyperparameters will be adjusted.
  - Regression Evaluation: The trained model will be evaluated using appropriate evaluation metrics such as R2 score (coefficient of determination) and Mean Absolute Error (MAE).
  - Predict house prices: Once the model is trained and evaluated, it can be utilized to predict the prices of four inherited houses and any other house in Ames, Iowa.


## ML Business Case
* In the previous bullet, you potentially visualised an ML task to answer a business requirement. You should frame the business case using the method we covered in the course.


## Dashboard Design
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items that your dashboard library supports.
* Eventually, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but eventually you needed to use another plot type)



## Unfixed Bugs
* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not valid reason to leave bugs unfixed.

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries you used in the project and provide example(s) of how you used these libraries.


## Credits 

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open Source site
- The images used for the gallery page were taken from this other open-source site



## Acknowledgements (optional)
* In case you would like to thank the people that provided support through this project.

---

![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)