class Slot:
	#constructor
	def __init__(self,data):
		self.data=data

class Hash_table:
	def __init__(self):
		#don't need to pass anything into constructor cuz starts empty
		self.slot_dict=dict()
	def insert(self,d):
		#generate key using hash
		key=hash(d)
		self.slot_dict[key]=Slot(data= d)
		return(True)


def main():
	ht=Hash_table()
	print(ht.insert(d=100))
if __name__=='__main__':
	main()