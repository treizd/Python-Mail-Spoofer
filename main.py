# Python mail spoofer - Power API for mail-spoofing
# Copyright (c) 2025 Treizd
#
# This file is part of python-mail-spoofer project.
#
# Python mail spoofer is free software: you can redistribute it and/or modify
# it under the terms of the MIT License. See the LICENSE file for details.


import asyncio
import aiohttp

recipient = "john_dae@example.com"
sender = "fbi@gov.us"
message = "You are being arrested!"
subject = "Read as soon as possible"
base_url = 'https://my-website.com/index.php'
proxy = "http://qwErTy:AsDfGHj@123.45.67.89:8000" # Or delete if not needed

async def send_email(recipient, sender, message, subject, base_url, proxy=None):
    params = {
        'a': recipient,
        'e': sender,
        'c': message,
        'b': subject
    }

    url = f"{base_url}?{urlencode(params)}"

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        try:
            async with session.get(url, proxy=proxy, timeout=10) as response: # Delete proxy keyword if not needed
                response.raise_for_status() 
                return await response.text()
        except aiohttp.ClientError as e:
            print(f"Error sending email request: {e}")
            return None
        except asyncio.TimeoutError:
            print("Timeout error while sending email")
            return None
        except Exception as e:
            print(f"An unexpected error while sending email: {e}")
            return None
async def main():
  result = await send_email(recipient, sender, message, subject, base_url, proxy)
  if result:
    print("Successfully sent!")
  else:
    print("Could not send the email")

asyncio.run(main())
