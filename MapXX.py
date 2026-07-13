CheckEven = lambda No : (No % 2 == 0)

Increment = lambda No : No + 1

def main():
    Data = [13,12,8,10,11,20]

    print("Input Data Is:", Data)

    FData = list(filter(CheckEven, Data)) # Filter Data

    print("Data After Filter:", FData)

    MData = list(map(Increment, FData)) # Map Data

    print("Data After Map", MData)

if __name__ == "__main__":
    main()