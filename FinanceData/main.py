# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from FinanceData.DailyData import downloadDividendData, downloadDailyData, readDailyDataWithDividen



# This is a runner
if __name__ == '__main__':
    stock_name = "IBM"
    # download the dividend data
    downloadDividendData(stock_name)
    # download the price data
    downloadDailyData(stock_name)
    # save the result into an excel csv file
    readDailyDataWithDividen(stock_name, "2011-10-1", "2021-10-1")
    # without assign a start/end date, it will use the time range: start_date="2003-1-1", end_date="2012-12-31"
    # readDailyDataWithDividen(stock_name)
