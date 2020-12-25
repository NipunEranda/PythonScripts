import time
import multiprocessing
from idCreater import *
from sliitResultChecker import *

id = Idcreater()
id.enterFields()
id.initiate()

if(id.choice == 1):
	rc = ResultChecker(id.oldNic)
else:
	rc = ResultChecker(id.newNic)
	
rc.setDetails()

start = time.time()
processes = []
for i in range(10):
	p = multiprocessing.Process(target=rc.initiate, args=(i,))
	p.start()
	processes.append(p)
	
for process in processes:
	process.join()

end = time.time()
print("Finished in "+ str(end-start) +" seconds.")
