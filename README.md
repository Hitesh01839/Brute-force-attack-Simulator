# VigilantCrack - Website Brute Force Simulator

VigilantCrack is a Python script that simulates a brute force attack on a website's login page. This tool is designed for educational and ethical purposes only. **Use it responsibly and only on systems you have explicit permission to test. Unauthorized use is illegal and unethical.**

## Usage

To run VigilantCrack, you need to provide the URL of the target website, the target username, and a list of potential passwords to test.

```bash
python vigilantcrack.py --url <target_url> --username <target_username> --passwords <password_list>
```

## Arguments
- --url: The URL of the target website's login page.
- --username: The target username you want to test.
- --passwords: A text file containing a list of potential passwords, with one password per line.

## Example
```bash
python vigilantcrack.py --url https://example.com/login --username admin --passwords passwords.txt
```

## Disclaimer
This tool is intended for educational and ethical purposes only. Unauthorized testing or use of VigilantCrack on systems without proper authorization is illegal and unethical. Always obtain explicit permission before using this tool on any system.

## Credits
VigilantCrack was created by Ganga Hitesh.