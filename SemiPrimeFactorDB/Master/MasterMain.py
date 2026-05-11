from Master import Master
import time
def main():
    digit = 20
    batchSize = 5
    hostNames = ["bzbro@bropiSL1.local","bzbro@bropiSL2.local","bzbro@bropiSL3.local"]
    master = Master(hostNames, digit, batchSize)
    count = 0
    try:
        while 1:
            results = master.SendBatchMulti(hostNames)
            print(results)
            if results:
                master.processResults(results)
                count = master.resultCount
                print(count)
            else:
                continue
    except KeyboardInterrupt:
        count = master.resultCount
        print("Count: " + str(count))
    except Exception as e:
        print(f"\nError encountered: {e}")
        time.sleep(10)     



if __name__ == "__main__":
    main()
