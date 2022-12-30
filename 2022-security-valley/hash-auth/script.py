from hash_auth import validate_password
import itertools

wordlist = [
    "AICDEV",
    "crypto",
    "hack",
    "hacking",
    "competition",
    "flag",
    "password",
    "pa$$w0rd",
    "pass",
    "hash",
    "authentication",
    "auth",
    "cyber",
    "security",
    "ytiruces",
    "s3curity",
    "s3cur1ty",
    "secur1ty",
    "valley",
    "yellav",
    "va113y",
    "valley",
    "va11ey",
    "vall3y",
    "2022",
    "22",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
    "ctf",
    "sha256",
    "python",
    "vim",
    "as",
    "ide",
]


def validate(password):
    res = validate_password(password)
    if(res):
        print(f'{password}: {res}')
        return password

def main():

    combinations = []
    counter = 0

    for i in range(1,3):
        upperred_wordlist = list(map(lambda item: item.upper(), wordlist))
        titled_wordlist = list(map(lambda item: item.title(), wordlist))
        combinations += list(itertools.permutations(wordlist, i))
        combinations += list(itertools.permutations(upperred_wordlist, i))
        combinations += list(itertools.permutations(titled_wordlist, i))

    for c in combinations:
        password = "_".join(c)
        validate(password)

        password = "-".join(c)
        validate(password)

        password = "".join(c)
        validate(password)

        password = password[0].lower() + password[1:]
        validate(password)

        counter += 4

    print(f'---')
    print(f'Checked {counter} combinations: Failure')

if __name__ == "__main__":
    main()
