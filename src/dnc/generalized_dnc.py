from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

# Function to calculate mid point between two points
def calculate_mid_point(point1: Point, point2: Point) -> tuple[float, float]:
    return ((point1.x + point2.y) / 2, (point1.x + point2.y) / 2)


# Function to generate all mid points from the given control points
def search_midpoint(points: list[Point], result: list[Point]) -> None:
    if len(points) == 1:
        return
    else:
        new_points = []
        for i in range(len(points) - 1):
            new_points.append(Point((points[i].x + points[i + 1].x) / 2, (points[i].y + points[i + 1].y) / 2))
        result.extend(new_points)
        search_midpoint(new_points, result)


# Function to find the left side control points
def left_control_points(result: list[Point], control_points: list[Point], n: int) -> list[Point]:
    left = [control_points[0]]
    i = 0
    j = 0
    while i < (n - 1):
        left.append(result[j])
        j += n - i - 1
        i += 1

    return left

# Function to find the right side control points
def right_control_points(result: list[Point], control_points: list[Point], n: int) -> list[Point]:
    right = []
    i = 0
    j = len(result) - 1
    while i < (n - 1):
        right.append(result[j])
        j -= (i + 1)
        i += 1
    right.append(control_points[-1])
    
    return right


def create_bezier_points(control_points: list[Point], result_points: list[Point], mid_points: list[Point], iterations: int, n: int) -> None:
    if iterations == 0:
        result = []
        search_midpoint(control_points, result)
        mid_points.append(result[-1])
        return
    else:
        result = []
        search_midpoint(control_points, result)
        result_points.append(result)
        
        left = left_control_points(result, control_points, n)
        create_bezier_points(left, result_points, mid_points, iterations - 1, n)

        right = right_control_points(result, control_points, n)
        create_bezier_points(right, result_points, mid_points, iterations - 1, n)
