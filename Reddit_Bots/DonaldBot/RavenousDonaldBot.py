#! python3
 # reddit RavenousDonaldBot




from RavenousDataBot import RavenousDataBot
from multiprocessing import Process

import datetime, csvmaker

print('DONALD STARTED')
###logs into RavenousDataBot user

def logger(s,message):
    timecollected = datetime.datetime.now()

    csvmaker.archive(s)

    log = open(s,'a')

    log.write(str(timecollected)+ "\n") 

    print(message + str(timecollected))

donaldnew = ('the_donald', 'new', 1000, 'donaldnew.csv', 'donaldarchive.txt')

donaldhot = ('the_donald', 'hot', 100,'hotdonald.csv', 'hotdonaldarchive.txt')

polhot = ('politics', 'hot', 100, 'hotpolitics.csv', 'hotpolarchive.txt')

polnew = ('politics', 'new', 1000, 'newpol.csv', 'newpolarchive.txt')


if __name__ == '__main__':
    print('---------------process started------------')

    proc = [
        Process(target = RavenousDataBot, args =  donaldnew),
        Process(target = RavenousDataBot, args = polnew),
        Process(target = RavenousDataBot, args = donaldhot),
        Process(target = RavenousDataBot, args = polhot)
    ]

    for p in proc:
        p.start()
    for p in proc:
        p.join()




logger('donaldlog.txt','logged at: ')