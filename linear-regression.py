import numpy as np

def get_numbers(prompt):
    while True:
        try:
            values = input(prompt).split()
            return [float(num) for num in values]
        except ValueError:
            print("Please enter numbers separated by spaces. Try again.")

def linear_regression(X, Y, x_predict):
    n = len(X)
    
    sum_x = sum(X)
    sum_y = sum(Y)
    sum_xy = sum(x*y for x,y in zip(X,Y))
    sum_x2 = sum(x**2 for x in X)
    
    b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
    a = (sum_y - b * sum_x) / n
    
    y_predict = b * x_predict + a
    
    return b, a, y_predict

def main():
    print("Linear Regression Calculator")
    print("--------------------------")
    
    X = get_numbers("Enter X values separated by spaces: ")
    
    Y = get_numbers("Enter Y values separated by spaces: ")
    
    while len(X) != len(Y):
        print(f"Error: You entered {len(X)} X values but {len(Y)} Y values.")
        print("Both lists must have the same number of values.")
        X = get_numbers("Re-enter X values: ")
        Y = get_numbers("Re-enter Y values: ")

    while True:
        try:
            x_predict = float(input("Enter X value to predict its Y: "))
            break
        except ValueError:
            print("Please enter a valid number.")
    
    try:
        b, a, y_predict = linear_regression(X, Y, x_predict)
        
        print("\nRegression Results:")
        print(f"b: {b:.4f}")
        print(f"a: {a:.4f}")
        print(f"Regression equation: y = {b:.4f}x + {a:.4f}")
        print(f"Predicted Y for X = {x_predict}: {y_predict:.4f}")
        
    except ZeroDivisionError:
        print("Error: Cannot perform regression (division by zero). Check your input values.")

if __name__ == "__main__":
    main()