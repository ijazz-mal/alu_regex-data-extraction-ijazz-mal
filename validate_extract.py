import re

with open("input1.txt", "r", encoding="utf-8") as f: #the utf-8 encoding is used to support special characters like ₹ and €
    txt = f.read()

timepattern = r"\b([0-1]?[0-9]:[0-5][0-9](?:\s(AM|PM|am|pm))?|2[0-4]:[0-5][0-9](?:\s(AM|PM|am|pm))?)" #time patterns like "23:59" or "11:30 AM"