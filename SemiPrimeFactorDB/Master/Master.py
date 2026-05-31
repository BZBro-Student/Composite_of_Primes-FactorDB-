import subprocess
import time
import sys
import requests
from contextlib import redirect_stdout
from concurrent.futures import ThreadPoolExecutor
from factordb.factordb import FactorDB
from PrimeBatchGenerator import PrimeBatchGenerator
from datetime import datetime
import time
class Master:
    def __init__(self, HostNames, digit, batchSize):
        self.HostNames = HostNames
        self.digit = digit
        self.batchSize = batchSize
        self.batchGen = PrimeBatchGenerator(self.digit,self.batchSize)
        self.resultCount = 0

    
    def SendBatch(self, host):
 
        data = self.batchGen.BatchGen()
        dataStr = "\n".join(data)

        try:
            send = subprocess.Popen(['ssh', host, 'python3 -u Minion.py'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,text= True)
            stdout, stderr = send.communicate(input=dataStr)

            if send.returncode != 0:
                print(f"Error on {host}: {stderr}")
                return None

            return stdout
        except Exception as e:
            print(f"Error on {host}: {stderr}")
            return None

    def SendBatchMulti(self, HostNames):
        results = []
        with ThreadPoolExecutor(max_workers=len(HostNames)) as executor:
            futures = {executor.submit(self.SendBatch, host): host for host in HostNames}
        
        for future in futures:
            currHost = futures[future]
            try:
                returnData = future.result()
                if returnData:
                    for lines in returnData.splitlines():
                        if lines.strip():
                            results.append(lines.split(","))
            except Exception as e:
                print(f"Error on {future}: {e}")
                continue
        return results

    def reportResults(self,string):
        url = "https://factordb.com/report.php"
        payload = {'report': string}
        try:
            response = requests.post(url, data=payload, timeout=10)
            if response.status_code == 200:
                self.resultCount = self.resultCount + 1
                return True
        except Exception as e:
            print(f"Error {e}")
            return False
        return False

    def processResults(self,results):
        for row in results:
            try:
                primeP, primeQ, result = row
                string = f"{result}={primeP}*{primeQ}"
                success = self.reportResults(string)
                if success:
                    time.sleep(0.2)
                else: 
                    time.sleep(1)
            except Exception as e:
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(current_time)
                print(f"Failed attempt {e}")





