import sys


lower_case = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper_case = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
special_chars = ['!','@','#','$']
digits = ['0','1','2','3','4','5','6','7','8','9']


def generate_pwd(length, num_uppercase, num_lowercase, num_numbers, num_special):
    password = []
    count_uppercase = 0
    count_lowercase = 0
    count_numbers = 0
    count_special = 0


    for i in range(length):
        if count_uppercase < num_uppercase:
            password.append(upper_case[i % len(upper_case)])
            count_uppercase += 1
        elif count_lowercase < num_lowercase:
            password.append(lower_case[i % len(lower_case)])
            count_lowercase += 1
        elif count_numbers < num_numbers:
            password.append(digits[i % len(digits)])
            count_numbers += 1
        elif count_special < num_special:
            password.append(special_chars[i % len(special_chars)])
            count_special += 1

    
    return ''.join(password)

if __name__ == "__main__":   
    if len(sys.argv) != 6:
        print("Usage: python password_generator.py <length> <num_uppercase> <num_lowercase> <num_numbers> <num_special>")
        sys.exit(1)
    
    
    length = int(sys.argv[1])
    num_uppercase = int(sys.argv[2])
    num_lowercase = int(sys.argv[3])
    num_numbers = int(sys.argv[4])
    num_special = int(sys.argv[5])
    
  
  
    password = generate_pwd(length, num_uppercase, num_lowercase, num_numbers, num_special)
    
    print("This is your password:",password)