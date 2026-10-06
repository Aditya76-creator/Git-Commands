class BinarySemaphore:
    def __init__(self):
        self.value = 1
        self.queue = []

    def wait(self, process):
        if self.value == 1:
            self.value = 0
            print(process, "got the resource")
        else:
            self.queue.append(process)
            print(process, "is waiting")

    def signal(self):
        if len(self.queue) > 0:
            process = self.queue.pop(0)
            print(process, "got the resource from queue")
        else:
            self.value = 1


class CountingSemaphore:
    def __init__(self, value):
        self.value = value
        self.queue = []

    def wait(self, process):
        if self.value > 0:
            self.value -= 1
            print(process, "got the resource")
        else:
            self.queue.append(process)
            print(process, "is waiting")

    def signal(self):
        if len(self.queue) > 0:
            process = self.queue.pop(0)
            print(process, "got the resource from queue")
        else:
            self.value += 1


print("BINARY SEMAPHORE")

binary = BinarySemaphore()

binary.wait("Process 1")
binary.wait("Process 2")
binary.wait("Process 3")

binary.signal()
binary.signal()
binary.signal()


print("\nCOUNTING SEMAPHORE")

counting = CountingSemaphore(3)

counting.wait("Process 1")
counting.wait("Process 2")
counting.wait("Process 3")
counting.wait("Process 4")
counting.wait("Process 5")

counting.signal()
counting.signal()
