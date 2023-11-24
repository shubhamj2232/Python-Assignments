def rotate_array(arr, D):
    rotation_index = len(arr) - D
    rotated_array = arr[rotation_index:] + arr[:rotation_index]
    return rotated_array

arr = [1, 2, 3, 4, 5]
D = 2

rotated_arr = rotate_array(arr, D)
print("Sample Output: arr after rotation =", rotated_arr)
