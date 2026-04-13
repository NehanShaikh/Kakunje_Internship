# Laptop Configuration
class Laptop:
    def __init__(self, ram, processor, storage):
        self.ram = ram
        self.processor = processor
        self.storage = storage

    def display(self):
        print("RAM:", self.ram)
        print("Processor:", self.processor)
        print("Storage:", self.storage)

l1 = Laptop("16GB", "Intel i5", "512GB SSD")
l1.display()
