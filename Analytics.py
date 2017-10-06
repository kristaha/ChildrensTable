import Stock


class MovingAvrageAnalytics():
    def __init__(self, stock):

        self.stock = stock

    def sma(self, numberOfDays):
        smaPristList = self.stock.getPriceList()

        if len(self.stock.priceList) > numberOfDays - 1:
            i = -numberOfDays
            sumPrices = 0
            while i < -numberOfDays:
                sumPrices += smaPristList
                i += 1

            return sumPrices / numberOfDays
        else:
            sumPrices = 0
            for i in range(len(smaPristList)):
                sumPrices += smaPristList

            return sumPrices / len(self.stock.getPriceList())

    def SMAhasShortTermAboveLongTerm(self, numberOfDaysShortTerm, numberOfDaysLongTerm):
        valueShortTerm = self.sma(numberOfDaysShortTerm)
        valueLongTerm = self.sma(numberOfDaysLongTerm)
        if valueShortTerm > valueLongTerm:
            return True
        else:
            return False

    def emaList(self, numberOfDays):
        smaValue = sum(self.stock.getPriceList()[:numberOfDays]) / numberOfDays
        multiplier = 2 / (numberOfDays + 1)
        emaValueList = []
        emaValueList.append(
            ((self.stock.getPriceList()[numberOfDays - 1] - smaValue) * multiplier) + smaValue)  # base case

        emaPriceList = self.stock.getPriceList()
        j = 0
        for stockPrice in emaPriceList[numberOfDays:]:
            emaValue = ((stockPrice - emaValueList[j]) * multiplier) + emaValueList[j]
            j += 1
            emaValueList.append(emaValue)

        return emaValueList

    def emaRecursive(self, numberOfDays, day):  # day=0 betyr at vi finner ema i dag, day=-1 finner ema i går.

        multiplier = 2 / (numberOfDays + 1)

        if (len(self.stock.getPriceList()[:len(self.stock.getPriceList()) + day])) == numberOfDays:
            smaValue = sum(
                self.stock.getPriceList()[:len(self.stock.getPriceList()) + day]) / numberOfDays    # finner sma av de 'numberOfDays' første dagene.
            return ((self.stock.getPriceList()[numberOfDays - 1] - smaValue) * multiplier) + smaValue  # baseCase
        else:
            return ((self.stock.getPriceList()[day] - self.emaRecursive(
                numberOfDays, day - 1)) * multiplier) + self.emaRecursive(numberOfDays, day - 1)

    def EMAhasShortTermAboveLongterm(self, numberOfDaysShortTerm, numberOfDaysLongterm):

        valueShortTerm = self.emaRecursive(numberOfDaysShortTerm, 0)
        valueLongTerm = self.emaRecursive(numberOfDaysLongterm, 0)

        if valueShortTerm > valueLongTerm:
            return True
        else:
            return False


class GrowthAnalytics():
    def __init__(self, stock):
        self.stock = stock

    def getCompoundAnnualGrowthRate(self, startDate, endDate):
        startIndex = self.stock.dateList.index(startDate)
        endIndex = self.stock.dateList.index(endDate)
        numberOfDays = endIndex - startIndex

        return ((self.stock.getPriceList()[endIndex] / self.stock.getPriceList()[startIndex]) ** (1 / numberOfDays)) - 1

    def getReturnOfEquity(self):
        pass
