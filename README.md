# TRG Week 33

## Costco Wholesale Corp. ($COST)

- Retail Membership & Warehouse-Based Wholesale Company

- https://www.kaggle.com/borismarjanovic/datasets

### 1st Commit

- Load data to raw HTML dataframe for cleaning and analysis.

### 2nd Commit

- Data runs from 1986-07-09 to 2017-11-10

- I think I would like to analyse the data in sets of 5 year timespans

- 1990-1995, 1995-2000, 2000-2005, 2005-2010, 2010-2015

- I want to name the 5 separate tables in 5 routes, respectively as, /90, /95, /00, /05, /10

### 3rd Commit

- I want to take the "High" column data from all 5 datasets and show the yearly average for years 1-5. Year 1 on the X-axis would be 1990, 1995, 2000, 2005, 2010. Year 5 would be the aggregated points of 1994, 1999, 2004, 2009, 2014. I want this visualization to be a new route while keeping the prior code the same.

- - Route Name /highs_by_year_block

### 4th Commit

- I'd like to create a similar route to the 3rd commit, but represent the yearly average "Low" prices.

- Route Name /lows_by_year_block

- Unfortunately, the visual comparison of the Average High and the Average Low are nearly the same.

### 5th Commit

- For the final commit, I want to take the yearly average "High" & "Low" prices, combine that with the current stock price of Costco, and calculate the yearly average median price from 2026 to 2031.

- Route Name /projected_median_prices

- The chart shows the median price to be much lower than the current price of $COST. Median price ranges from $132 to $152. The actual price of $COST is $950. Perhaps this price evaluation is not the wisest. 