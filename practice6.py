stops = """the
is
at
on
a
and"""

story = """The cat sat on the mat. 
The cat is a good cat. 
Is the dog on the mat? No, the dog is at the park."""

with open("stopwords.txt", "w") as f:
    f.write(stops)

with open("story.txt", "w") as f:
    f.write(story)

stop_words = []
cleaned_words = []

def process(first, second):
    with open(first, 'r') as f, open(second, 'r') as f2:
    
        for stops in f:
            stops = stops.strip().lower()

            stop_words.append(stops)
        for words in f2:
            words = words.strip().lower()
            parts = words.replace('.', '').replace('?', '').replace(',', '').split()
            for part in parts:

                if part not in stop_words:
                    cleaned_words.append(part)
    return cleaned_words

result = process('stopwords.txt', 'story.txt')
        

def process_summary(cleaned):
    words = []
    counts = []

    for i in range(len(cleaned)):
        if cleaned[i] not in words:
            words.append(cleaned[i])
            count = 0

            for j in range(len(cleaned)):
                if cleaned[i] ==  cleaned[j]:
                    count += 1
        counts.append(count)
    for i in range(len(words)):
         print(f"{words[i]}: {counts[i]}")

process_summary(result)

        

