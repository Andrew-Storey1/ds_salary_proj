# Data Science Salary Estimator: Project Overview Pt.1
- Create a tool that estimates Data Scientist salaries based on geographic location in the UK.
- Scrape job info from Indeed using Beautifulsoup
- Discover the best model for the peoject and apply it
- Build a client-facing API using flask

## Why and What Next?
Salaries tend to be higher in bigger cities such as London or Manchester and lower in smaller cities such as Leeds or Newcastle. However, as remote working is becoming the norm due to covid-19 I am curious whether this will change. 

A theory is that as more jobs become remote, there will be less incentive to live in bigger cities. If that is the case, in the future will salaries be determined by where you live rather than the location of your office?

## Steps
### Web Scraping
Use Selenium to scrape 1000 job postings from glassdoor.com to receive the following information about each role:
- Job title/seniority
- Salary Estimate
- Rating
- Company
- Location
- Company Size

Using selenium again I will scrape Numbeo.com for the cost of living in each city to receive the following information:
#### Restaurant Prices
- Inexpensive Restaurant & Mid-range Restaurant
- Domestic Beer 
- Imported Beer
- Cappuccino
- Coke/Pepsi 
- Bottled Water

#### Groceries
- Milk (1 liter)
- Loaf of Fresh White Bread (500g)
- Rice (white), (1kg)
- Eggs (regular) (12)
- Chicken Fillets (1kg)
- Apples (1kg)
- Banana (1kg)
- Oranges (1kg)
- Tomato (1kg)
- Potato (1kg)    
- Onion (1kg)    

### Transportation
- One-way Ticket (Local Transport)
- Monthly Pass (Regular Price)
- Taxi Start (Normal Tariff)
- Taxi 1km (Normal Tariff)
- Gasoline (1 litre)

### Utilities    
- Basic (Electricity, Heating, Cooling, Water, Garbage) for 85m2 Apartment
- Internet (60 Mbps or More, Unlimited Data)

#### Sports And Leisure
- Fitness Club, Monthly Fee for 1 Adult    
- Tennis Court Rent (1 Hour on Weekend)    
- Cinema, International Release, 1 Seat    

#### Clothing And Shoes
- 1 Pair of Jeans (Levis 501 Or Similar)
- 1 Summer Dress in a Chain Store (Zara, H&M, ...)
- 1 Pair of Nike Running Shoes (Mid-Range)
- 1 Pair of Men Leather Business Shoes

#### Rent Per Month
- Apartment (1 bedroom) in City Centre
- Apartment (1 bedroom) Outside of Centre
- Apartment (3 bedrooms) in City Centre    
- Apartment (3 bedrooms) Outside of Centre

#### Buy Apartment Price
- Price per Square Meter to Buy Apartment in City Centre    
- Price per Square Meter to Buy Apartment Outside of Centre

#### Salaries And Financing
- Average Monthly Net Salary (After Tax)
- Mortgage Interest Rate in Percentages (%), Yearly, for 20 Years Fixed-Rate

### Data Cleaning
After scraping the data, I need to clean it up so that will be usable for my model. I will make the following changes and create the following variables:
- Parse numeric data out of salary
- Make columns for employer-provided salary and yearly wages
- Remove rows without salary
- Column for simplified job title and Seniority
