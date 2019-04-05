#6. Using Python

#b) Write a map-reducer program to find the total number of the teams.
from mrjob.job import MRJob
from mrjob.step import MRStep
import sys

class MRWordTeamCount(MRJob):
	def mapper1(self, _, lines):
		data = lines.split(',')
		players = data[3].strip()
		yield players,None	
	def combiner(self, word, counts):
		
		yield word,None			
		
		
	def reducer1(self, key, counts):

		yield "total teams",key
	def reducer2(self, key,word):
		count =0
		for i in word:
				count+=1	
		
			
		yield key,count
	def steps(self):
		return [ MRStep(mapper=self.mapper1,reducer=self.combiner),MRStep(reducer=self.reducer1),MRStep(reducer=self.reducer2)]



if __name__ == '__main__':
    MRWordTeamCount.run()





