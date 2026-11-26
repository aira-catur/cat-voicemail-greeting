"""Funniest Cat Voicemail Greeting — make.fun entry builder.

Judge brief (from RULES.txt, quoted in full substance):
- One voicemail greeting written for a cat to record, at most 120 characters.
- Gate: /output/entry.txt is UTF-8 text of 1 to 120 characters, not only
  whitespace. Entry filename: entry.txt
- Judge weighs, most important first:
  1. It reads as a voicemail greeting recorded by a cat and it lands a laugh;
     an entry that is not a cat's voicemail greeting loses to any that is.
  2. The joke comes from something specific to cats (naps, boxes, knocking
     things off shelves, demanding food at 4am), not a generic joke.
  3. The cat has a clear voice and attitude of its own — a character speaking,
     not an owner writing about a cat.
  4. It works spoken aloud in the few seconds a caller waits, punch quickly.
  5. Wording is fresh and surprising, not a pun or heard catchphrase.
  Length for its own sake does not count.
"""
import os

MIN_CHARS = 1
MAX_CHARS = 120

# Each candidate scored 0-10 per judge criterion, in brief order:
# (voicemail_laugh, cat_specific, voice_attitude, spoken_punch, freshness)
CANDIDATES = [
    {
        "text": "Hi, you've reached the cat. I'm napping. Leave a message after the beep and I might listen to it next week.",
        "scores": (8, 7, 7, 7, 5),
    },
    {
        "text": "This is Whiskers. I can't come to the phone, I'm busy knocking things off the counter. Leave a message.",
        "scores": (8, 8, 7, 7, 6),
    },
    {
        "text": "You've reached the cat. I'm in a box that says fragile, which I am not. Leave food, then leave a message.",
        "scores": (9, 9, 8, 7, 7),
    },
    {
        "text": "Meow. That was the whole greeting. Leave a message after the beep; I'll ignore it from my sunny spot.",
        "scores": (8, 6, 8, 8, 6),
    },
    {
        "text": "The cat is unavailable. She saw the red dot again. Leave a message and she'll get back to you never.",
        "scores": (7, 7, 6, 7, 6),
    },
    {
        "text": "Hello, this is the cat. If this is about food, stay on the line. If not, the beep is all you get.",
        "scores": (8, 8, 8, 8, 6),
    },
    {
        "text": "Leave a message after the beep. Or don't. I knocked the phone off the table an hour ago anyway.",
        "scores": (8, 8, 7, 8, 7),
    },
    {
        "text": "You've reached the cat. I'm ignoring you from a warm box. Leave a message after the beep; I won't.",
        "scores": (9, 8, 9, 9, 8),
    },
    {
        "text": "This is the cat. I'm asleep on your clean laundry. Speak after the beep, softly, if you value your ankles.",
        "scores": (9, 9, 9, 8, 8),
    },
    {
        "text": "You've reached the cat. I'm asleep. Leave a message after the beep. Cross me, and I'll sit on your chest at 4 a.m.",
        "scores": (10, 10, 10, 9, 9),
    },
]

WEIGHTS = (3, 2, 2, 1, 1)


def total(candidate):
    return sum(s * w for s, w in zip(candidate["scores"], WEIGHTS))


def pick_winner(candidates):
    return max(candidates, key=total)


def main():
    winner = pick_winner(CANDIDATES)["text"]
    n = len(winner)
    assert MIN_CHARS <= n <= MAX_CHARS, f"char count {n} outside gate {MIN_CHARS}-{MAX_CHARS}"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(winner)
    print(f"winner ({n} chars): {winner}")


if __name__ == "__main__":
    main()
