#import numpy
#numpy.random.seed(1234)
import skbio
import csv
import PyPluMA

class PERMANOVAPlugin:
    def input(self, filename):
        self.myfile = filename

    def run(self):
        files = open(self.myfile, "r")
        filenames = files.read().split()
        files.close()

        self.groups = open(PyPluMA.prefix()+"/"+filenames[1], "r")

        #get group names from groupfile
        csv_reader = csv.reader(self.groups)
        group_names = []
        next(csv_reader)

        for row in csv_reader:
            group_names.append(row[1])

        #get distance matrix from distfile
        dm = skbio.DistanceMatrix.read(PyPluMA.prefix()+"/"+filenames[3], format='lsmat')
        self.result = skbio.stats.distance.permanova(dm, group_names)

    def output(self, filename):
        outfile = open(filename, 'w')
        outfile.write(str(self.result))
