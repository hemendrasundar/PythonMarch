x = int(input("Enter a number from 0 to 99 \n"))

units = ["","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE","TEN","ELEVEN","TWELVE","THIRTEEN","FOURTEEN","FIFTEEN","SIXTEEN","SEVENTEEN","EIGHTTEEN","NINTEEN"]

tens = ["","","TWENTY","THIRTY","FOURTY","FIFTY","SIXTY","SEVENTY","EIGHTY","NINTY"]

if x == 0:
    print("ZERO")
elif x <= 19 :
    print(units[x])
elif x <= 99 :
    print(tens[x//10] +"  "+ units[x%10])    
else :
    print("invalid input")    



