"""Zufallszahlen-Generator: fragt nach Bereich und Anzahl und gibt Zufallszahlen aus."""
import random


def zahl_abfragen(frage, standard):
    """Fragt eine ganze Zahl ab; bei leerer Eingabe gilt der Standardwert."""
    while True:
        eingabe = input(f"{frage} [{standard}]: ").strip()
        if eingabe == "":
            return standard
        try:
            return int(eingabe)
        except ValueError:
            print("Bitte eine ganze Zahl eingeben.")


def main():
    print("=== Zufallszahlen-Generator ===")
    while True:
        minimum = zahl_abfragen("Kleinste Zahl", 1)
        maximum = zahl_abfragen("Größte Zahl", 100)
        if minimum > maximum:
            minimum, maximum = maximum, minimum  # vertauscht eingegeben? Einfach umdrehen
        anzahl = max(1, zahl_abfragen("Wie viele Zahlen?", 1))
        ohne_doppelte = input("Ohne doppelte Zahlen? (j/n) [n]: ").strip().lower() == "j"

        if ohne_doppelte:
            moeglich = maximum - minimum + 1
            if anzahl > moeglich:
                print(f"Im Bereich gibt es nur {moeglich} verschiedene Zahlen – ich nehme alle.")
                anzahl = moeglich
            zahlen = random.sample(range(minimum, maximum + 1), anzahl)
        else:
            zahlen = [random.randint(minimum, maximum) for _ in range(anzahl)]

        print("Ergebnis:", ", ".join(str(z) for z in zahlen))
        if anzahl > 1:
            print(f"Summe: {sum(zahlen)} · Kleinste: {min(zahlen)} · Größte: {max(zahlen)}")

        if input("\nNochmal? (j/n) [j]: ").strip().lower() == "n":
            print("Tschüss!")
            break
        print()


if __name__ == "__main__":
    main()
