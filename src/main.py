import numpy as np
from bruteforce.bruteforce import plotBezierCurveBruteForce
from dnc.dnc_animate import plotBezierCurveDnC
from utils.utils import read_control_points_from_file
from time import time

def main():
    try:
        # Input control points from a file
        print("1. Metode Brute Force")
        print("2. Metode Divide and Conquer")
        method = input ("Masukkan metode yang ingin digunakan (1/2): ")
        while (method != "1" and method != "2"):
            print("Masukkan metode yang valid")
            method = input ("Masukkan metode yang ingin digunakan (1/2): ")
        
        filename = input("Masukkan nama file dengan konfigurasi terkait: ")
        Points = read_control_points_from_file(filename)
        if Points is None:
            return
        # Input number of samples
        print("Untuk metode brute force, jumlah nilai 7 akan disamakan dengan metode divide and conquer. \nMisal 3 iterasi akan menggunakan 2^3 - 1 = 7 variansi nilai t.")
        num_samples = int(input("Masukkan jumlah iterasi: "))
        

        if method == "1":
            num_samples = pow(2,num_samples) + 1
            plotBezierCurveBruteForce(Points, num_samples)
        else: 
            interval = float(input("Masukkan interval waktu: "))
            plotBezierCurveDnC(Points, num_samples, interval)
        # Plot the Bézier curve
    except ValueError as ve:
        print("Error:", ve)
        print("Please enter valid numeric values for coordinates and number of samples.")

if __name__ == "__main__":
   
    main()
    
    
