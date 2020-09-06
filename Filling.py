def func4():
    #x = [0, 0, 30, 0, 0, 0, 50, 0, 0]
    #x = [0,0,0,24]
    #x = [80,0,0,0,0]
    x = []
    n = int(input("enter length of list : "))
    for d in range(0,n):
        data = int(input("Enter data : "))
        x.insert(d, data)
    y = []
    cnt = 0
    #list4 = [0, 0, 0, 0, 0]
    list4 = []
    for e in range(0,n):
        list4.insert(e, 0)
    
    indx_0 = list4.index(0)
    for m in range(0,len(x)):        
        if x[m] == 0:
            pass
        else:
            a = 0
            indx = x.index(x[m])
            for j in range(indx_0, (indx + 1)):
                a += 1
                if x[j] != 0:
                    y.insert(j, x[j])
            z = 0        
            
            for k in range(0, len(y)):   
                z += y[k]
            for i in range(indx_0, (indx + 1)):                    
                if i <= indx:
                    list4[i] = z//(a+cnt)
            cnt += 1  
            
            indx_0 = list4.index(0)
            z = list4[indx_0 - 1]
            y.clear()
            y.insert(0, z)
            
            
    for m in range((indx_0 - 1), len(list4)):
        a = 0
        for j in range(indx_0, len(list4)):            
            a += 1            
            if x[j] != 0:
                y.insert(j, x[j])
        z = 0        
        for k in range(0, len(y)):   
            z += y[k]
        for i in range(indx_0 - 1, len(list4)):                    
            list4[i] = z//(a+1)
                
    print(list4)
    

func4()
