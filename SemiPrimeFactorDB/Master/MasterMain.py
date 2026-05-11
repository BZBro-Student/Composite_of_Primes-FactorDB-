from Master import Master
def main():
    digit = 99
    batchSize = 1000
    hostNames = ["bzbro@bropiSL1.local","bzbro@bropiSL2.local","bzbro@bropiSL2.local"]
    master = Master(hostNames, digit, batchSize)
    out = master.SendBatch(hostNames[0])
    print(out)


if __name__ == "__main__":
    main()
