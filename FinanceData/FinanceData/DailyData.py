# To setup chromedriver for OS:
# https://www.browserstack.com/guide/run-selenium-tests-using-selenium-chromedriver
import os
from datetime import datetime

import pandas
from random import randint

from FinanceData.ChromeDriverSetter import webDriverWithCustimizedDownloadLocaiton
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from collections import defaultdict


def downloadDailyData(stock_name: str) -> str:
    stock_file_name = "./stock_price/"+stock_name + ".csv" # the historical price file

    # make the result folders
    if not os.path.exists('stock_price/'):
        os.makedirs('stock_price/')

    # delete the result file if it is already exist
    if os.path.exists(stock_file_name):
        os.remove(stock_file_name)
    if os.path.exists(stock_name+".csv"):
        os.remove(stock_name+".csv")

    # initialize a driver and use it to visit the yahoo finance page
    driver = webDriverWithCustimizedDownloadLocaiton()
    driver.maximize_window()
    url = "https://finance.yahoo.com/quote/" + stock_name + "/history?p=" + stock_name
    print(url)
    driver.get(url)

    # 1. Clicks on Historical Data tab and sleeps for 2 seconds.
    # https://selenium-python.readthedocs.io/locating-elements.html
    # ID = "id"
    # XPATH = "xpath"
    # LINK_TEXT = "link text"
    # PARTIAL_LINK_TEXT = "partial link text"
    # NAME = "name"
    # TAG_NAME = "tag name"
    # CLASS_NAME = "class name"
    # CSS_SELECTOR = "css selector"
    Historical_tab_XPATH = "//span[text() = 'Historical Data']"
    driver.find_element(By.XPATH, Historical_tab_XPATH).click()
    time.sleep(randint(2, 4))
    # 2. select the time period dropdown button
    Time_period_button = "//*[@id='Col1-1-HistoricalDataTable-Proxy']/section/div[1]/div[1]/div[1]/div/div"
    driver.find_element(By.XPATH, Time_period_button).click()
    time.sleep(randint(2, 4))
    # 3. select the Max button to download all the available data
    Max_button_XPATH = "//*[@id='dropdown-menu']/div/ul[2]/li[4]/button/span"
    driver.find_element(By.XPATH, Max_button_XPATH).click()
    time.sleep(randint(2, 4))
    # time.sleep(2)
    # 4. click the Apply button to apply the change on time period
    Apply_button_XPATH = "//*[@id='Col1-1-HistoricalDataTable-Proxy']/section/div[1]/div[1]/button/span"
    driver.find_element(By.XPATH, Apply_button_XPATH).click()
    time.sleep(randint(2, 4))

    # 5. click the Download button to download the data file and close the driver
    Download_button_XPATH = "//*[@id='Col1-1-HistoricalDataTable-Proxy']/section/div[1]/div[2]/span[2]/a/span"
    driver.find_element(By.XPATH, Download_button_XPATH).click()
    time.sleep(randint(2, 4))

    driver.close()
    # delete the result file if it is already exist
    if os.path.exists(stock_name + ".csv"):
        os.rename(stock_name + ".csv", stock_file_name)

    return stock_file_name

