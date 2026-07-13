import os
import time
import multiprocessing

def SumEven(No):
    print(f"PID of SumEven : {os.getpid()} PPID Of SumEven : {os.getppid()}")

    Sum = 0

    for i in range(2, No, 2):
        Sum = Sum + i

    print("Sumation of Even: ", Sum)

def SumOdd(No):
    print(f"PID of SumOdd : {os.getpid()} PPID Of SumOdd : {os.getppid()}")
    
    Sum = 0

    for i in range(1, No, 2):
        Sum = Sum + i

    print("Sumation of Odd: ", Sum)

def main():
    print(f"PID of Main : {os.getpid()} PPID Of Main : {os.getppid()}")

    start_time = time.perf_counter()
    
    tObj1 = multiprocessing.Process(target=SumEven, args=(100, )) 
    tObj2 = multiprocessing.Process(target=SumOdd, args=(100, ))
    
    tObj1.start()
    tObj2.start()
    
    tObj1.join()
    tObj2.join()      

    end_time = time.perf_counter()

    print(f"Time required is: {end_time-start_time:.4f}")
    
if __name__ == "__main__":
    main()