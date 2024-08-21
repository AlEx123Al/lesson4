from datetime import datetime

def print_current_datetime():
    current_datetime = datetime.now()

    formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

    print(f"urrent date {formatted_datetime}")
print_current_datetime()
