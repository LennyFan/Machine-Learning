## logistic implement


def logistic(x,y,test):
        
    w = [ 0.0 for i in range(len(x[0])+1) ]
    alpha = 0.1
    # train
    for e in range(3):
        
        for i in range(len(x)):
            
            power = [-w[j] if j==len(x[0]) else -w[j]*x[i][j] for j in range(len(x[0])+1)]
            shift = max(power)
            
            # prevent underflow 
            hx = 1.0*math.exp(-shift)/(1*math.exp(-shift)+math.exp(sum(power) - shift))
            # dont care
            '''
            try:
                hx = 1.0/(1+math.exp(sum(power)))
            except:
                hx = 1.0
            '''
            for j in range(len(w)):
                if j == len(w)-1:
                    w[j] = w[j] + alpha*(label_y[i] - hx)*1
                else:
                    w[j] = w[j] + alpha*(label_y[i] - hx)*x[i][0]
            
    # test  
    res =[]
    for d in test:
        power = [-w[j] if j==len(x[0]) else -w[j]*d[j] for j in range(len(x[0])+1)]
        shift = max(power)
        
        hx = 1.0*math.exp(-shift)/(1*math.exp(-shift)+math.exp(sum(power) - shift))
       
        #print hx
        if hx >= 0.5:
            res.append(1)
        else:
            res.append(0)
    
    return res
