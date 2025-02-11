class digit:
    def calculate(self, x):
        return x + int(str(x)*2) + int(str(x)*3) + int(str(x)*4)
    
result = digit()
print(result.calculate(3))