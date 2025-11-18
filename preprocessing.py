import pandas as pd

verses = []

with open("en.sahih.txt", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        line = line.strip() 
        if not line:
            continue  
        parts = line.split("|", 2)
        if len(parts) != 3:
            print(f"Skipping line {i}: {line}")
            continue
        surah, ayah, text = parts
        verses.append((int(surah), int(ayah), text))

df = pd.DataFrame(verses, columns=["surah", "ayah", "text"])
df.to_csv("quran_sahih.csv", index=False, encoding="utf-8")

print(f"Clean CSV saved: quran_sahih.csv")
print(f"Total verses: {len(df)}")
