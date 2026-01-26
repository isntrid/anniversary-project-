import glob
import json
import re
import csv

messages_path = r"C:\Users\ridn1\Visual Studio Code\anniversary project\Messages"
json_files = glob.glob(messages_path + '/**/*.json', recursive=True)

msgs = []

suited = []

for path in json_files:
    if 'channel' in path:
        with open(path, 'r', encoding='utf-8') as channels:
            line = channels.readline()
            if "1441233100473503805" in line or "798933998499135538" in line:
                suited.append(path)

for channel_path in suited:
  
    path = f"{channel_path[:-12]}messages.json"
    with open(path, 'r', encoding='utf-8') as m_file:
        all_messages = json.load(m_file)
        for message in all_messages:
            if "Contents" in message:
                msgs.append(message["Contents"])

csv_file = 'comments.csv'
with open(csv_file, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for m in msgs:
        writer.writerow([m])

def load_messages():
    with open(csv_file, encoding="utf-8") as f:
        msgs = [line.strip() for line in f]
    return msgs

def average_words(msgs):
    if not msgs:
        return 0
    return sum(len(m.split()) for m in msgs)

def search_messages(msgs, word):
    pattern = re.compile(rf"\b{re.escape(word)}\b", re.IGNORECASE)
    matches = [m for m in msgs if pattern.search(m)]
    matches = sorted(matches, key=len)
    return matches

msgs_from_csv = load_messages()
inp = input('What would you like to search for?')
print("Total words:", average_words(msgs_from_csv))
found = search_messages(msgs_from_csv, inp)
print(f"Found {len(found)} messages containing '{inp}':")
for f in found[:5]:  # show first 5 matches
    print(f)


