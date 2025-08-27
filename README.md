![Static Badge](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white)

# Email Sending Script

This script uses `aiohttp` and `asyncio` to send an email via a web endpoint

## AWARE
- In some jurisdictions, spoofing is illegal and subject to legal prosecution; the script author is not responsible for user actions, does not encourage its use, and presents it for informational purposes only

## Prerequisites

- Python 3.7 or higher
- `aiohttp` library: `pip install aiohttp`
- `urllib` library: `pip install urllib`

## Setup of API

1. **Setup your website:**
- Go to `index.php` and transfer it to your site (you should chahge the name, check notes)

## Installation

1. Clone this repository (if you have it on GitHub):
```bash
git clone [repository URL]
```
2. Navigate to the project directory:
```bash
cd [project directory name]
```
3.  **Install Dependencies:**
```bash
pip install aiohttp
```


## Usage
1. Configure the Script:

   - Modify the following variables in the script:
     - recipient: The recipient's email address
     - sender: The sender's email address
     - message: The email body
     - subject: The email subject
     - base_url: The base URL of the web endpoint
     - proxy: (Optional) A proxy server to use (if needed).  Delete if not needed

2. Run the Script:
```bash
python main.py
```
   
## Code Explanation

- send_email(recipient, sender, message, subject, base_url, proxy=None):
   - This asynchronous function sends the email
   - It constructs a URL with the email parameters
   - It uses aiohttp to make an asynchronous GET request to the specified URL
   - It handles potential errors such as aiohttpClientError and asyncioTimeoutError

- main():
   - This asynchronous function calls send_email() with the configured parameters
   - It prints a success or failure message based on the result

## Important Notes

- Ensure the base_url is a valid endpoint that can handle email sending based on the provided parameters
- The script disables SSL verification (ssl=False) for the TCPConnector. Consider enabling it in production for security reasons
- Handle errors appropriately and log them for debugging
- If you are not using a proxy, delete proxy keyword when sending request
- Not all mailers support spoofing. On some of them it will be shown not the sender email, but the ...@your-domain.com or something like that
- Libraries such as `imaplib` does not see spoofed mails

## Recomendations

- Do not write "spam" subjects. If you will, some mailers will just put your mail in a spam-box
- Use proxy. Do not use your real IP-address
- Do not name the .php file "index.php", because otherwise, people can find it and use it without your permission
- Set up main index.html, so when people enter site, they don't see anything suspicious

## License

This project is licensed under the MIT License


## Support

![Static Badge](https://img.shields.io/badge/TON-0098EA?style=for-the-badge&logo=TON&logoColor=white)

`UQB-7m2USzQ451d9orgD4iECLD0FL_BV-zzk3i--bdRl51ho`


![Static Badge](https://img.shields.io/badge/TRC20-50AF95?style=for-the-badge&logo=tether&logoColor=white)

`TUbvCEDE5wpVRsbLmuU8JfkWY4gNcBNbrx`
