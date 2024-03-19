import numpy as np

# Define custom exception class
class LengthError(Exception):
    pass

def read_control_points_from_file(filename):
    try:
        filename = "../test/input/" + filename 
        with open(filename, 'r') as file:
            num_points = int(file.readline())
            points = []
            for _ in range(num_points):
                line = file.readline().split()
                if len(line) != 2:
                    raise ValueError("Error: Invalid input format. Silahkan Buat dalam format x y.")
                x, y = map(float, line)
                points.append([x, y])
            if len(points) != num_points:
                raise LengthError("Error: Jumlah titik kontrol tidak sesuai dengan yang diberikan. Silahkan coba lagi.")
            return np.array(points)

    except LengthError as le:
        print(str(le))
        return None
    except FileNotFoundError:
        print(f"Error: File '{filename}' tidak ditemukan, silahkan coba lagi.")
        return None
    except ValueError as e:
        print(str(e))
        print("Pastikan formatnya sebagai berikut:")
        print("Baris pertama = jumlah titik kontrol")
        print("Baris selanjutnya dengan format: ")
        print("x y")
        print("Baca readme untuk informasi lebih lanjut")
        return None
