import random

# 1 se 100 ke beech ek random number choose kiya
secret_number = random.randint(1, 100)
attempts = 0

print("--- Guess the Number Game ---")
print("Maine 1 se 100 ke beech ek number socha hai. Guess karo!")

# Loop tab tak chalega jab tak sahi guess nahi milta
while True:
    # User se guess input liya
    guess = int(input("Apna guess enter karo: "))
    attempts += 1  # Har guess par attempt badhega
    
    # Conditions check karna
    if guess < secret_number:
        print("Too Low! Thoda bada number try karo.\n")
    elif guess > secret_number:
        print("Too High! Thoda chhota number try karo.\n")
    else:
        print(f"🎉 Mubarak ho! Aapne {attempts} attempts mein sahi number guess kar liya!")
        break  # Sahi guess hote hi loop khatam
