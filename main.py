MAX_LINES = 3

def deposit():
    while True:
        amount = input("Hvor mye vil du sette inn? $")
        if amount.isdigit():
            amoun = int(amount)
            if amount >= 0:
                break
            else:
                print("du må sette inn mer enn 0")
            
    return amount

def get_number_of_lines():
        while True:
             lines = input("Hvor mange linjer vil du vedde på (1-" + str(MAX_LINES) + ")? ")
              if lines.isdigit():
                  lines = int(lines)
                   if 1 <= lines <= MAX_LINES:
                         break
                else:
                print("du må sette inn mer enn 0") 
       
    return lines
            


def main():
    balance = deposit()
    lines = get_number_of_lines
    print(balance, lines)

main()