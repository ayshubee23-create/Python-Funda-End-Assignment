# ---------------------------------------------------------------
# Step 1: Preloaded feedbacks
# ---------------------------------------------------------------
feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
    'Feedback': [
        ' Very GOOD Service!!!',
        'poor support, not happy ',
        'GREAT experience! will come again.',
        'okay okay...',
        ' not BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],
    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}
print("original feedback data loaded successfully!")
print("Total feedbacks:", len(feedback_data['Feedback']))


# ---------------------------------------------------------------
# Step 2: Add more feedbacks
# ---------------------------------------------------------------
def read_int(prompt, low=None, high=None):
    """Keep asking until the user enters a valid integer (within range, if given)."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("  Please enter a whole number.")
            continue
        if low is not None and value < low:
            print(f"  Value must be at least {low}.")
        elif high is not None and value > high:
            print(f"  Value must be at most {high}.")
        else:
            return value


def add_feedbacks(data):
    count = read_int("How many more feedbacks do you want to add? ", low=0)
    next_s_no = data['S_No'][-1] + 1          # starts from 11

    for _ in range(count):
        print(f"\n--- Feedback {next_s_no} ---")
        name = input("Name: ").strip()
        text = input("Feedback: ")
        rating = read_int("Rating (1-5): ", low=1, high=5)

        data['S_No'].append(next_s_no)
        data['Name'].append(name)
        data['Feedback'].append(text)
        data['Rating'].append(rating)
        next_s_no += 1


# ---------------------------------------------------------------
# Step 3: Text cleaning
# ---------------------------------------------------------------
def clean_text(text):
    for ch in ['.', ',', '!', '?']:           # remove punctuation
        text = text.replace(ch, '')
    text = ' '.join(text.split())             # collapse multiple spaces + strip ends
    return text.lower()                       # lowercase


def clean_feedbacks(data):
    data['Feedback'] = [clean_text(f) for f in data['Feedback']]


# ---------------------------------------------------------------
# Step 4: Word count insights
# ---------------------------------------------------------------
def count_word_in_feedbacks(word):
    """Return how many feedbacks contain the given word (case-insensitive)."""
    word = word.lower().strip()
    count = 0
    for feedback in feedback_data['Feedback']:
        if word in feedback.lower().split():
            count += 1
    return count


# ---------------------------------------------------------------
# Main program
# ---------------------------------------------------------------
add_feedbacks(feedback_data)
clean_feedbacks(feedback_data)

print("\n===== WORD COUNT INSIGHTS =====")
for w in ['good', 'poor', 'excellent']:
    print(f'Feedbacks containing "{w}": {count_word_in_feedbacks(w)}')

# ---------------------------------------------------------------
# Step 5: Final summary & insights
# ---------------------------------------------------------------
print("\n===== CLEANED FEEDBACK DATA =====")
for key, values in feedback_data.items():
    print(f"{key}: {values}")

average_rating = sum(feedback_data['Rating']) / len(feedback_data['Rating'])
print(f"\nAverage rating: {average_rating:.2f}")

longest_index = 0
for i, feedback in enumerate(feedback_data['Feedback']):
    if len(feedback.split()) > len(feedback_data['Feedback'][longest_index].split()):
        longest_index = i
longest = feedback_data['Feedback'][longest_index]
print(f"\nLongest feedback ({len(longest.split())} words) by "
      f"{feedback_data['Name'][longest_index]}: \"{longest}\"")

unique_words = []
for feedback in feedback_data['Feedback']:
    for word in feedback.split():
        if word not in unique_words:
            unique_words.append(word)
print(f"\nUnique words used ({len(unique_words)}): {unique_words}")

# ---------------------------------------------------------------
# Optional: Sort feedbacks by rating (highest to lowest)
# ---------------------------------------------------------------
print("\n===== FEEDBACKS SORTED BY RATING (HIGH TO LOW) =====")
rows = zip(feedback_data['S_No'], feedback_data['Name'],
           feedback_data['Feedback'], feedback_data['Rating'])
for s_no, name, feedback, rating in sorted(rows, key=lambda r: r[3], reverse=True):
    print(f"{s_no:>2} | {name:<6} | {rating} | {feedback}")