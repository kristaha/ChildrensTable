import datetime
import Stock


class FileReader():
    def __init__(self, filePath):
        self.file = open(filePath, 'r')
        self.valueList = self.readFile()  # listene i listen ser slik ut: [dato, pris, volum]

    def readFile(self):
        lines = []
        for line in self.file:
		lines.append(line.split())
	
	return lines
