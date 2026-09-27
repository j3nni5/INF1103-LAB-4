def load_orders(filename="inventory.txt"):
    # try to read saved orders; if the file doesn't exist yet, start empty
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            orders = [line.strip() for line in lines if line.strip()]
            return orders
    except FileNotFoundError:
        return []


def save_orders(orders, filename="inventory.txt"):
    # write every order back to the file, one per line
    with open(filename, "w") as f:
        for order in orders:
            f.write(order + "\n")


def get_next_id(orders):
    # first order starts at 1001, otherwise increment the last one
    if not orders:
        return 1001
    last_order = orders[-1]
    last_id = int(last_order.split(",")[0])
    return last_id + 1


def print_orders(orders):
    print("Current Orders:")
    for order in orders:
        parts = order.split(",")
        print(", ".join(parts))
    print("")


def get_product_name():
    # same "keep asking until valid" pattern as get_valid_input(), adapted for text
    failed_attempts = 0
    while True:
        name = input("Enter Product Name (or 'quit' to finish): ").strip()
        if name.lower() == "quit":
            return "quit", failed_attempts
        elif name != "":
            return name, failed_attempts
        else:
            failed_attempts += 1
            print("Error: Please enter a product name.")


def get_quantity():
    # same digit-checking pattern as get_valid_input(), but requires > 0
    failed_attempts = 0
    while True:
        text = input("Enter Quantity: ").strip()
        if text.isdigit() and int(text) > 0:
            return int(text), failed_attempts
        else:
            failed_attempts += 1
            print("Error: Please enter a positive whole number.")


def generate_report(number_orders, rejected_entries):
    print("Total Orders Processed: " + str(number_orders) +
          " Number of Failed/Rejected Entries: " + str(rejected_entries))


# ---- main program ----
orders = load_orders()
rejected_entries = 0
number_orders = 0

while True:
    print_orders(orders)

    name, failed = get_product_name()
    rejected_entries += failed

    if name == "quit":
        save_orders(orders)
        print("All orders saved. Quitting.")
        break

    quantity, failed = get_quantity()
    rejected_entries += failed

    next_id = get_next_id(orders)
    new_order = str(next_id) + "," + name + "," + str(quantity)
    orders.append(new_order)
    number_orders += 1

    print("New Order Added:")
    print(new_order)

    save_orders(orders)
    print("Order successfully saved to inventory.txt")
    print("")

generate_report(number_orders, rejected_entries)