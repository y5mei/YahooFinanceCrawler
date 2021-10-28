# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from FinanceData.DailyData import downloadDividendData, downloadDailyData, readDailyDataWithDividen, \
    readExtraInvestingData, readFF3Factor_ResearchData, readDailyData,  \
    readDailyDataWithDividenIndia
from FinanceData.ChromeDriverSetter import webDriverWithCustimizedDownloadLocaiton


# This is a runner
if __name__ == '__main__':
    # stock_name = "ABX.TO"
    # stock_name = "^CRSPTM1"
    # download the dividend data
    # downloadDividendData(stock_name)

    # download the price data
    # downloadDailyData(stock_name)

    # save the result into an excel csv file
    # readDailyDataWithDividen(stock_name, "2011-10-1", "2021-10-1")

    # without assign a start/end date, it will use the time range: start_date="2003-1-1", end_date="2012-12-31"
    # readDailyDataWithDividen(stock_name)

    # this is the replacement data for CRSP, WE USED CRSPTM1
    # readExtraInvestingData("CRSP-Investing")

    # this is the DJ global index W1DOW W1DOW-Investing
    # readExtraInvestingData("W1DOW-Investing")

    # readFF3Factor_ResearchData("FF3Factors")
#######################################################################################################################
    # 0) ABX is from an india website: https://in.investing.com/indices/the-global-dow-usd-historical-data
    # 1) IBM
    # readDailyDataWithDividen("IBM", "2011-10-1","2021-10-1")
    # 2) KEP
    # readDailyDataWithDividen("KEP", "2011-10-1", "2021-10-1")
    # 3) Siemens SIEGY
    # readDailyDataWithDividen("SIEGY", "2011-10-1", "2021-10-1")
    # 4) Group Televisa TV
    # readDailyDataWithDividen("TV", "2011-10-1", "2021-10-1")
    # 5) YPF
    # readDailyDataWithDividen("YPF", "2011-10-1", "2021-10-1")
    # 6) Australia EWA
    # readDailyDataWithDividen("EWA", "2011-10-1", "2021-10-1")
    # 7) Canada EWC
    # readDailyDataWithDividen("EWC", "2011-10-1", "2021-10-1")
    # 8) Germany EWG
    # readDailyDataWithDividen("EWG", "2011-10-1", "2021-10-1")
    # 8) Malaysia EWM
    # readDailyDataWithDividen("EWM", "2011-10-1", "2021-10-1")
    # 8) mEXICO EWW
    # readDailyDataWithDividen("EWW", "2011-10-1", "2021-10-1")
    # 9) Singapore EWS
    # readDailyDataWithDividen("EWS", "2011-10-1", "2021-10-1")
    # 9) SPY 500
    # readDailyDataWithDividen("SPY", "2011-10-1", "2021-10-1")
    # 10) CRSPTM1
    # readExtraInvestingData("CRSP-Investing", "2011-10-1", "2021-10-1")
    # 11) ABX
    #  readDailyDataWithDividenIndia("ABXIndia", "2011-10-1", "2021-10-1")

    readExtraInvestingData("W1DOW-Investing", "2011-10-1", "2021-10-1")
