import os 
import re
import urlib.parse

CLIENT_EMAIL = os.getenv("CLIENT_EMAIL","")

KEYWORDS = (
   "gmail", "email", "e-mail", "mail",
    "write an email", "send an email", "draft an email",
    "compose an email", "write mail", "send mail", "draft mail",
    "compose mail"
)

def is_email_command(text):
   text = text.lower()
   return any(k in text for k in KEYWORDS)

def extract_email(text):
    match = re.search(r"[\w.+-]+@[\w.-]+\.\w+", text)
    if match:
        return match.group(0)

    match = re.search(
        r"([\w.+-]+)\s+at\s+([\w.-]+)\s+dot\s+(\w+)",
        text.lower()
    )

    if match:
        return f"{match.group(1)}@{match.group(2)}.{match.group(3)}"
