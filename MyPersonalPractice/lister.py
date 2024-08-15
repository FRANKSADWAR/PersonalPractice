class ListInstance:
    """
    Min-in class that provides a formatted print() or str()
    of instances via inheritance of __str__, coded here; displays instance attrs only; 
    self is the instance of lowest class;
    uses __X names to avoid clashing with client's attrs

    Each instance has a built-in __class__ attribute that references the class from which it was created from, and each class has a __name__ attribute that 
    references the name in the header.
    The expression self.__class__.__name__ fetches the name of an instance's class.

    This class uses the __dict__ which is exported in instance's attribute dictionary to build up a string showing the names and values of all instance attributes.
    The class uses two additional techniques: 
                                        - It displays the instance's memory address by calling the id built in function
                                        - It uses pseudoprivate naming pattern for it's worker method __attrnames
    """

    def __str__(self):
        return '< Instance of %s, address %s:\n%s>' % (self.__class__.__name__, id(self), self.__attrnames())
    

    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\t name %s=%s' % (attr, self.__dict__[attr])
        return result


class Super:
    def __init__(self):
        self.data1 = 'Spam'
    def ham(self):
        pass

class Sub(Super, ListInstance):
    def __init__(self):
        Super.__init__(self)
        self.data2 = 'Eggs'   # instance attributes
        self.data3 = 42
    def spam(self):
        pass

if __name__ == "__main__":
    X = Sub()
    print(X)
