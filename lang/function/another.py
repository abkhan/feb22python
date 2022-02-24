#define a function
def say_hello(name):
    print("Hello %s, how you doing?" % name)

#define an array/list

name_list = ["myname", "yourname", "hername", "hisname"]

# iterate over the list

for name in name_list:
    if name == "myname":
        print("oh, its my name")
    say_hello(name)
