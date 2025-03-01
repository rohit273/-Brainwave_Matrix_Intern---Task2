import re
import string
from collections import Counter

def check_password_strength(password: str) -> str:
    length_score = min(len(password) / 8, 1) * 30  # Score based on length
    
    complexity_score = 0
    if any(char.islower() for char in password):
        complexity_score += 10
    if any(char.isupper() for char in password):
        complexity_score += 10
    if any(char.isdigit() for char in password):
        complexity_score += 10
    if any(char in string.punctuation for char in password):
        complexity_score += 10
    
    uniqueness_score = 10  # Default high uniqueness score
    common_passwords = {"password", "123456", "qwerty", "abc123", "letmein, Hitman123456@, Bl@ckMiRRor@123"}
    if password.lower() in common_passwords:
        uniqueness_score = 0  # Very weak if it's a common password
    
    score = length_score + complexity_score + uniqueness_score
    
    if score >= 70:
        return "Strong Password"
    elif score >= 40:
        return "Moderate Password"
    else:
        return "Weak Password"

# Example usage
if __name__ == "__main__":
    user_password = input("Enter your password: ")
    strength = check_password_strength(user_password)
    print(f"Password Strength: {strength}")
