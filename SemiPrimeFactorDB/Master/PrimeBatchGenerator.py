from sympy import randprime
import io
class PrimeBatchGenerator:
    def __init__(self, digit, batchSize):
        self.digit = digit
        self.batchSize = batchSize
    
    def BatchGen(self):
        results=[]
        for i in range(self.batchSize):
            prime1 = randprime(10**(self.digit-1),10**(self.digit))
            prime2 = randprime(10**(self.digit-1),10**(self.digit))
            results.append(f"{prime1},{prime2}")
        return results


    