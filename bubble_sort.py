def bubble(int lo, int hi):
	last = lo
	while ++lo < hi:
		if _elem[lo - 1] > _elem[lo]:
			last = lo
			swap(_elem[lo - 1], _elem[lo])
	return last