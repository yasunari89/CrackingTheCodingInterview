class StringBuilder:

    def __init__(self):
        self.string_list = []
    
    def append(self, string):
        self.string_list.append(string)
    
    def to_str(self):
        return "".join(self.string_list)


if __name__ == "__main__":
    import time
    import random
    import string

    print("------------TEST------------")
    
    def rand_string(n):
        return "".join(random.choices(string.ascii_letters + string.digits, k=n))
    
    words = [rand_string(10) for _ in range(10000000)]

    start = time.time()
    sentence = ""
    for word in words:
        sentence += word 
    result = sentence
    end = time.time()
    print("string addition by + operation: {}s".format(end - start))

    start = time.time()
    s = StringBuilder()
    for word in words:
        s.append(word)
    result = s.to_str()
    end = time.time()
    print("string addition by StringBuilder: {}s".format(end - start))
