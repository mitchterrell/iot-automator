from _IHub._IHub import IHub


class test(IHub):
    def __init__(self):
        super(test, self).__init__()


my_test = test()
print(my_test.devices)
