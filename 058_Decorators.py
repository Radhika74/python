def greet(fx):
  def mfx(*args, **kwargs): #list of arguments,dic of keyword arguments
    print("Good Morning")
    fx(*args, **kwargs)
    print("Thanks for using this function")
    return fx
  return mfx
@greet
def hello():
  print("Hello, world!")
@greet
def add(a, b):
  print(a+b)
# greet(hello)()
hello()
# greet(add)(1, 2)
add(1, 2)

 