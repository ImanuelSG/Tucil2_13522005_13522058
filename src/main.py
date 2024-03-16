import numpy as np
from bruteforce.bruteforce import plotBezierCurve

def main():
    try:
        # Input control points from the user
        num_points = int(input("Enter the number of control points: "))
        Points = []
        for i in range(num_points):
            x = float(input(f"Enter x-coordinate for control point {i+1}: "))
            y = float(input(f"Enter y-coordinate for control point {i+1}: "))
            Points.append([x, y])
        Points = np.array(Points)
        
        # Input number of samples
        num_samples = int(input("Enter the number of samples: "))
        
        # Plot the Bézier curve
        plotBezierCurve(Points, num_samples)
    
    except ValueError as ve:
        print("Error:", ve)
        print("Please enter valid numeric values for coordinates and number of samples.")

if __name__ == "__main__":
    main()
