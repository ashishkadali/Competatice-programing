# Write the function fun_distance(x1, y1, x2, y2) 
# that takes four int values x1, y1, x2, y2 
# that represent the two points (x1, y1) and (x2, y2), 
# and returns the distance between those points as a int.

import math
def fun_distance(x1, y1, x2, y2):
	# your code goes here
	# a=math.sqrt((((x2-x1)**2)+((y2-y1)**2))*0.5)
	a=(x2-x1)**2
	b=(y2-y1)**2


	return math.floor( math.sqrt(a+b))

	# 3.5=3 /floor
	# 3.5=4 / ceil