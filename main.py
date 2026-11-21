"""Write one short text to /output/entry.txt.

The scene is quiet and vast: a climber alone on the last ridge before
sunrise, pack heavy and breath thin, pausing as first light touches one
peak, then another, then all at once, while the valley below is still
dark. The text aims for calm and awe rather than excitement — stillness,
scale, and a vastness that does not notice one small figure on a long
slope, and that being enough.
"""

import os

# The text is fixed and deterministic; it is written unchanged to the output.

TEXT = "She climbs the last ridge before sunrise, pack heavy, breath thin, and stops. Below, the valley is still dark; above, first light touches one peak, then another, then all at once. One small figure on a long slope, and the morning does not notice her, and that is enough."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
