reminders = []

def add_reminder():
    task = input("Enter reminder task: ")
    time = input("Enter reminder time: ")
    reminders.append({"task": task, "time": time})
    print("Reminder added")

def view_reminders():
    if not reminders:
        print("No reminders set")
    else:
        for reminder in reminders:
            print("Task:", reminder["task"], "| Time:", reminder["time"])

def main():
    while True:
        print("1. Add Reminder")
        print("2. View Reminders")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_reminder()
        elif choice == "2":
            view_reminders()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
