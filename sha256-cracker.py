from pwn import *
import sys



if len(sys.argv) != 2:
    print("Invalid arguments!")
    print(">> {} <sha256sum>".format(sys.argv[0]))
    sys.exit()

wanted_hash = sys.argv[1]
password_file = "/usr/share/wordlists/rockyou.txt"
attempts = 0

with log.progress("Attempting to crack hash: {}!\n".format(wanted_hash)) as p:
    with open(password_file, "r", encoding="latin-1") as password_list:
        for password in password_list:
            password = password.strip("\n").encode("latin-1")
            password_hash = sha256sumhex(password)

            if password_hash == wanted_hash:
                p.success("Password hash found after {} attempts!".format(attempts))
                print("Password: {}".format(password.decode("latin-1")))
                exit()

            attempts += 1
            p.status("Attempts: {}".format(attempts))

        p.failure("Password hash not found!")


