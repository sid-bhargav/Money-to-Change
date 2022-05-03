## CLASSES
class Change:
    def __init__(self, hundred, fifty, twenty, ten, five, dollar, quarter, dime, nickel, penny):
        self.c = [hundred, fifty, twenty, ten, five, dollar, quarter, dime, nickel, penny]
    def __init__(self, money):
        ratio_list = [100, 50, 20, 10, 5, 1, 0.25, .10, .05, 0.01]
        c_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(len(ratio_list)):
            ## The list goes through all values of the list and makes sure that it takes how many times that value fits in the current sum of money
            c_list[i] = int(money/ratio_list[i])
            ## The value of money is then adjusted by the amount added to the list so that subsequent values are correct
            money = money % ratio_list[i]
            self.c = [c_list[0], c_list[1], c_list[2], c_list[3], c_list[4], c_list[5], c_list[6], c_list[7], c_list[8], c_list[9]]
    def __str__(self) -> str:
        ## Simplifies the to string method and also makes it easier to only print the bills/coins that actually are due. Seperated into single and plural for prettiness
        change_string_list_s = [" Hundred", " Fifty", " Twenty", " Ten", " Five", " Dollar", " Quarter", " Dime", " Nickel", " Penny"]
        change_string_list_p = [" Hundreds", " Fifties", " Twenties", " Tens", " Fives", " Dollars", " Quarters", " Dimes", " Nickels", " Pennies"]
        change_string = ""
        for i in range(len(self.c)):
            if (self.c[i] != 0):
                ## if the value is just one then it will get the string from the singles list
                if(self.c[i] == 1):
                    change_string += str(self.c[i]) + change_string_list_s[i] + ", "
                ## if the value is > 1 then it will get the string from the singles list
                else: 
                    change_string += str(self.c[i]) + change_string_list_p[i] + ", "
        return change_string[0:len(change_string)-2]

## CODE
print(Change(37.49))