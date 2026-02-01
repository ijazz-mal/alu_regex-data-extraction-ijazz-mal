import re

with open("inputs.txt", "r", encoding="utf-8") as f: #the utf-8 encoding is used to support special characters like ₹ and €
    txt = f.read()

timepattern = r"\b((?:(?:0?[1-9]|1[0-2]):[0-5][0-9]\s?(?:AM|PM|am|pm))|(?:(?:[01][0-9]|2[0-3]):[0-5][0-9]))\b" #time patterns like "23:59" or "11:30 AM"
time_candidates = re.findall(timepattern, txt)

URLpattern = r"\b(https?://[^\s<>#%~`\"]+\s)" #URLs starting with http or https excluding spaces and certain special characters
URL_candidates = re.findall(URLpattern, txt)

hashtagpattern = r"(#[A-Za-z0-9_]+)" #hashtags like #example_01
hashtag_candidates = re.findall(hashtagpattern, txt)
print("Time Candidates:", time_candidates)
print("URL Candidates:", URL_candidates)
print("Hashtag Candidates:", hashtag_candidates)