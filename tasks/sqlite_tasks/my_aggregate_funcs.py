class Average:
    """Aggregate average func"""
    def __init__(self):
        """Initialize the aggr function"""
        self.average = 0
        self.count = 0

    def step(self, value):
        """Add a value to the container"""
        self.average += value
        self.count += 1

    def finalize(self):
        """Finalize the aggr"""
        return int(self.average / self.count)


class FieldConcatenation:
    """Concatenate multiple fields"""
    def __init__(self):
        """Initialize the aggr function"""
        self.fields = ""

    def step(self, value):
        """Add a value to the container"""
        self.fields += str(value)

    def finalize(self):
        """Finalize the aggr"""
        return self.fields
