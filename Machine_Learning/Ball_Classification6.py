from sklearn import tree

def main():
    print("Ball Classification Case Study")

    # Testing Features= [35, 1], [95, 0]
    Independent = [
        [35, 1],
        [47, 1],
        [90, 0],
        [48, 1],
        [90, 0],
        [35, 1],
        [92, 0],
        [35, 1],
        [35, 1],
        [35, 1],
        [96, 0],
        [43, 1],
        [110, 0],
    ]

    # Testing Labels= [1, 2]
    Dependent = [
        1,
        1,
        2,
        1,
        2,
        1,
        2,
        1,
        1,
        1,
        2,
        1,
        2,
    ]

    # Creating and Training the Model
    model = tree.DecisionTreeClassifier()

    # The .fit() function is where the actual machine learning "training" happens.
    model = model.fit(Independent, Dependent)

    # Making Predictions
    Result = model.predict([[35, 1], [95, 0]])

    print("Predicted Result of model is:", Result)

if __name__ == "__main__":
    main()