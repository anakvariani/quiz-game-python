import json
import os

USERS_FILE = "users.json"
QUIZ_FILE = "ka_math.json"

# მომხმარებლების მართვა
def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if content:
                return json.loads(content)
    return {}

def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=4)

def register():
    users = load_users()
    username = input("შეიყვანეთ სახელი: ")
    if username in users:
        print("მომხმარებელი უკვე არსებობს!")
        return None
    password = input("შეიყვანეთ პაროლი: ")
    users[username] = password
    save_users(users)
    print("რეგისტრაცია წარმატებით დასრულდა!")
    return username

def login():
    users = load_users()
    username = input("სახელი: ")
    password = input("პაროლი: ")
    if users.get(username) == password:
        print("ავტორიზაცია წარმატებით დასრულდა!")
        return username
    else:
        print("არასწორი სახელი ან პაროლი.")
        return None

# ქუიზის მართვა
def load_quiz():
    with open(QUIZ_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def play_quiz(quiz):
    score = 0
    for q in quiz:
        print("\n" + q["question"])
        choice = input("შეიყვანეთ პასუხი: ").strip()
        if choice == q["answer"]:
            score += 1
    print(f"\nთქვენი ქულა: {score}/{len(quiz)}")

# მთავარი პროგრამა
def main():
    print("მოგესალმებით მათემატიკის ქუიზში!")
    user = None
    while not user:
        action = input("1. რეგისტრაცია\n2. ლოგინი\nაირჩიეთ: ")
        if action == "1":
            user = register()
        elif action == "2":
            user = login()

    quiz = load_quiz()
    while True:
        play_quiz(quiz)
        again = input("გინდა კიდევ ერთი თამაში? (y/n): ")
        if again.lower() != "y":
            print("მადლობა თამაშისთვის!")
            break

if __name__ == "__main__":
    main()
