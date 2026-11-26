import os

PARTS = [
    "Diagnosis: you don't have imposter syndrome,",
    "you're just the only one here who read the instructions.",
    "Prescription: one nap, zero meetings, and no Googling symptoms at 3am.",
]

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as handle:
    handle.write(" ".join(PARTS) + "\n")
