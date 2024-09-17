import random

def binary_to_decimal(user_input: int, generated_number: int) -> bool:
    temp_input, index= 0, 0
    while user_input:
        print((user_input % 2))
        temp_input += (user_input % 2) * 2 ** index
        index += 1
        user_input //= 10

    return generated_number == temp_input

def main():
    while True:
        generated_number = random.randint(0, 7)
        print(generated_number)
        user_input = int(input("Enter number in binary: "))

        if not (binary_to_decimal(user_input, generated_number) and 0 <= user_input <= 1111):
            break
# binary_to_decimal(111, 7)

main()