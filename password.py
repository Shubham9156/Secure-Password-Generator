import string
import secrets

def generate_password(length=12):
    # Define character sets for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure at least one character from each set
    password = [secrets.choice(string.ascii_lowercase),
                secrets.choice(string.ascii_uppercase),
                secrets.choice(string.digits),
                secrets.choice(string.punctuation)]
    
    # Fill the rest of the password with random characters
    password.extend(secrets.choice(characters) for _ in range(length - 4))
    
    # Shuffle the password characters
    secrets.SystemRandom().shuffle(password)
    
    return ''.join(password)

if __name__ == "__main__":
    length = int(input("Enter the desired password length: "))
    password = generate_password(length)
    print("Generated Password:", password)
