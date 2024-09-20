import csv


class Reader:
    def __init__(self, filename):
        self.filename = filename
    def read(self):
        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            #read into a list
            data = list(reader)
            return data

