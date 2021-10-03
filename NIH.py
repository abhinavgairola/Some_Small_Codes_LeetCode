
from itertools import permutations

def solution1(N):

    """
    Generate permutation and return the maximum
    """
    Numbers = [ i for i in str(N)]
    

    Maximum = max([int(''.join(list(i))) for i in (set(permutations(Numbers, 3)))])
    
    return Maximum

Input1 = 553
Input2 = 213

Maxi = solution1(Input2)

print("This is the output of first function of the test ---- {}".format(Maxi))
    
def solution2(message, K):
    
    """
    Split the string as per the input length
    """

    Iterator = message.split()

    if 0<K<= len(message):
        CroppedMessage = (' '.join(([ i for i in (message[0:K]).split() if i in Iterator])))
    else:
        CroppedMessage = message


    return CroppedMessage
Input1 = "Codility We test coders"
Input2 = "Why not"
Input3= "The quick brown fox jumps over the lazy dog"



K1 = 14
K2 = 100
K3 = 39

Message = solution2(Input3,K3)
print("This is the output of second function of the test ---- {}".format(Message))


def solution3(S):


    """
    Stack manipulation using the given cases
    """
    Iterator = S.split()

    Stack = []

    for i in Iterator:

        
       
        if i.isdigit():
            Stack.append(int(i))

        if i == '-':

            try:
                Op1 = Stack.pop(-1)
                Op2 = Stack.pop(-1)
                Stack.append(Op1-Op2)
            except:
                return -1
                break

        if i == '+':
            try:
                Op1 = Stack.pop(-1)
                Op2 = Stack.pop(-1)
                Stack.append(Op1+Op2)
            except:
                return -1
                break

        if i == "DUP":
            Stack.append(Stack[-1])
            

        if i == "POP":
            Stack.pop(-1)

      


    return(Stack.pop(-1))



Input1 = "4 5 6 - 7 +"

Input2 = "13 DUP 4 POP 5 DUP + DUP + -"

Input3 ="5 6 + -"

Input4 ="3 DUP 5 - -"
  
FinalAnswer = solution3(Input4)

print("This is the output of third function of the test ---- {}".format(FinalAnswer))