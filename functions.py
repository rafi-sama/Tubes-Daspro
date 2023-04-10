def len_count(x):

    N = 0

    for i in x:
        N += 1
    
    return N

def split(data, separator):

    NSeparator = 0

    len = len_count(data)
    
    for i in range(len):
        if data[i] == separator:
            NSeparator += 1
        
    tempArr = ["" for i in range(NSeparator + 1)]
    tempElement = ""
    kolom = 0

    for i in range(len):

        if data[i] == separator:
            
            tempArr[kolom] = tempElement
            tempElement = ""
            kolom += 1

        elif i == len-1 :
        
            tempArr[kolom] = tempElement

            break
        else:

            tempElement += data[i]
        
    return tempArr
