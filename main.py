"""Write one short text to /output/entry.txt.

The scene is quiet and vast: a man alone on deck at dusk, hands on the
rail, watching the water turn slate while the sea goes on unhurried,
older than his grandfather and still here after him. The text aims for
calm and awe rather than excitement — stillness, scale, and a vastness
that settles him, the way breath settles into sleep.
"""

import os

# The text is fixed and deterministic; it is written unchanged to the output.

TEXT = "The ferry leaves at dusk, and a man stays on deck after the others go inside, hands on the rail, watching the water turn slate. The sea does not hurry. It was here before his grandfather, and will be here after, and knowing that settles him, the way breath settles into sleep."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
