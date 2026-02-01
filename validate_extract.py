import re

with open("inputs.txt", "r", encoding="utf-8") as f: #the utf-8 encoding is used to support special characters like ₹ and €
    txt = f.read()

timepattern = r"\b((?:(?:0?[1-9]|1[0-2]):[0-5][0-9]\s?(?:AM|PM|am|pm))|(?:(?:[01][0-9]|2[0-3]):[0-5][0-9]))\b" #time patterns like "23:59" or "11:30 AM"
valid_time = re.findall(timepattern, txt)

URLpattern = r"\b(https?://[^\s<>#%~,`\"]+)\b" #URLs starting with http or https excluding spaces and certain special characters
URL_candidates = re.findall(URLpattern, txt)

hashtagpattern = r"(#[A-Za-z0-9_]+)" #hashtags like #example_01
hashtag_candidates = re.findall(hashtagpattern, txt)

telpattern = r"\b([+]?[\d\s-]{8,})" #minimal digits being 8 for a phone number with optional +, spaces or dashes
tel_candidates = re.findall(telpattern, txt)

moneypattern = r"\s([$₹€£¥]{1}(?:\s)?[\d,.]+(?:\d{1,2})?|[\d,.]+(?:\d{1,2})?(?:\s)?[$€£¥₹]{1})"#currency patterns like $12.00 or 12.34$
money_candidates = re.findall(moneypattern, txt)

HTMLpattern =  r"<(?:\/)?\w+(?:\s\w+=\"(?:[A-Za-z0-9-._@%#&*:\s]+)?\")?(?:\s+)?(?:\/)?>"#HTML tags like <div class="example"> or </p> or <img src="image.png" />
HTML_candidates = re.findall(HTMLpattern, txt)

#---------------------------------EXTRACTION DONE!!!!-------------------------------------------------------

def validate_phonenumber(candidate: str) -> str | None:
    
    digits = re.sub(r"[^\d]", "", candidate) #remove spaces and dashes
    
    if not digits.isdigit():  #check if all characters remaining are digits
        return None

    if not 8 <= len(digits) <= 15: #check length
        return None
    
    if len(set(digits)) == 1:  #reject patterns like 1111111111 or 0000000000
        return None

    if digits in ("1234567890","0123456789","9876543210","123123123123"): #reject simple sequences
        return None
    
    censored = "*" * (len(digits) - 4) + digits[-4:] #mask output fot privacy

    return censored

def validate_url(url: str) -> bool:  #rejects URLs that are too short to be plausible.

    url = url.strip()  #remove leading/trailing blankspace

    if len(url) < 10:  #minimal plausible URL length
        return False
    return True

def validate_hashtag(tag: str) -> bool:  #rejects hashtags that are too long.

    if len(tag) > 100:
        return False
    return True

import re

def validate_currency(candidate: str) -> str | None:

    candidate = candidate.strip()
    
    number = re.sub(r"[$₹€£¥\s]", "", candidate)  #remove currency symbol and spaces

    if re.search(r"\d,\d{0,2},", number):  #reject multiple commas in wrong places
        return None
    if re.search(r"\d\.\.", number):  #reject multiple periods in wrong places
        return None
    
    return candidate


#treating HTML tags as plain text to prevent accidental execution .
safe_HTML = [tag for tag in HTML_candidates]


valid_URL = []
valid_tel = []
valid_tag = []
valid_money = []
valid_HTML = safe_HTML

for candidate in tel_candidates:
    result = validate_phonenumber(candidate)
    if result:
        valid_tel.append(result)

for candidate in URL_candidates:
    result = candidate.strip()
    if validate_url(result):
        valid_URL.append(result)

for candidate in hashtag_candidates:
    result = candidate.strip()
    if validate_hashtag(result):
        valid_tag.append(result)

for candidate in money_candidates:
    result = validate_currency(candidate)
    if result:
        valid_money.append(result)

#---------------------------------VALIDATION DONE!!!!-------------------------------------------------------

with open("outputs.txt", "w", encoding="utf-8") as f:
    f.write("Time:\n" + "\n".join(valid_time) + "\n\n")
    f.write("URLs:\n" + "\n".join(valid_URL) + "\n\n")
    f.write("Hashtags:\n" + "\n".join(valid_tag) + "\n\n")
    f.write("Phone Numbers:\n" + "\n".join(valid_tel) + "\n\n")    
    f.write("Money Amounts:\n" + "\n".join(valid_money) + "\n\n")
    f.write("HTML Tags:\n" + "\n".join(safe_HTML) + "\n")

#---------------------------------OUTPUTS DONE!!!!-------------------------------------------------------