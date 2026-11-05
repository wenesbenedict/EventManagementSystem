while True:
    print("\n--- SOFTWARE METRICS ---")
    print("1. Defect Density")
    print("2. Defect Removal Efficiency (DRE)")
    print("3. Mean Time to Change (MTTC)")
    print("4. Software Maturity Index (SMI)")
    print("5. Schedule Performance Index (SPI)")
    print("6. Cost Performance Index (CPI)")
    print("7. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            defects = float(input("Total defects: "))
            kloc = float(input("KLOC: "))
            if defects < 0 or kloc <= 0:
                raise ValueError("Enter valid non-negative defects and KLOC > 0.")
            print("Defect Density =", round(defects / kloc, 2), "defects/KLOC")

        elif choice == 2:
            removed = float(input("Defects removed before release: "))
            remaining = float(input("Defects found after release: "))
            if removed < 0 or remaining < 0 or removed + remaining == 0:
                raise ValueError("Defect counts must be non-negative and total > 0.")
            dre = removed / (removed + remaining) * 100
            print("DRE =", round(dre, 2), "%")

        elif choice == 3:
            total_time = float(input("Total time spent on changes: "))
            changes = float(input("Number of changes: "))
            if total_time < 0 or changes <= 0:
                raise ValueError("Time must be >= 0 and changes > 0.")
            print("MTTC =", round(total_time / changes, 2), "time units/change")

        elif choice == 4:
            m = float(input("Total modules in current release (M): "))
            added = float(input("Modules added (Fa): "))
            changed = float(input("Modules changed (Fc): "))
            deleted = float(input("Modules deleted (Fd): "))
            if m <= 0 or min(added, changed, deleted) < 0:
                raise ValueError("M must be > 0; other counts must be >= 0.")
            smi = (m - added - changed - deleted) / m
            print("SMI =", round(smi, 3))

        elif choice == 5:
            ev = float(input("Earned Value (EV): "))
            pv = float(input("Planned Value (PV): "))
            if ev < 0 or pv <= 0:
                raise ValueError("EV must be >= 0 and PV > 0.")
            print("SPI =", round(ev / pv, 2))

        elif choice == 6:
            ev = float(input("Earned Value (EV): "))
            ac = float(input("Actual Cost (AC): "))
            if ev < 0 or ac <= 0:
                raise ValueError("EV must be >= 0 and AC > 0.")
            print("CPI =", round(ev / ac, 2))

        elif choice == 7:
            print("Program terminated.")
            break
        else:
            print("Invalid choice. Select 1 to 7.")

    except ValueError as error:
        print("Invalid input:", error)
