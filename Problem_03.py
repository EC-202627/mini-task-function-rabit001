def calculate_fine(book_title, days_overdue, daily_rate=5.0, max_fine=150.0):
    fine = days_overdue * daily_rate
    capped = False
    if fine > max_fine:
        fine = max_fine
        capped = True
    return fine, capped

book_title = input()
days_overdue = int(input())

fine, capped = calculate_fine(book_title, days_overdue)

print(f"Book: {book_title}")
print(f"Days overdue: {days_overdue}")
print(f"Fine: Rs. {fine}")
if capped:
    print(f"You have accumulated the maximum fine of INR: {fine}")
