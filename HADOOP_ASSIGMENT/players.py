#6. Using python, 

#a) Write a map-reducer program to find the total count of the players

from mrjob.job import MRJob
from mrjob.step import MRStep
import sys  
class MRWordPlayerCount(MRJob):
	def mapper1(self, _, lines):
		data = lines.split(',')
		players = data[0].strip()
		print(players)
		yield players,1	
	def combiner(self, word, counts):
#		print(word)
		yield word,1		
		
		
	def reducer1(self, key, counts):

		yield "total players",key
	def reducer2(self, key,word):

		yield key,len(list(word))
	def steps(self):
		return [ MRStep(mapper=self.mapper1,reducer=self.combiner),MRStep(reducer=self.reducer1),MRStep(reducer=self.reducer2)]



if __name__ == '__main__':
    MRWordPlayerCount.run()





