import random
import string

def generate_password(length, complexity="strong"):
    if complexity == "strong":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits
    elif complexity == "weak":
        characters = string.ascii_lowercase  # Only lowercase letters for weak passwords
    else:
        raise ValueError("Invalid complexity level. Choose from 'strong', 'medium', or 'weak'.")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    if length <= 0:
        print("Password length must be greater than 0.")
        return
    
    complexity = input("Enter the desired complexity (strong/medium/weak): ").lower()
    
    if complexity not in ["strong", "medium", "weak"]:
        print("Invalid complexity level. Please choose from 'strong', 'medium', or 'weak'.")
        return

    password = generate_password(length, complexity)
    print("Your generated password is:")
    print(password)

if __name__ == "__main__":
    main()
