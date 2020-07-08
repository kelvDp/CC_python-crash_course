def make_sandwich(*args):
    # print(f"This sandwich will have some {args}.")
    # another way of doing it:
    print("This sandwich will have some :")
    for arg in args:
        print(arg)

make_sandwich("cheese")
make_sandwich("cheese","Bacon")
make_sandwich("ham","cheese","tomato","bacon","lettuce")
