class Conversion:
    def convert(self, num1: int, num2: int) -> int:
        if num1 < num2:
            num1, num2 = num2, num1
        bin1 = bin(num1)[2:]
        bin2 = bin(num2)[2:]
        rest = len(bin1) - len(bin2)
        for i in range(rest):
            bin2 = '0' + bin2
        counter = 0
        for i in range(len(bin1)):
            if bin1[i] != bin2[i]:
                counter += 1
        return counter