import matplotlib.pyplot as plt

def main():

    marks = [45,55,60,62,65,67,70,72,75,78,80,82,85,90,92]

    plt.hist(
        marks,              # Continous data
        bins=5,             # number of groups
        edgecolor="#000",   # Border Color
        alpha=0.8,          # Transperency
        rwidth=0.9          # Relative width of bars
    )

    plt.title("Marvellous Histogram Plot")
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.show()

if __name__ == "__main__":
    main()
