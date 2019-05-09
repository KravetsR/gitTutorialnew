def enough(cap, on, wait):
    # Your code here
    return (int( 0 if cap - on - wait >=0 else on + wait - cap))