class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.steps = [0]
        self.version = 0

    def add(self, num: int):
        self.value += num
        if self.version == len(self.steps) - 1: # last value
            self.steps.append(self.value)
        else:
            offset = self.value - self.steps[self.version + 1]
            self.steps[self.version + 1] = self.value
            for i in range(self.version + 2, len(self.steps)):
                self.steps[i] += offset
        self.version += 1

    def subtract(self, num: int):
        self.value -= num
        if self.version == len(self.steps) - 1: # last value
            self.steps.append(self.value)
        else:
            offset = self.value - self.steps[self.version + 1]
            self.steps[self.version + 1] = self.value
            for i in range(self.version + 2, len(self.steps)):
                self.steps[i] += offset
        self.version += 1

    def undo(self):
        if self.version > 0:
            self.version -= 1
            self.value = self.steps[self.version]

    def redo(self):
        if self.version < len(self.steps) - 1:
            self.version += 1
            self.value = self.steps[self.version]

    def bulk_undo(self, steps: int):
        self.version -= steps
        if self.version < 0:
            self.version = 0
        self.value = self.steps[self.version]

    def bulk_redo(self, steps: int):
        self.version += steps
        if self.version > len(self.steps) - 1:
            self.version = len(self.steps) - 1
        self.value = self.steps[self.version]
