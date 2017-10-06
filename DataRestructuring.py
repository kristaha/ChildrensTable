import datetime


class DataRestructuring():
    def __init__(self):
        pass

    def convertFromDaysToWeeks(self, valueList, dateList):
        weeklyValueList = []
        weeklyValue = 0

        for i in range(len(valueList)):
            if (not dateList[i - 1].isocalendar()[1] == dateList[i].isocalendar()[1]) and (
            not len(weeklyValueList) == 0):
                weeklyValueList.append(weeklyValue)
                weeklyValue = valueList[i]
            else:
                weeklyValue += valueList[i]

        return weeklyValueList
