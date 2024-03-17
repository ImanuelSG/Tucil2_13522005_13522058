def fill_bezier_points(point1, point2, point3, current_step):
    global total_steps
    if current_step < total_steps:
        middle_point1 = calculate_mid_point(point1, point2)
        middle_point2 = calculate_mid_point(point2, point3)
        middle_point3 = calculate_mid_point(middle_point1, middle_point2)
        current_step += 1
        fill_bezier_points(point1, middle_point1, middle_point3, current_step)
        bezier_points.append(middle_point3)
        fill_bezier_points(middle_point3, middle_point2, point3, current_step)

def calculate_mid_point(point1, point2):
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

def generate_bezier_curve(point1, point2, point3):
    global bezier_points
    bezier_points = []
    bezier_points.append(point1)
    fill_bezier_points(point1, point2, point3, 0)
    bezier_points.append(point3)

# Example usage
total_steps = 2
bezier_points = []

point1 = (0, 0)
point2 = (4, 4)
point3 = (8, 0)

generate_bezier_curve(point1, point2, point3)

print(bezier_points)
