def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	# Return the element-wise sum of vectors 'a' and 'b'.
	# If vectors have different lengths, return -1.
	c = []
	if len(a)!=len(b):return -1
	for idx in range(len(a)):
		c.append(a[idx]+b[idx])
	return c