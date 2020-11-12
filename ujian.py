

def phone_number():
    x = str(input("masukan nomor anda: "))
    # y = str('-1','-2','-3','-4','-5','-6','-7','-8','-9')
    nomor = len(x)+1
    # print(nomor)
    
    if nomor != 10:
        print("Digits must bein length of 10, not more or less")
    elif x.isalpha() == True:
        print("no alphabet")  
    elif x == '-'  :
        print('Input only positive number')
    elif x.isascii() == True:
        print('no symbol')
    else:
        print() 

    print(f'({x[:3]}) {x[3:6]}-{x[6:]}')

phone_number()    

def move_zero(num_list):

    num_zero = [0 for i in range(num_list.count(0))]
    x = [ i for i in num_list if i != 0]
    x.extend(num_zero)
    return(x)

# print(move_zero(['pyhon',1,0,1,True,2,0,1,3,'python']))



class Statistic:

    def __init__(self,mean,median,mode,std):
        self.mean = mean
        self.median = median
        self.mode = mode
        self.std = mode







