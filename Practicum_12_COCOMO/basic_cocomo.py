print("--- BASIC COCOMO ESTIMATOR ---")

try:
    kloc = float(input("Enter project size in KLOC: "))
    if kloc <= 0:
        raise ValueError("Project size must be greater than zero.")

    print("1. Organic")
    print("2. Semi-detached")
    print("3. Embedded")
    choice = int(input("Select project mode: "))

    if choice == 1:
        a, b, c, d, mode = 2.4, 1.05, 2.5, 0.38, "Organic"
    elif choice == 2:
        a, b, c, d, mode = 3.0, 1.12, 2.5, 0.35, "Semi-detached"
    elif choice == 3:
        a, b, c, d, mode = 3.6, 1.20, 2.5, 0.32, "Embedded"
    else:
        raise ValueError("Select mode 1, 2, or 3.")

    effort = a * (kloc ** b)       # Person-Months
    duration = c * (effort ** d)   # Months
    personnel = effort / duration

    print("\n--- ESTIMATION RESULTS ---")
    print("Project mode:", mode)
    print("Project size:", kloc, "KLOC")
    print("Effort:", round(effort, 2), "Person-Months")
    print("Development duration:", round(duration, 2), "Months")
    print("Average personnel:", round(personnel, 2))

except ValueError as error:
    print("Invalid input:", error)
