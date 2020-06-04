### Dataset description

We are working with 42,840 hierarchical time series. The data were obtained in the **3 US states** of California (CA), Texas (TX), and Wisconsin (WI). **Hierarchical** here means that data can be aggregated on different levels: item level, department level, product category level, and state level. The sales information reaches back **from Jan 2011 to June 2016**. In addition to the sales numbers, we are also given corresponding data on **prices, promotions, and holidays**. Note, that we have been warned that **most of the time series contain zero values**

### Dataset files

#### Training data
- *sales_train_validation.csv* - Contains the historical daily unit sales data per product and store [d_1 - d_1913].
    - Date range: [2011-01-29 - 2016-05-22] 
    - Fields: IDs, department, category, store, and state 
- *sell_prices.csv* - Contains information about the price of the products sold per store and date. It is a weekly average
    - Fields: store_id, item_id, wm_yr_wk (the id of the week), sell_price (provided per week (average across seven days), if not available the product was not sold during this week) 
- *calendar.csv* - Contains the dates on which products are sold. The dates are in a yyyy/dd/mm format.
    - Fields: day-of-the week, month, year, and an 3 binary flags of [SNAP food stamps](https://www.benefits.gov/benefit/361)

#### Validation data
 - *sales_train_evaluation.csv* - Available one month before the competition deadline. It will include sales for [d_1 - d_1941]. It includes the validation period of 28 days until 2016-06-19

#### Submission file
- *submission.csv* - Demonstrates the correct format for submission to the competition. The prediction of 28 forecast days (F1-F28)



