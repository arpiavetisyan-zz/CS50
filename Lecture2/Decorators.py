def announce(f):
    def wrapper():
        print("Before calling function")
        f()
        print("After calling function")
    return wrapper

@announce
def hello():
    print("Hello world")

hello()

