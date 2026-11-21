"""Write one short text to /output/entry.txt.

The scene is quiet and vast: Mara alone on a roof at 3 a.m., small and
cold beneath the Perseids, while the night stays larger than her and asks
nothing back. The text aims for calm and awe rather than excitement —
stillness, scale, and a light that keeps falling whether or not anyone
points at it.
"""

import os

# The text is fixed and deterministic; it is written unchanged to the output.

TEXT = (
    "At 3 a.m., Mara stands on the roof in her father's coat, "
    "watching the Perseids fall over the sleeping town. "
    "Each one is gone before she can point. "
    "She stays, cold and small, under the falling light, "
    "while the night goes on being larger than her, quietly, "
    "asking nothing back."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
