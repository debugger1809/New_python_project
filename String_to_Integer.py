class Solution:
    def myAtoi(self, str_):
        """
        :type str: str
        :rtype: int
        """
        str_ = str(str_)
        #remove whitespace
        str_ = str_.strip()
    
        if (len(str_) == 0):
            return 0
    
        result = 0 
        flag = 1
        if (str_[0]<'0' or str_[0]>'9') and (str_[0] != '-' and str_[0] != '+'):
            return 0
        else:
            if str_[0] == '-':
                flag = -1
            elif str_[0] == '+':
                flag = 1
            else: 
                result = int(str_[0])
        
            for i in range(1,len(str_)):    #(line27)- just a reference pointer
                if (str_[i] == ' ' or str_[i]<'0' or str_[i]>'9'):
                    break
                else:    
                    result = result*10 + int(str_[i])
 
            if flag==1:
                if result <= 2**31-1:
                    return result
                return (2**31-1)
            else:
                if result*flag >= -2**31:
                    return result*flag
                return -2**31
