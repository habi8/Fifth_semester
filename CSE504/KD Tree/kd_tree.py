class Node:
    def __init__(self, point, axis, left=None, right=None):
        self.point = point
        self.axis = axis
        self.left = left
        self.right = right

def build_kd_tree(points, depth=0):
    if not points:
        return None

    # Select axis based on depth so that axis cycles through all dimensions
    k = len(points[0])  # Dimension of the data
    axis = depth % k

    # Sort points by the selected axis and choose the median as pivot
    points.sort(key=lambda x: x[axis])
    median = len(points) // 2

    # Create node and recursively build left and right subtrees
    return Node(
        point=points[median],
        axis=axis,
        left=build_kd_tree(points[:median], depth + 1),
        right=build_kd_tree(points[median + 1:], depth + 1)
    )

def distance_squared(point1, point2):
    return sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2))

def find_nearest(kd_tree, target_point, best=None):
    if kd_tree is None:
        return best

    axis = kd_tree.axis
    next_best = None
    next_branch = None

    # Update best point
    if best is None or distance_squared(target_point, kd_tree.point) < distance_squared(target_point, best):
        next_best = kd_tree.point
    else:
        next_best = best

    # Choose the branch to search next
    if target_point[axis] < kd_tree.point[axis]:
        next_branch = kd_tree.left
        opposite_branch = kd_tree.right
    else:
        next_branch = kd_tree.right
        opposite_branch = kd_tree.left

    # Explore the next branch
    next_best = find_nearest(next_branch, target_point, next_best)

    # Check if we need to explore the opposite branch
    if (target_point[axis] - kd_tree.point[axis]) ** 2 < distance_squared(target_point, next_best):
        next_best = find_nearest(opposite_branch, target_point, next_best)

    return next_best

# Define specific 10 points
points = [
    [2, 3],
    [5, 4],
    [9, 6],
    [4, 7],
    [8, 1],
    [7, 2],
    [6, 8],
    [3, 5],
    [1, 4],
    [0, 6]
]

# Build the KD-Tree
kd_tree = build_kd_tree(points)

# Define the target point
target = [3, 4]

# Find the nearest neighbor
nearest = find_nearest(kd_tree, target)
print(f"Nearest point to {target} is {nearest}")
