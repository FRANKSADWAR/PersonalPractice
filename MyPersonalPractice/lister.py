class ListInstance:
    """
    Min-in class that provides a formatted print() or str()
    of instances via inheritance of __str__, coded here; displays instance attrs only; 
    self is the instance of lowest class;
    uses __X names to avoid clashing with client's attrs

    Each instance has a built-in __class__ attribute that references the class from which it was created from, and each class has a __name__ attribute that 
    references the name in the header.
    The expression self.__class__.__name__ fetches the name of an instance's class.
    """

    def __str__(self):
        return '< Instance of %s, address %s:\n%s>' % (self.__class__.__name__, id(self), self.__attrnames())
    

    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\t name %s=%s' % (attr, self.__dict__[attr])
        return result
