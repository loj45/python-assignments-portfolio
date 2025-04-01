x=float(input("enter x: "))

def kritikproblem(x):
    k=0
    n=0
    if 0<=x<=1:
        def function(a, b):
            y=((a)**(2*b+1))/(2*b+1)
            return y
        #we're going to run a while loop until the error is <0.001 with n as blabla

        while function(x,n)>0.0001:
            n+=1 #equal to n=n+1
        i=0
        j=0 #current number for the first round of the loop
        k=0 #calculated number, after summation

        for i in range(n):
            j=(((-1)**int(x))*(int(x)**((2*i)+1)))/((2*i)+1)
            k+=j

    else:
        print("Error!") #because input is not within bounds [0,1]

    return (k,n, function(x,n))

print(kritikproblem(x))