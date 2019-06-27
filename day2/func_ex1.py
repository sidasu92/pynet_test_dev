def my_func(x, y, z=20):
    print( x+y+z )

print ("positional 1, 2, 3 = 6")
my_func(1, 2, 3)

print ("named args: 50")
my_func(y=20, x=10)

print ( "one positional and 2 named, 150")
my_func(100, y=20, z=30)

print ("3 strings, sidhant")
my_func("sid","han", "t")

print ("3 list")
list1 = ["s", "i", "d"]
list2 = ["h", "a", "n"]
list3 = ["t", "_", "_"]
my_func(list1, list2, list3)
