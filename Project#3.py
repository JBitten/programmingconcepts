# Create seats (1–20), all start as available
seats = [False] * 20

total_cost = 0

while True:
    print("\nSeat Map (X = taken, O = available):")

    for i in range(20):
        if seats[i]:
            print("X", end=" ")
        else:
            print(i + 1, end=" ")
    print()

    choice = input("\nSelect a seat (1-20) or type 0 to quit: ")

    if choice == "0":
        break

    seat_num = int(choice)

    if seat_num < 1 or seat_num > 20:
        print("Invalid seat number.")
        continue

    if seats[seat_num - 1]:
        print("Seat already taken. Choose another.")
        continue

    # Emergency seats (rows 9-10 → seats 9 and 10 for simplicity)
    if seat_num == 9 or seat_num == 10:
        confirm = input("This is an emergency seat. Can you assist in an emergency? (yes/no): ")
        if confirm.lower() != "yes":
            print("You cannot select this seat.")
            continue

    # First class seats (1-5)
    if seat_num >= 1 and seat_num <= 5:
        print("First class seat selected. Fee: $50")
        total_cost += 50
    else:
        print("Regular seat selected. No fee.")

    seats[seat_num - 1] = True
    print("Seat", seat_num, "successfully booked!")

print("\nBooking complete.")
print("Total cost: $", total_cost)

print("Your seats:")
for i in range(20):
    if seats[i]:
        print(i + 1, end=" ")