## Time-Series-Regression-Analysis-TSRA-Corporation-Favorita-

<a name="readme-top"></a>

<div align="center">
  <h1><b>Telco Churn </b></h1>
</div>

<!-- TABLE OF CONTENTS -->

# 📗 Table of Contents

- [📗 Table of Contents](#-table-of-contents)
- Overview
- [🛠 Built With ](#-built-with-)
- [Tech Stack ](#tech-stack-)
- Packages and Libraries
- Cleaning The Data
- Exploratory Data Analysis
- Visualizations
- Analysis
- Modelling
- Findings
- [Key Insights ](#key-insights-)
- [💻 Getting Started ](#-getting-started-)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Install](#install)
- [Usage](#usage)
- [👥 Authors ](#-authors-)
- [🔭 Future Features ](#-future-features-)
- [🤝 Contributing ](#-contributing-)
- [⭐️ Show your support ](#️-show-your-support-)
- [🙏 Acknowledgments ](#-acknowledgments-)
- [📝 License ](#-license-)

<!-- PROJECT DESCRIPTION -->

#  Analyzing Customer Behavior and Predicting Churn in the Telecommunication Firm <a name="about-project"></a>

## Overview 

Scenario: We are a data scientist working in Corporation Favorita, a large Ecuadorian-based grocery retailer. Corporation Favorita wants to ensure that they always have the right quantity of products in stock. To do this we have decided to build a series of machine learning models to forecast the demand of products in various locations. The marketing and sales team have provided us with some data to aid this endeavor. 
Thd team uses CRISP-DM Framework for Data Science projects

This is a time series regression analysis problem. In this project, we will predict store sales on data from Corporation Favorita, a large Ecuadorian-based grocery retailer.

Specifically, we are to build a model that more accurately predicts the unit sales for thousands of items sold at different Favorita stores.

The training data includes dates, store, and product information, whether that item was being promoted, as well as the sales numbers. Additional files include supplementary information that may be useful in building your models
## Data Sources 📊
- The dataset was provided in GitHub and SQL and was transformed to CSV format for transparency and reproductibility.
- Statistics on Time series regression.

## Topical Questions and Hypotheses
#### Questions 🤔:

ANALYTICAL QUESTIONS
The following analytical questions will help us gain insight and as well as confirm our hypothesis

1. Is the train dataset complete (has all the required dates)?

2. Which dates have the lowest and highest sales for each year (excluding days the store was closed)?

3. Compare the sales for each month across the years and determine which month of which year had the highest sales.

4. Did the earthquake impact sales?

5. Are certain stores or groups of stores selling more products? (Cluster, city, state, type)

6. Are sales affected by promotions, oil prices and holidays?

7. What analysis can we get from the date and its extractable features?

8. Which product family and stores did the promotions affect.

9. What is the difference between RMSLE, RMSE, MSE (or why is the MAE greater than all of them?)

10. Does the payment of wages in the public sector on the 15th and last days of the month influence the store sales.

### Hypotheses 🔬:
#### A significance level (α) of 5% will used to perform all the hypothesis testing

The following hypothesis will be tested

1. Products on promotions have higher or equal averages sales compared those that are not on promotion.

**File Descriptions and Data Field Information**

**train.csv**

-   The training data, comprising time series of features store_nbr, family, 
    and onpromotion as well as the target sales.

-   **store_nbr** identifies the store at which the products are sold.

-   **family** identifies the type of product sold.

-   **sales** gives the total sales for a product family at a particular store
    at a given date. Fractional values are possible since products can be sold in 
    fractional units (1.5 kg of cheese, for instance, as opposed to 1 bag of chips).

-   **onpromotion** gives the total number of items in a product family that
    were being promoted at a store at a given date.

**test.csv**

-   The test data, having the same features as the training data. You will predict the target sales for the dates in this file.

-   The dates in the test data are for the 15 days after the last date in the training data.

**transaction.csv**

-   Contains date, store_nbr and transaction made on that specific date.

**sample_submission.csv**

-   A sample submission file in the correct format.

**stores.csv**

-   Store metadata, including city, state, type, and cluster.

-   cluster is a grouping of similar stores.

**oil.csv**

-   **Daily oil price** which includes values during both the train and
     test data timeframes. (Ecuador is an oil-dependent country and its
     economical health is highly vulnerable to shocks in oil prices.)

**holidays_events.csv**

-   Holidays and Events, with metadata

> **NOTE**: Pay special attention to the transferred column. A holiday
> that is transferred officially falls on that calendar day but was
> moved to another date by the government. A transferred day is more
> like a normal day than a holiday. To find the day that it was
> celebrated, look for the corresponding row where type is **Transfer**.
>
> For example, the holiday Independencia de Guayaquil was transferred
> from 2012-10-09 to 2012-10-12, which means it was celebrated on
> 2012-10-12. Days that are type **Bridge** are extra days that are
> added to a holiday (e.g., to extend the break across a long weekend).
> These are frequently made up by the type **Work Day** which is a day
> not normally scheduled for work (e.g., Saturday) that is meant to
> payback the Bridge.

-   Additional holidays are days added a regular calendar holiday, for
    example, as typically happens around Christmas (making Christmas
    Eve a holiday).

**Additional Notes**

-   Wages in the public sector are paid every two weeks on the 15th and
    on the last day of the month. Supermarket sales could be affected
    by this.

-   A magnitude 7.8 earthquake struck Ecuador on April 16, 2016. People
    rallied in relief efforts donating water and other first need
    products which greatly affected supermarket sales for several
    weeks after the earthquake.

## 🛠 Built With <a name="built-with"></a>

### Tech Stack <a name="tech-stack"></a>





<details>
<summary>Language</summary>
  <ul>
    <li><a href="https://www.python.org/">Python</a></li>
  </ul>
</details>


<details>
<summary>Database</summary>
  <ul>
    <li><a href="https://www.microsoft.com/en-us/sql-server">SQL</a></li>
  </ul>
</details>




## Packages and Libraries 📚
#### Collection of significant Python Libraries:
- Pandas
- Numpy
- Seaborn
- Scipy
- Matplotlib
- Pyodbc
- Dotenv
- Sklearn
- Statsmodels
- Scikit
- Imblearn
- Custom Imputer
- XG Boost
- Pipeline

## Cleaning the Data 🧹
#### We begin by thoroughly cleaning our data.
- Changing data types 
- Dealing with Nan values
- Replacing Values in categorical columns to be more consistent

## Exploratory Data Analysis 🕵



- Univariate Analysis
  https://github.com/Koanim/LP2-Telco-churn-prediction/blob/main/box%20plot.JPG


  
- Bivariate Analysis
- https://github.com/Koanim/LP2-Telco-churn-prediction/blob/main/bivariate.JPG?raw=true





## Visualizations 👀

- Line Chart 📈
- Bar chart 📊
- Box plot ![Box Plot Logo](path/to/boxplot_logo.png)
- Kernel Density Estimate (KDE) plot ![KDE Plot Logo](path/to/kde_logo.png)
- Calplot ![Calplot Logo](path/to/calplot_logo.png)
- Heatmap ![Heatmap Logo](path/to/heatmap_logo.png)

## Analysis 🔍
- Utilizing Python and data analysis libraries such as Pandas, Matplotlib, and Seaborn, we performed exploratory data analysis (EDA) to uncover trends and insights.
- 

## Statistical, Machine Learning Models and Hyperparameter Tuning
-   Sarima
-   Exponential smoothening model
-   GradientBoost Regressor	
-	XGBoost	
-   Linear Regression	