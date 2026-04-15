#!/usr/bin/env python3
"""Generate targeted wordlist based on breach pattern analysis."""

base_words = [
    "Initech", "initech", "INITECH", "Init3ch",
    "Solutions", "InitSol",
    "Chicago", "chicago",
    "DevOps", "Admin", "DBadmin", "SysAdmin",
    "Welcome", "Password", "Summer", "Winter", "Spring", "Fall",
]

years = ["2023", "2024", "2025", "23", "24", "25"]
specials = ["!", "@", "#", "$", "!!", "#$"]

wordlist = set()

for word in base_words:
    wordlist.add(word)
    for year in years:
        wordlist.add(f"{word}{year}")
        for s in specials:
            wordlist.add(f"{word}{year}{s}")

# Add observed patterns from breach data
wordlist.update([
    "P@ssw0rd1!", "Qwerty123!", "Changeme1!",
    "Welcome1!", "Letmein123!", "Monkey123!",
])

output_path = "/opt/Labs/initialAccess/labs/module-01/lab-02-breaches/wordlists/targeted_passwords.txt"
with open(output_path, "w") as f:
    for pw in sorted(wordlist):
        f.write(pw + "\n")

print(f"[+] Generated {len(wordlist)} targeted passwords")
print(f"[+] Saved to {output_path}")
