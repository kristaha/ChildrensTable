class Stock():
    def __init__(self, name, ticker, priceList, volumeList, annualyIncomeList, quarterlyIncomeList, dateList,
                 nettoResultList):
        self.name = name
        self.ticker = ticker
        self.priceList = priceList
        self.volumeList = volumeList
        self.annualyIncomeList = annualyIncomeList
        self.quartelyIncomeList = quarterlyIncomeList
        self.dateList = dateList
        self.nettoResultList = nettoResultList

    def getName(self):
        return self.name

    def getTicker(self):
        return self.ticker

    def getPriceList(self):
        return self.priceList

    def getvolumeList(self):
        return self.volumeList

    def setPriceList(self, list):
        self.priceList = list

    def updatePriceList(self, value):
        self.priceList.append(value)

    def setVolumeList(self, list):
        self.volumeList = list

    def updateVolumeList(self, value):
        self.volumeList.append(value)

    def getAnnuallyIncomeList(self):
        return self.annualyIncomeList

    def getQuarterlyIncomeList(self):
        return self.quartelyIncomeList

    def getDateList(self):
        return self.dateList

    def setDateList(self, list):
        self.dateList = list

    def getNettoResultList(self):
        return self.nettoResultList
