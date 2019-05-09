# def areYouPlayingBanjo(name):
#     return (name + " plays banjo" if name[0].lower()=="r" else name + " does not play banjo")

name = input("Are you playing banjo? enter your name:")
if(name.lower().startswith("r")):
    print("plays banjo")
else:
    print("does not play banjo")    