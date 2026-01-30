def display_menu():
    """Displays the menu of options."""
    print("\n--- To-Do List Menu ---")
    print("\n--- Welcome")
    print("\n---Welcome to the To-Do List!---")
    print("1. View To-Do List")
    print("2. Add Item to To-Do List")
    print("3. Mark Item as Completed")
    print("4. Download To-Do List")
    print("5. Exit")

def view_list(todo_list):
    """Displays the current to-do list."""
    print("\n--- Your To-Do List ---")
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        for index, item in enumerate(todo_list, start=1):
            print(f"{index}. {item}")
    print("-----------------------")

def add_item(todo_list):
    """Adds a new item to the to-do list."""
    item = input("Enter the new to-do item: ")
    todo_list.append(item)
    print(f"'{item}' has been added to your to-do list.")

def mark_completed(todo_list):
    """Marks an item as completed (removes it from the list)."""
    view_list(todo_list)
    try:
        item_number = int(input("Enter the number of the item to mark as completed: "))
        if 1 <= item_number <= len(todo_list):
            removed_item = todo_list.pop(item_number - 1)
            print(f"'{removed_item}' has been marked as completed.")
        else:
            print("Invalid item number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def download_list(todo_list, filename=r"saved_lists\todo_list.txt"):
    """Downloads the to-do list to a text file."""
    try:
        with open(filename, 'w') as file:
            for item in todo_list:
                file.write(f"{item}\n")
        print(f"To-do list has been downloaded to '{filename}'.")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

def main():
    """Main function to run the to-do list application."""
    todo_list = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            view_list(todo_list)
            print("Press Enter to return to the menu.")
            input()
        elif choice == '2':
            add_item(todo_list)
            add_more = 'y'
            while add_more == 'y':
                add_more = input("Do you want to add another item? (Y/N): ").strip().lower()
                if add_more == 'y':
                    add_item(todo_list)
                elif add_more != 'n':
                    while add_more not in ['y', 'n']:
                        add_more = input("Invalid input. Please enter 'Y' or 'N': ").strip().lower()
        elif choice == '3':
            mark_completed(todo_list)
        elif choice == '4':
            download_location = input("Enter the filename (with path) to save the to-do list or leave blank for 'saved_lists\todo_list.txt': ")
            if download_location.strip():
                download_list(todo_list, download_location.strip())
            else:
                download_list(todo_list)
        elif choice == '5':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()