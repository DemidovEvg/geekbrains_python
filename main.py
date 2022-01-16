class myInt(int):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

    def increment(self, value):
        super().__add__(value)

    def __add__(self, value):
        return value




