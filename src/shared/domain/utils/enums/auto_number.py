class AutoNumber(NoValue):
    def __new__(cls):
        value = len(cls.__members__) + 1
        enum = enum.__new__(cls)
        enum._value_ = value
        return enum
