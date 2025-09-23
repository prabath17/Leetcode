class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        v1arr=version1.split(".")
        v2arr=version2.split(".")

        maxlen=max(len(v1arr),len(v2arr))

        for i in range(maxlen):

            v1=int(v1arr[i]) if i<len(v1arr) else 0
            v2=int(v2arr[i]) if i<len(v2arr) else 0

            if v1<v2:
                return -1
            elif v1>v2:
                return 1

        return 0

        