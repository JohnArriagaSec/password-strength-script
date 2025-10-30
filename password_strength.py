print("Password strength detector")

password = input("enter your password: (Must include at least a symbol one capital and one lower case and a symbol)")

common_passwords = {
    "123456","password","123456789","12345678","12345","qwerty",
    "111111","1234567","iloveyou","sunshine","qwerty123","admin",
    "welcome","monkey","letmein"
}

SEQ_PATTERNS = [
    "0123456789", "abcdefghijklmnopqrstuvwxyz",
    "qwertyuiop", "asdfghjkl", "zxcvbnm"
]

SYMBOLS = r"""!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""



has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower()for c in password)
has_digit = any(c.isdigit() for c in password)
has_symbol = any(c in SYMBOLS for c in password)

is_common = password.lower() in common_passwords

def has_sequence(s, seq_len=4):
    s = s.lower()
    for seq in SEQ_PATTERNS:
        for i in range(len(seq) - seq_len + 1):
            piece = seq[i:i+seq_len]
            print("checking piece:", piece) #see what it is checking
            if piece in s or piece[::-1] in s:
                print("found sequence:", piece)
                return True, piece
    return False, None

seq_found, seq_piece = has_sequence(password)


#output lines

if is_common:
    print("this was detected to be a common password do not use it")
elif not (has_upper and has_lower and has_digit and has_symbol):
    print(f"did not fit the requirements please check again:", password,"requirements:(Must include at least a symbol one capital and one lower case and a symbol)")
else:
    print("Passwords meets all requirements")

if seq_found:
    print(f"your password has been detected with a common sequence change immediately!",seq_piece)