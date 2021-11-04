def medians(nums1, nums2):
    from statistics import median
    list1 = nums1 + nums2
    list1.sort()
    median_of_lists = float(median(list1))
    return median_of_lists

print(medians(nums1, nums2))
