# YahooFinanceCrawler

## This is a python crawler that will automatically download 
1) the historical stock price data
2) the dividends data
3) then calculate the montly return rate

## Usage:
You must have a chromeDriver avaliable on your computer, selenium 4.0 library is used to support the automation.
To get start, follow the examples in the main mehtod in the main.py file.
```Python
 stock_name = "ABX.TO"
 # download the dividend data
 downloadDividendData(stock_name)
 
 # download the price data
 downloadDailyData(stock_name)
 
 # save the result into an excel csv file
 readDailyDataWithDividen(stock_name, "2011-10-1", "2021-10-1")
 
 # without assign a start/end date, it will use the time range: start_date="2003-1-1", end_date="2012-12-31"
 # readDailyDataWithDividen(stock_name)

```