def downloadDividendData(stock_name: str):
    stock_dividend_file_name = "./dividend/" + stock_name + "_div.csv"  # the dividend price file

    # make the result folders
    if not os.path.exists('dividend/'):
        os.makedirs('dividend/')

    # delete the result file if it is already exist
    if os.path.exists(stock_dividend_file_name):
        os.remove(stock_dividend_file_name)
    if os.path.exists(stock_name+".csv"):
        os.remove(stock_name+".csv")

    # initialize a driver and use it to visit the yahoo finance page
    driver = webDriverWithCustimizedDownloadLocaiton()
    driver.maximize_window()
    url = "https://finance.yahoo.com/quote/" + stock_name + "/history?p=" + stock_name
    print(url)
    driver.get(url)

    # 1. Clicks on Historical Data tab and sleeps for 2 seconds.
    # https://selenium-python.readthedocs.io/locating-elements.html
    # ID = "id"
    # XPATH = "xpath"
    # LINK_TEXT = "link text"
    # PARTIAL_LINK_TEXT = "partial link text"
    # NAME = "name"
    # TAG_NAME = "tag name"
    # CLASS_NAME = "class name"
    # CSS_SELECTOR = "css selector"
    Historical_tab_XPATH = "//span[text() = 'Historical Data']"
    driver.find_element(By.XPATH, Historical_tab_XPATH).click()
    time.sleep(randint(2, 4))
    # 2. select the time period dropdown button
    Time_period_button = "//*[@id='Col1-1-HistoricalDataTable-Proxy']/section/div[1]/div[1]/div[1]/div/div"
    driver.find_element(By.XPATH, Time_period_button).click()
    time.sleep(randint(2, 4))
    # 3. select the Max button to download all the available data
    Max_button_XPATH = "//*[@id='dropdown-menu']/div/ul[2]/li[4]/button/span"
    driver.find_element(By.XPATH, Max_button_XPATH).click()
    time.sleep(randint(2, 4))
    # time.sleep(2)


    # 6. click the dividends dropdown list:
    Dividends_button_XPATH = "//*[@id='Col1-1-HistoricalDataTable-Proxy']/section/div[1]/div[1]/div[2]/span/div/span/span"
    driver.find_element(By.XPATH, Dividends_button_XPATH).click()
    time.sleep(randint(2, 3))

    # 7. click the dividen only menul item
    # use ctrl + shift + c to inspect the nested element id
    Dividen_only_button_XPATH = "//*[@data-test='historicalFilter-menu']/div[2]/span"
    driver.find_element(By.XPATH, Dividen_only_button_XPATH).click()
    time.sleep(randint(2, 3))

    # 8. click the Apply button to apply the change on time period
    Apply_button_XPATH = "//*[@id='Col1-1-HistoricalDataTable-Proxy']/section/div[1]/div[1]/button/span"
    driver.find_element(By.XPATH, Apply_button_XPATH).click()
    time.sleep(randint(2, 3))

    Download_button_XPATH = "//*[@id='Col1-1-HistoricalDataTable-Proxy']/section/div[1]/div[2]/span[2]/a/span"
    driver.find_element(By.XPATH, Download_button_XPATH).click()
    time.sleep(randint(2, 4))

    driver.close()

    # delete the result file if it is already exist
    if os.path.exists(stock_name+".csv"):
        os.rename(stock_name+".csv", stock_dividend_file_name)
    return stock_dividend_file_name

# https://ca.investing.com/indices/crsp-us-total-market-historical-data
def parseNumber(param):
    pass
# http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html#Research
def readFF3Factor_ResearchData(stockName: str, start_date="2003-1-1", end_date="2012-12-31"):
    stock_name = stockName
    stock_file_name = "./stock_price/" + stock_name + ".csv"  # the historical price file
    result_file_name = "./result/" + stock_name + ".csv"  # the historical price file
    df = pandas.read_csv(stock_file_name)
    # for i, col in df.iterrows():
    #     df.at[i, "Date"]= str(col[0])[:4]+str(col[0])[4:6]+"01"
    df["Date"] = pandas.to_datetime(df.Date,format='%Y%m')
    # keep only the date and close price
    # df = df[['Date', 'Price']]

    df = df.set_index(['Date'])
    df = df.loc[start_date:end_date]
    # # df['Monthly_Return'] = df['Monthly_Return'].apply(lambda x: format(x, '.2%'))  # change to percentage
    df = df.reindex(index=df.index[::-1])  # reverse the order to have the latest data on the top
    # # df = df.rename(columns={'Monthly_Return': stock_name + "_Monthly_Return"})
    print(df)
    df.to_csv(result_file_name)

# this method read the data downloaded from inversting.com, and calculate the monthly return rate base on the csv file
def readExtraInvestingData(stockName: str,start_date="2003-1-1", end_date="2021-10-01"):
    stock_name = stockName
    stock_file_name = "./stock_price/"+stock_name + ".csv" # the historical price file
    result_file_name = "./result/" + stock_name + ".csv"  # the historical price file

    df = pandas.read_csv(stock_file_name, parse_dates=["Date"])
    # keep only the date and close price
    df = df[['Date', 'Price']]

    # get the last element of a group
    def get_last(df):
        return df.head(1)

    # group all the dataframe by year and month, and return, then return the last day of a month to a data frame
    # group_keys = False so we do not have the leading group indexs (year and month)
    df_out = df.groupby([df['Date'].dt.year, df['Date'].dt.month], group_keys=False).apply(get_last)
    # set the date column as the index column
    # convert the str value to float numbers
    df = df_out.set_index(['Date'])
    for i, col in df.iterrows():
        if type(col[0])== str:
            df.at[i, "Price"]= float(col[0].replace(",",""))
    # print(df)
    # calculate the percentage change
    df = df.pct_change()

    df = df.loc[start_date:end_date]
    df['Price'] = df['Price'].apply(lambda x: format(x, '.2%'))  # change to percentage
    df = df.reindex(index=df.index[::-1])  # reverse the order to have the latest data on the top
    df = df.rename(columns={'Price': stock_name})

    print(df)
    df.to_csv(result_file_name)

    print(df)

