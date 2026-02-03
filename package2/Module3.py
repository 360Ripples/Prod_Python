def sayHello():
    return "Hello its me";

def sayBye():
    print("Bye Bye!");

# if this Module 3 is executed using the Py command the 
#__name__ will have the value __main__
# if the module is executed from some other class in our example
# from package 1 module 2 this will have the value as the module name
# name __name__ will have the value package2.Module3

print(__name__);
if __name__ == "__main__":
    sayBye()

