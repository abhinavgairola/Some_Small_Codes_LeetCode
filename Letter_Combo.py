


class LeetCode:

    def ReturnCombo(self,digits):

        """ This method takes a string containing digits as inputs.
        It then splits it and find the corresponding numbers in a dictionary.
        The dictionary represents the numbers found on a particular phone keypad.
        It then returns the combination of various alphabets found on the keypad.
        An example input can be digits = "23"
        """

        Dictionary = {"2":"abc","3":"def","4":"ghi","5":"jki",
        "6":"mno","7":"pqrs","8":"tuv","9":"wxyz"} ## Dictionary of phone numbers

        SplitDigit = ''


        SplitDigit = ([SplitDigit+i for i in digits])

        Values = ([Dictionary[i] for i in SplitDigit])


        if len(Values) == 1:
            Answer = [ data for data in Values[0]]

        if len(Values) == 2:
            A,B = Values # Unpack and iterate
            Answer = [ data+data1 for data in A for data1 in B]
    
        if len(Values) == 3:
            A,B,C = Values
            Answer = [ data+data1+data2 for data in A for data1 in B for data2 in C]

        if len(Values) == 4:
            A,B,C,D = Values
            Answer = [ data+data1+data2+data3 for data in A for data1 in B for data2 in C for data3 in D]

        if len(Values)==0:
            Answer = []

    

        return Answer

    def Multiply_Complex(self,ip1,ip2):

        """
        Takes two complex numbers as input and multiply them. The inputs are given as strings.
        For example A= "1+-1i", B="1+-1i"
        """

        number1 = [ float(num[0:-1]) if num.endswith('i') else float(num) for num in ip1.split('+')   ]## For leetcode I kept the datatype to be int
        number2 = [ float(num[0:-1]) if num.endswith('i') else float(num) for num in ip2.split('+')   ]

        product = ([num1*num2 for num1 in number1 for num2 in number2])
        answer = str(product[0]-product[3])+'+'+str(product[1]+product[2])+'i'

        return answer
    

    def Power(self, num1, num2):

        """
        Finding powers without using the pow method. This method uses a recursive function
        call to find the power.
        """

        if num2>0:

            if num2==1:
                return num1
            else :
                return num1*self.Power(num1,num2-1)
        else:
            if num2*-1 == 1:
                return num1
            else:
                return 1/(num1*self.Power(num1,(num2*-1)-1))
    
    def multiply(self, str1, str2):

        """
        Multiply two strings without using multiply function.
        """
        #TODO method is not highly optimized.

        

        Dictionary = {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"0":0}

        if len(str2)==1 and len(str1)==1:

            Val1, Val2 = Dictionary[str1],Dictionary[str2]
        
        if len(str1)==1 and len(str2)!=1:
            Data = ''


            Data = ([Dictionary[i] for i in str2])

            print(Data)

            Number = 0
            for i in range(0,len(Data)):

                Number+=(Data[i]*10**((len(Data)-1)-i))

            Val2 = Number
            Val1 = Dictionary[str1]

        if len(str1)!=1 and len(str2)==1:
            Data = ''


            Data = ([Dictionary[i] for i in str1])

            print(Data)

            Number = 0
            for i in range(0,len(Data)):

                Number+=(Data[i]*10**((len(Data)-1)-i))

            Val1 = Number
            Val2 = Dictionary[str2]

        if len(str1)!=1 and len(str2)!=1:
            Data1 = ''
            Data2 = ''


            Data1 = ([Dictionary[i] for i in str1])

            Data2 = ([Dictionary[i] for i in str2])

        

            Number1 = 0
            Number2 = 0
            for i in range(0,len(Data1)):

                Number1+=(Data1[i]*10**((len(Data1)-1)-i))

            for i in range(0,len(Data2)):

                Number2+=(Data2[i]*10**((len(Data2)-1)-i))

            Val1 = Number1
            Val2 = Number2

            



            
        result = 0
        #list1 = [Val1 for i in range(Val2)]
        for i in range(Val2):
            result+=Val1

        #result = sum(list1)

        #print("This is the result",result)

        return result


    

if __name__ == "__main__":

    obj = LeetCode()

    Ans = obj.Power(2,-2)
    print("This is the answer{}".format(Ans))
    print("This is the outputput",obj.multiply("24","24"))
    ## Print docstrings
    print(obj.ReturnCombo.__doc__)




  
        

 
