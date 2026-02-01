import re

with open("inputs.txt", "r", encoding="utf-8") as f: #the utf-8 encoding is used to support special characters like ₹ and €
    txt = f.read()

timepattern = r"\b((?:(?:0?[1-9]|1[0-2]):[0-5][0-9]\s?(?:AM|PM|am|pm))|(?:(?:[01][0-9]|2[0-3]):[0-5][0-9]))\b" #time patterns like "23:59" or "11:30 AM"

time_candidates = re.findall(timepattern, txt)
