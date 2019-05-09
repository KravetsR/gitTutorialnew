    
def enough(cap, on, wait):
	return (int(0 if cap - on - wait >=0 else on + wait - cap))