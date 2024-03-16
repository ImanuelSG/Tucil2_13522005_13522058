def mid_point(control_point1, control_point2):
    return (
        (control_point1[0] + control_point2[0]) / 2,
        (control_point1[1] + control_point2[1]) / 2,
    )


def bezier_points(ctrl_points, current_iteration, iterations):
    b_points = []
    if current_iteration < iterations:
        mid_points = [
            mid_point(ctrl_points[i], ctrl_points[i + 1])
            for i in range(len(ctrl_points) - 1)
        ]
        b_points.extend(mid_points)
        new_ctrl_points = [ctrl_points[0]] + mid_points + [ctrl_points[-1]]
        for i in range(len(new_ctrl_points) - 2):
            b_points += bezier_points(
                new_ctrl_points[i: i + 3], current_iteration + 1, iterations
            )
    return b_points


def bezier(ctrl_points, iterations):
    b_points = []
    b_points += bezier_points(ctrl_points, 0, iterations)
    return b_points


# Example usage
iterations = 5
ctrl_points = [(0, 0), (1, 1), (2, 0)]

b_points = bezier(ctrl_points, iterations)

print(b_points)
