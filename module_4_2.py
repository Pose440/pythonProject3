
def test_function(x):
    a = 10/2
    def inner_function(x):
        if a == 5:
            print("Я в области видимости функции test_function")
    inner_function(x)

inner_function()