name = input(str("pls enter your name:"))
def hello(name):
    if name == "ilay": 
        king = name + " the king!"
        print(f"hello {king}")
    elif name != "ilay":
        print("you " + name + " are not ilay")
hello(name)
