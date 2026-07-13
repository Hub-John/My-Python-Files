import time
import threading

def SumEven(No):
    print("TID of SumEven thred is: ", threading.get_ident())

def SumOdd(No):
    print("TID of SumOdd thred is: ", threading.get_ident())
    
def main():
    print("TID of main thred is: ", threading.get_ident())
    
    start_time = time.perf_counter() # Stop Watch Start
    
    tObj1 = threading.Thread(target=SumEven, args=(1000000, )) 
    tObj2 = threading.Thread(target=SumOdd, args=(1000000, ))
    tObj1.start()
    tObj2.start()
    tObj1.join()
    tObj2.join()      

    end_time = time.perf_counter() # Stop Watch End

    print(f"Time required is {end_time-start_time:.4f}")
    
if __name__ == "__main__":
    main()