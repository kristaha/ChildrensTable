import datetime
from yahoo_finance import Share
import Stock


class FileReader():
    def __init__(self, filePath):
        self.file = open(filePath, 'r')
        self.valueList = self.readFile()  # listene i listen ser slik ut: [dato, pris, volum]

    def readFile(self):
        lines = []
        for line in self.file:
            lineValuesList = line.split()
            lines.append(lineValuesList)
        return lines

    def getPriceList(self):
        priceList = []

        for list in self.valueList:
            value = list[1]
            if ',' in value:
                splitNr = value.split(',')
                priceList.append(float(splitNr[0] + '.' + splitNr[1]))
            else:
                priceList.append(float(value))

        return priceList

    def getVolumeList(self):
        volumeList = []

        for list in self.valueList:
            volumeList.append(int(list[2]))

        return volumeList

    def getDateList(self):
        dateList = []

        for list in self.valueList:
            date = list[0].split('.')
            dateList.append(datetime.date(int(date[2]), int(date[1]), int(date[0])))
        return dateList


#path = "/Users/kristianhaga/Library/Mobile Documents/com~apple~TextEdit/Documents/testForFillesing.txt"
#reader = FileReader(path)

#print(reader.getDateList())


class ReadInFromAPI(): # yahoo finance er lagt ned.
    def __init__(self, stock, startDate, endDate):
        self.stock = stock
        self.valueDict = self.readInData(startDate, endDate)

    def readInData(self, startDate, endDate):  # dato på formatet 'yyyy-mm-dd'
        #return Share(self.stock.getTicker()).get_historical(startDate, endDate)
        return Share('YHOO').get_historical('2014-04-25', '2014-04-29')

    def getPriceList(self):
        priceList = []

        for dict in self.valueDict:
            priceList.insert(0, float(dict.get('Close')))
        return priceList

    def getVolumeList(self):
        volumeList = []

        for dict in self.valueDict:
            volumeList.insert(0, int(dict.get('Volume')))
        return volumeList

    def getDateList(self):
        dateList = []

        for dict in self.valueDict:
            date = dict.get('Date').split('-')
            dateList.insert(0,datetime.date(int(date[0]), int(date[1]), int(date[2])))
        return dateList

#stock = Stock.Stock('Yahoo','YHOO', [0],[0], [0],[0])
#reader = ReadInFromAPI(stock,'2017-07-01', '2017-07-25')

#print(reader.getPriceList())