def readDailyData(stockName: str, start_date="2003-1-1", end_date="2012-12-31"):
    stock_name = stockName
    stock_file_name = "./stock_price/"+stock_name + ".csv" # the historical price file
    stock_dividend_file_name = "./dividend/" + stock_name + "_div.csv"  # the dividend price file

    df = pandas.read_csv(stock_file_name, parse_dates=["Date"])
    # keep only the date and close price
    df = df[['Date', 'Close']]

    # get the last element of a group
    def get_last(df):
        return df.tail(1)

    # group all the dataframe by year and month, and return, then return the last day of a month to a data frame
    # group_keys = False so we do not have the leading group indexs (year and month)
    df_out = df.groupby([df['Date'].dt.year, df['Date'].dt.month], group_keys=False).apply(get_last)
    # set the date column as the index column
    df = df_out.set_index(['Date'])

    # calculate the percentage change
    df = df.pct_change()
    df = df.loc['2003-1-1':'2012-12-31']
    df['Close'] = df['Close'].apply(lambda x: format(x, '.2%'))  # change to percentage
    df = df.reindex(index=df.index[::-1])  # reverse the order to have the latest data on the top
    df = df.rename(columns={'Close': stock_name})
    print(df)


def readDailyDataWithDividen(stockName: str, start_date="2003-1-1", end_date="2012-12-31"):
    stock_name = stockName
    stock_file_name = "./stock_price/" + stock_name + ".csv"  # the historical price file
    stock_dividend_file_name = "./dividend/" + stock_name + "_div.csv"  # the dividend price file
    result_file_name = "./result/"+stock_name + ".csv"  # the historical price file

    # make the result folders
    if not os.path.exists('result/'):
        os.makedirs('result/')

    # delete the result file if it is already exist
    if os.path.exists(result_file_name):
        os.remove(result_file_name)

    # get the dataframe for historical data
    df = pandas.read_csv(stock_file_name, parse_dates=["Date"])
    df = df[['Date', 'Close']]

    # get the dataframe for dividends
    df_div = pandas.read_csv(stock_dividend_file_name, parse_dates=["Date"])
    df_div = df_div[['Date', 'Dividends']]

    # if df_div.empty:
    #     df_div = df.copy()
    #     for col in df_div:
    #         df_div["Close"].values[:]=0
    #     df_div = df_div.rename(columns={'Close': "Dividends"})

    # build a hashmap for dividends, key is yyyy-mm, value is the dividends
    dividends_dict = defaultdict(lambda: 0.0)
    for index, row in df_div.iterrows():
        key = str(row['Date'].year)+"-"+str(row['Date'].month)
        val = row['Dividends']
        dividends_dict[key] += val
        # print(key, val)


    # get the last element of a group
    def get_last(df):
        return df.tail(1)

    # group all the dataframe by year and month, and return, then return the last day of a month to a data frame
    # group_keys = False so we do not have the leading group indexs (year and month)
    try:
        df_out = df.groupby([df['Date'].dt.year, df['Date'].dt.month], group_keys=False).apply(get_last)
    except:
        df['Date'] = pandas.to_datetime(df['Date'])
        df_out = df.groupby([df['Date'].dt.year, df['Date'].dt.month], group_keys=False).apply(get_last)
    # df_out = df.groupby([df['Date'].dt.year, df['Date'].dt.month], group_keys=False).apply(get_last)
    # set the date column as the index column
    df = df_out.set_index(['Date'])
    # calculate the percentage change
    pct_change_list = []
    date_time_list = []
    buy_price = 0
    counter = 0
    for index, row in df.iterrows():
        key = str(index.year) + "-" + str(index.month)
        if counter ==0:
            buy_price = row["Close"]
            pct_change_list.append("NaN")
            date_time_list.append(index)
            counter +=1
            continue
        else:
            sold_price = row["Close"]+dividends_dict[key]
            pct_price = (sold_price-buy_price)/buy_price
            pct_change_list.append(pct_price)
            date_time_list.append(index)
            buy_price = row["Close"]

    df_pct = pandas.DataFrame({"Monthly_Return":pct_change_list,"Date":date_time_list})
    df_pct = df_pct.set_index(['Date'])

    # print(df_pct)
    df = df.join(df_pct["Monthly_Return"])
    df = df[['Monthly_Return']]

    # df = df.pct_change()
    df = df.loc[start_date:end_date]
    df['Monthly_Return'] = df['Monthly_Return'].apply(lambda x: format(x, '.2%'))  # change to percentage
    df = df.reindex(index=df.index[::-1])  # reverse the order to have the latest data on the top
    df = df.rename(columns={'Monthly_Return': stock_name+"_Monthly_Return"})
    print(df)
    df.to_csv(result_file_name)

