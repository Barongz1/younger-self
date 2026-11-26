"""One Line to Your Younger Self — entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

# The line: advice to a younger self — the loudest dream is not the one to chase; the quiet one that keeps you up at night is the one worth following.
TEXT = "Don't chase the loudest dream — the quiet one that keeps you up at night is the one worth following."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
