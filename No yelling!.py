# def filter_words(st):
#     a = st.lower()
#     b = a.upper([0])
#     c = b.split()
#     return " ".join(c)

def filter_words(st):
    return " ".join(st.split()).capitalize() 