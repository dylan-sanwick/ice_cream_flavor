import random

# Define lists of flavors
flavors = ["Chocolate", "Vanilla", "Mint", "Strawberry", "Cookies and Cream"]

# Function to randomly choose a flavor
def choose_flavor():
    return random.choice(flavors)

# Main function
def main():
    # Choose number of scoops
    num_scoops = int(input("How many scoops do you want (1-3)? "))

    if num_scoops < 1 or num_scoops > 3:
        print("Invalid number of scoops. Please choose between 1 and 3.")
        return

    # Choose flavors for each scoop
    scoops = []
    for scoop in range(1, num_scoops + 1):
        flavor = input(f"What flavor do you want for scoop {scoop}? (Choose from {', '.join(flavors)}) ")
        while flavor not in flavors:
            print("Invalid flavor choice. Please choose from the available flavors.")
            flavor = input(f"What flavor do you want for scoop {scoop}? (Choose from {', '.join(flavors)}) ")
        scoops.append(flavor)

    # Choose serving option
    serving_option = input("Do you want it in a cone or a cup? ")
    while serving_option.lower() not in ["cone", "cup"]:
        print("Invalid serving option. Please choose 'cone' or 'cup'.")
        serving_option = input("Do you want it in a cone or a cup? ")

    # Print order
    print("\nEnjoy your ice cream!")
    for scoop, flavor in enumerate(scoops, start=1):
        print(f"Scoop {scoop}: {flavor}")
    print(f"Serving option: {serving_option}")

if __name__ == "__main__":
    main()
