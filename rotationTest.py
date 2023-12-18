
import math
def rotate_image(angle):
   
    # Step 2: Define the Rotation Matrix
    angle_rad = math.radians(angle)
    cos_theta = math.cos(angle_rad)
    sin_theta = math.sin(angle_rad)
    rotation_matrix = [
    [cos_theta, -sin_theta
    ],
    [sin_theta, cos_theta
    ]
]
    return rotation_matrix

import numpy as np

# Define the 3D vector (as a column matrix)
vector_3d = np.array([
    [
        1
    ],
    [
        2
    ],
    [
        3
    ]
])

# Define the starting point (as a column matrix)
start_point_3d = np.array([
    [
        4
    ],
    [
        5
    ],
    [
        6
    ]
])

# Calculate the point the vector is facing at
end_point_3d = start_point_3d + vector_3d

# Print the results
print("Starting Point (3D):\n", start_point_3d)
print("Vector (3D):\n", vector_3d)
print("End Point (3D):\n", end_point_3d)
