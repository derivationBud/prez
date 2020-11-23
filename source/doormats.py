answer=input("What size of door mat do you want ? ")
N=int(answer) # Must be integer
assert N%2==1 # Must be odd

def design(row,N):
    return  ((N//2-row)*"---"
            +(2*row+1 )*".|."
            +(N//2-row)*"---")

padding=((3*N-len("WELCOME"))//2)*"-"

for row in range(N//2): print(design(row,N))
print( padding+"WELCOME"+padding)
for row in range(N//2-1,-1,-1): print(design(row,N))
