from multiprocess import Process
import time


def longSquare(num,results):
    time.sleep(1)
    print(num**2) 
    print('Finished computing!')

if __name__ == '__main__':
    results = {}
    p1 = Process(target=longSquare, args=(1,results))
    p2 = Process(target=longSquare, args=(2,results))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(results)


