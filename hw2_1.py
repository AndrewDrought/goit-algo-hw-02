import queue
import random

queue = queue.Queue()

def generate_request():
    new_request = random.randint(1, 100)
    queue.put(new_request)
    print(f"Заявка {new_request} додана до черги.")

def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Заявка {request} оброблена.")
    else:
        print("Черга пуста.")


if __name__ == "__main__":
    while True:
        user_input = input("Натисніть 'q' для виходу, або будь-що інше для продовження: ")
        if user_input.lower() == 'q':
            break
        else:
            generate_request()
            process_request()