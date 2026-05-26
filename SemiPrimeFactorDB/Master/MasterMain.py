from Master import Master
import time
def main():
    logFile = "log_file.txt"
    digit = 99
    batchSize = 1000
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
                with open(logFile,"w") as file:
                    file.write(str(count))
            else:
                continue
        time.sleep(1)
    except KeyboardInterrupt:
        count = master.resultCount
        print("Count: " + str(count))
    except Exception as e:
        print(f"\nError encountered: {e}")
        time.sleep(10)     



if __name__ == "__main__":
    main()
