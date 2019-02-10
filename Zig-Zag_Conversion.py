class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) == 1 or numRows == 1:
            return s
        list_ = []
        #for the first line
        m = 0
        while m < len(s):
            list_ += [s[m]]
            m += 2*numRows-2
            
        #the mid line
        for i in range(1,numRows-1):
            j=0
            while j < len(s):
                if (i+j) < len(s):
                    list_ += [s[i+j]]
                if i+j+2*numRows-2*(i+1) < len(s):
                    list_ += [s[i+j+2*numRows-2*(i+1)]]
                j += 2*numRows-2
        
        #the last line
        k = numRows - 1
        while k < len(s):
            list_ += [s[k]]
            k += 2*numRows-2
        
        #output
        str_ = ''
        for n in range(len(list_)):
            str_ += str(list_[n])
        return str_
