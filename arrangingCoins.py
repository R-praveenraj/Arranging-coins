def arrangingCoins(number):
    result=0
    #dummy=1
    while number>=result:
        number-=result
        result+=1
    return result-1

number=int(input())
print(arrangingCoins(number))