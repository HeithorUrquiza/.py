from statistics import mode

def med(list):
    sum = 0
    for x in list:
        sum += x
    print('\nMédia: {:.2f}'.format(sum/len(list)))

def mediana(list):
    list.sort()
    if (len(list)%2 == 0):
        print("Mediana: {} e {}".format(list[int(len(list)/2 - 1)], list[int(len(list)/2)]))
    else:
        print("Mediana: {}".format(list[int(len(list)/2)]))
        
def moda(list):
    list.sort()
    print(f"Moda: {mode(list)}")