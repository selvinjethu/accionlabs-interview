class ArrayIntersection:
    def find_common(self, arr1, arr2):
        return sorted(set(arr1) & set(arr2))
    
arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]

intersect = ArrayIntersection()
print(intersect.find_common(arr1,arr2))

add exception handling
