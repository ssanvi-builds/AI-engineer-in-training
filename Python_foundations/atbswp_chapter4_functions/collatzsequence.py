def collatz(number): 
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        print(number, end=" ")

def main():
    while True:
        try:
            number_input = input("Please insert a number\n")
            collatz(int(number_input))
            print()
            break
        except ValueError:
            print("Please enter a valid number")

main()