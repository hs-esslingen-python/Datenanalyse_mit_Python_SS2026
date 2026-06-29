# Dies ist ein Python-Skript mit Kommandozeilenparametern.

import sys

if __name__ == '__main__':
    print('Python-Skript mit Kommandozeilenparametern')
    print(f"__name__ = {__name__} - Dies ist die main_Komandozeilenparameter.py Datei.")
    print(f"sys.argv = {sys.argv} - Dies sind die Kommandozeilenparameter.")

    Argumente = sys.argv[1:]  # Ignoriere den ersten Parameter (Dateiname)
    if Argumente:
        print("Die übergebenen Kommandozeilenparameter sind:")
        for i, arg in enumerate(Argumente):
            print(f"Parameter {i + 1}: {arg}")
    


