import re

with open("inputs.txt", "r", encoding="utf-8") as f: #the utf-8 encoding is used to support special characters like ₹ and €
    txt = f.read()

timepattern = r"\b((?:(?:0?[1-9]|1[0-2]):[0-5][0-9]\s?(?:AM|PM|am|pm))|(?:(?:[01][0-9]|2[0-3]):[0-5][0-9]))\b" #time patterns like "23:59" or "11:30 AM"
time_candidates = re.findall(timepattern, txt)

URLpattern = r"\b(https?://[^\s<>#%~`\"]+\s)" #URLs starting with http or https excluding spaces and certain special characters
URL_candidates = re.findall(URLpattern, txt)

hashtagpattern = r"(#[A-Za-z0-9_]+)" #hashtags like #example_01
hashtag_candidates = re.findall(hashtagpattern, txt)

telpattern = r"\b([+]?[\d\s-]{8,})" #minimal digits being 8 for a phone number with optional +, spaces or dashes
tel_candidates = re.findall(telpattern, txt)

moneypattern = r"\s([$₹€£¥]{1}(?:\s)?[\d,]+(?:\.\d{1,2})?|[\d,]+(?:\.\d{1,2})?(?:\s)?[$€£¥₹]{1})"#currency patterns like $12.00 or 12.34$
money_candidates = re.findall(moneypattern, txt)

HTMLpattern =  r"<(?:\/)?\w+(?:\s\w+=\"(?:[A-Za-z0-9-._@%#&*:\s]+)?\")?(?:\s+)?(?:\/)?>"#HTML tags like <div class="example"> or </p> or <img src="image.png" />
HTML_candidates = re.findall(HTMLpattern, txt)

#---------------------------------EXTRACTION DONE!!!!-------------------------------------------------------