
def repeat(number_of_times):
    
    def fun2(another_function):
        def wrapper_function(*args, **kargs):
            print("the activities before another function{}".format(another_function))

            for i in range(number_of_times):
                another_function(*args, **kargs)

            print("the activities after another function{}".format(another_function))
        return wrapper_function
    return fun2

@repeat(number_of_times = 3)   # decorator
def fun1(name):
    print("Hello {}, from fun1".format(name))

# fun = fun2(fun1)
fun1("Python")