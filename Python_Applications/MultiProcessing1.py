import time
import multiprocessing

def SumEven(No):
    Sum = 0

    for i in range(2, No, 2):
        Sum = Sum + i

    print("Sumation of Even: ", Sum)

def SumOdd(No):

    Sum = 0

    for i in range(1, No, 2):
        Sum = Sum + i

    print("Sumation of Odd: ", Sum)

def main():
    
    start_time = time.perf_counter() # Stop Watch Start
    
    tObj1 = multiprocessing.Process(target=SumEven, args=(1000000, )) 
    tObj2 = multiprocessing.Process(target=SumOdd, args=(1000000, ))
    
    tObj1.start()
    tObj2.start()
    
    tObj1.join()
    tObj2.join()      

    end_time = time.perf_counter()

    print(f"Time required is: {end_time-start_time:.4f}")
    
if __name__ == "__main__":
    main()