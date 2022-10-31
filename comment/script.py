import json 

# Ask user for youtube url or video id
url = input("Enter a youtube url or video id: ")
url = url.split("watch?v=")[1] if url else 'HW0fY_6GuVU'

print(url)

# Read file comments.json and convert to object
with open('comments.json', 'r') as f:
    comments = json.load(f)

# Loop through comments and print the textDisplay attribute
# filter comments by replyCount > 0
# for comment in filter(lambda c: c['replyCount'] > 0, comments):
#     print(comment['textDisplay'])

# Print keys in comments
print(comments[0].keys())