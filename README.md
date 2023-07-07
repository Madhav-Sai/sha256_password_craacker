

```markdown
# SHA256 Password Cracker

![SHA256 Password Cracker]

## Overview

The SHA256 Password Cracker is a Python script that attempts to crack a SHA256 hash by comparing it to a list of passwords. It uses the rockyou.txt wordlist to perform the cracking.

## Requirements

- Python 3.x
- `pwn` library
by pip install pwntools 

## Installation

1. Clone the repository:

```shell
git clone https://github.com/Madhav-Sai/sha256_password_cracker.git
```

2. Navigate to the project directory:

```shell
cd sha256-password-cracker
```

## Usage

1. Run the script:

```shell
python sha256_password_cracking.py <sha256sum>
```

Replace `<sha256sum>` with the actual SHA256 hash value you want to crack. The script will attempt to crack the provided SHA256 hash by comparing it to a list of passwords from the `rockyou.txt` file.

Please note that the `rockyou.txt` file is assumed to be located at `/usr/share/wordlists/rockyou.txt`. Adjust the `password_file` variable in the script if the file is located elsewhere.

The script will display the progress of the cracking attempts and indicate whether the password hash was found or not. If a match is found, the password will be displayed.

## Example

To crack a SHA256 hash, run the following command:

```shell
python sha256_password_cracking.py 1f3870be274f6c49b3e31a0c6728957f
```

