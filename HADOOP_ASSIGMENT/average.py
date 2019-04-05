#10. Using python, map-reducer, find the average votes on the year 1936.



from mrjob.job import MRJob



class MRmyjob(MRJob):
	def mapper(self,_,line):

		data = line.split(',')
		date = data[1].strip()
		votes = data[5].strip()
		if date == '1936':
			yield "votes",votes
		
	
	def reducer(self, key, list_of_values):
		count = 0
		total = 0
		for x in list_of_values:
			total = total + float(x);
			count = count+1
			avglen = ("%.2f" % (total / count))
		yield key,avglen
	
if __name__ == '__main__':
	MRmyjob.run();