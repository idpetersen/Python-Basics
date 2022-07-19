#!/usr/bin/env python3


def wpakey():
    with open('karmacoffeewpa.txt', 'a') as file:
        first = ["1","2","3","4","5","6","7","8","9","0"]
        second = ["1","2","3","4","5","6","7","8","9","0"]
        third = ["1","2","3","4","5","6","7","8","9","0"]
        forth = ["1","2","3","4","5","6","7","8","9","0"]
        for fi in first:
            for s in second:
                for t in third:
                    for f in forth:
                        end_combo = fi + s + t + f
                        wpa_key_case = "KarmaCoffee" + end_combo
                        wpa_key_nocase = "karmacoffee" + end_combo
                        file.write(wpa_key_case)
                        file.write('\n')
                        file.write(wpa_key_nocase)
                        file.write('\n')


def main():
    wpakey()


if __name__ == "__main__":
    main()