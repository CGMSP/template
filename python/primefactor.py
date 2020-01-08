def primeFactors(n):  #Define function primeFactors with parameter n
    while n % 2 == 0:  #While n is divisable by 2,
        print (2), #print 2 as one of the prime factors,
        n = n / 2 #Divide n by 2
    for i in range(3,int(math.sqrt(n))+1,2): #start a loop in which variable i becomes a different prime number every time loop is repeated
        while n % i== 0: #While n is divisible by i, 
            print (i), #Print i
            n = n / i  #Divide n by i     
    if n > 2: # If n is greater than 2
        print (n) #Print n
