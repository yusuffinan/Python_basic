class kumanda():
    def __init__(self, kanallistesi):
        self.kanallistesi = kanallistesi
        self.index = -1
    def __iter__(self):
            return self
    def __next__(self):
            self.index += 1
            if self.index < len(self.kanallistesi):
                return self.kanallistesi[self.index]
            else:
                self.index = -1
                raise StopAsyncIteration
        
kumandaa = kumanda(["atv","trt","show","fox","ynei"])
itt = iter(kumandaa)
for i in kumandaa:
     print(i)