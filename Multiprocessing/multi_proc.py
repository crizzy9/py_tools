import multiprocessing

def spawn(i, i2):
	print("Spawned!", i, i2)

# so that when this file is imported it wont run??
if __name__ == '__main__':
	for i in range(100):
		p = multiprocessing.Process(target=spawn, args=(i,i+1))
		p.start()
		# waits for other processes to finish otherwise will create individual process for all
		# p.join()