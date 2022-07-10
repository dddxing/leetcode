def maxArea(heights):
	l, r = 0, len(heights)-1

	max_area = 0

	while l < r:

		base = r - l
		height = min(heights[l], heights[r])
		area = base * height
		max_area = max(area, max_area)

		if heights[l] > heights[r]:
			r -= 1
		else:
			l += 1
			
	return max_area

heights = [1,8,6,2,5,4,8,3,7]

print(maxArea(heights))