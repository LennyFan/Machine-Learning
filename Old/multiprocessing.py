import multiprocessing
multiprocessing.cpu_count()




from multiprocessing import Pool, TimeoutError
import time
import os
distanceset = []
def f((x1,x2)):
    dis = None
    while dis == None:
        try:
            dis = geometry_distance(m.gdf.loc[[x1]],m.gdf.loc[[x2]])
        except:
            print("Connection refused by the server..")
            print("Let me sleep for 60 seconds")
            print("ZZzzzz...")
            time.sleep(60)
            print("Was a nice sleep, now let me continue...")
            continue
    
def mp_worker((inputs, the_time)):
    print " Processs %s\tWaiting %s seconds" % (inputs, the_time)
    time.sleep(int(the_time))
    print " Process %s\tDONE" % inputs

def mp_handler():
    pool.map(f, comparehouses[:10])
    
if __name__ == '__main__':
    pool = Pool(processes=3)              
    # allows the system to recognize four total "cores" or "threads" (two real and two virtual).
    mp_handler()