def readDailyDataWithDividenIndia(stockName: str, start_date="2003-1-1", end_date="2012-12-31"):
    stock_name = stockName
    stock_file_name = "./stock_price/" + stock_name + ".csv"  # the historical price file
    stock_dividend_file_name = "./dividend/" + stock_name + "_div.csv"  # the dividend price file
    result_file_name = "./result/"+stock_name + ".csv"  # the historical price file

    # make the result folders
    if not os.path.exists('result/'):
        os.makedirs('result/')

    # delete the result file if it is already exist
    if os.path.exists(result_file_name):
        os.remove(result_file_name)

    # get the dataframe for historical data
    df = pandas.read_csv(stock_file_name, parse_dates=["Date"])
    df = df[['Date', 'Close']]

    # get the dataframe for dividends
    df_div = pandas.read_csv(stock_dividend_file_name, parse_dates=["Date"])
    df_div = df_div[['Date', 'Dividends']]

    # if df_div.empty:
    #     df_div = df.copy()
    #     for col in df_div:
    #         df_div["Close"].values[:]=0
    #     df_div = df_div.rename(columns={'Close': "Dividends"})

    # build a hashmap for dividends, key is yyyy-mm, value is the dividends
    dividends_dict = defaultdict(lambda: 0.0)
    for index, row in df_div.iterrows():
        key = str(row['Date'].year)+"-"+str(row['Date'].month)
        val = row['Dividends']
        dividends_dict[key] += val
        # print(key, val)


    # get the last element of a group
    def get_last(df):
        return df.head(1)

    # group all the dataframe by year and month, and return, then return the last day of a month to a data frame
    # group_keys = False so we do not have the leading group indexs (year and month)
    try:
        df_out = df.groupby([df['Date'].dt.year, df['Date'].dt.month], group_keys=True).apply(get_last)
        print(df_out)
    except:
        df['Date'] = pandas.to_datetime(df['Date'])
        df_out = df.groupby([df['Date'].dt.year, df['Date'].dt.month], group_keys=False).apply(get_last)
    # df_out = df.groupby([df['Date'].dt.year, df['Date'].dt.month], group_keys=False).apply(get_last)
    # set the date column as the index column
    df = df_out.set_index(['Date'])
    # calculate the percentage change
    pct_change_list = []
    date_time_list = []
    buy_price = 0
    counter = 0
    for index, row in df.iterrows():
        key = str(index.year) + "-" + str(index.month)
        if counter ==0:
            buy_price = row["Close"]
            pct_change_list.append("NaN")
            date_time_list.append(index)
            counter +=1
            continue
        else:
            sold_price = row["Close"]+dividends_dict[key]
            pct_price = (sold_price-buy_price)/buy_price
            pct_change_list.append(pct_price)
            date_time_list.append(index)
            buy_price = row["Close"]

    df_pct = pandas.DataFrame({"Monthly_Return":pct_change_list,"Date":date_time_list})
    df_pct = df_pct.set_index(['Date'])

    # print(df_pct)
    df = df.join(df_pct["Monthly_Return"])
    df = df[['Monthly_Return']]

    # df = df.pct_change()
    df = df.loc[start_date:end_date]
    df['Monthly_Return'] = df['Monthly_Return'].apply(lambda x: format(x, '.2%'))  # change to percentage
    df = df.reindex(index=df.index[::-1])  # reverse the order to have the latest data on the top
    df = df.rename(columns={'Monthly_Return': stock_name+"_Monthly_Return"})
    print(df)
    df.to_csv(result_file_name)

def downloadAndPrintMontlyReturn(stock_name: str):
    stock_file_name = downloadDailyData(stock_name)
    readDailyData(stock_name)

if __name__ == "__main__":
    stock_name = "IBM"
    # stock_name = "KEP"
    # stock_name = "ABX.TO"
    # stock_name = "ENR.DE"
    # downloadDividendData(stock_name)
    # downloadDailyData(stock_name)
    # readDailyDataWithDividen(stock_name)
