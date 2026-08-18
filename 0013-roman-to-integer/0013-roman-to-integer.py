class Solution:
    def romanToInt(self, s: str) -> int:
        val={
            'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000
        }
        lst=list(s)
        total=0
        n=len(lst)
        for i in range(n):
            if i<n-1 and val[lst[i]]<val[lst[i+1]]:
                total=total-val[lst[i]]
            else:
                total=total+val[lst[i]]
        return int(total)