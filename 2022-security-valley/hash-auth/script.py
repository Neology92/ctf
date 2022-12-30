from hash_auth import validate_password
import itertools

wordlist = [
    "AICDEV",
    "crypto",
    "auth",
    "crypto",
    "hack",
    "hacking",
    "security",
    "ytiruces",
    "s3curity",
    "valley",
    "yellav",
    "va113y",
    "2022",
    "22",
    "1",
    "2",
    "ctf",
    "competition",
    "flag",
    "password",
    "pass",
    "hash",
    "authentication",
    "cyber",
]


def print_res(res, password):
    if(res):
        print(f'{password}: {res}')
        return password

def main():

    combinations = []
    counter = 0

    for i in range(1,4):
        combinations += list(itertools.permutations(wordlist, i))

    for c in combinations:
        password = "_".join(c)

        res = validate_password(password)
        print_res(res, password)

        password = password.upper()
        res = validate_password(password)
        print_res(res, password)

        password = password.title()
        res = validate_password(password)
        print_res(res, password)

        password = password.replace("_", "")
        res = validate_password(password)
        print_res(res, password)

        password = password[0].lower() + password[1:]
        res = validate_password(password)
        print_res(res, password)

        password = "-".join(c)
        res = validate_password(password)
        print_res(res, password)

        password = password.upper()
        res = validate_password(password)
        print_res(res, password)

        password = password.title()
        res = validate_password(password)
        print_res(res, password)

        counter += 8

    print(f'---')
    print(f'Checked {counter} combinations: Failure')

if __name__ == "__main__":
    main()
