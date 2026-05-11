import sys

def processIn(dataIn):
    
    for line in dataIn:
        try:
            p,q = line.split(',')
            primeP = int(p)
            primeQ = int(q)
            semiPrime = primeP * primeQ
            print(f"{primeP},{primeQ},{semiPrime}")
        except Exception:
            continue

if __name__ == "__main__":
    dataIn = sys.stdin.read().splitlines()
    processIn(dataIn)