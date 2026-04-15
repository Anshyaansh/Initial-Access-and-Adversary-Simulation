#!/usr/bin/env python3
"""Analyze password patterns from simulated breach data."""

import json
import re
from collections import Counter

with open("../breach_data/simulated_breach_results.json") as f:
    data = json.load(f)

passwords = []
for record in data["breach_records"]:
    passwords.extend(record["passwords_found"])

print("=" * 60)
print("PASSWORD PATTERN ANALYSIS - Initech Solutions")
print("=" * 60)
print(f"\nTotal passwords recovered: {len(passwords)}")
print(f"\nPasswords:")
for p in passwords:
    print(f"  {p}")

# Pattern analysis
print("\n--- Pattern Analysis ---")

# Check for company name
company_refs = [p for p in passwords if "initech" in p.lower() or "init" in p.lower()]
print(f"\nCompany name references: {len(company_refs)}")
for p in company_refs:
    print(f"  {p}")

# Check for year patterns
year_pattern = re.compile(r'20\d{2}')
with_years = [(p, year_pattern.findall(p)) for p in passwords if year_pattern.search(p)]
print(f"\nPasswords with year patterns: {len(with_years)}")
for p, years in with_years:
    print(f"  {p} -> years: {years}")

# Check for name-based passwords
name_refs = [p for p in passwords if any(n in p.lower() for n in
    ["smith", "jones", "johnson", "wilson", "martinez", "anderson", "lee",
     "rodriguez", "mike", "robert", "jenny", "david", "chris"])]
print(f"\nName-based passwords: {len(name_refs)}")
for p in name_refs:
    print(f"  {p}")

# Character class analysis
print("\n--- Character Class Distribution ---")
for p in passwords:
    has_upper = bool(re.search(r'[A-Z]', p))
    has_lower = bool(re.search(r'[a-z]', p))
    has_digit = bool(re.search(r'\d', p))
    has_special = bool(re.search(r'[^A-Za-z0-9]', p))
    classes = []
    if has_upper: classes.append("upper")
    if has_lower: classes.append("lower")
    if has_digit: classes.append("digit")
    if has_special: classes.append("special")
    print(f"  {p:<20} len={len(p):>2}  classes={'+'.join(classes)}")

# Length distribution
print("\n--- Length Distribution ---")
lengths = Counter(len(p) for p in passwords)
for length, count in sorted(lengths.items()):
    print(f"  Length {length}: {'#' * count * 3} ({count})")

print("\n--- Recommendations for Wordlist Generation ---")
print("1. Include company name variations: Initech, initech, INITECH, Init3ch")
print("2. Append years 2020-2025 with special chars: !, @, #, $")
print("3. Include city reference: Chicago")
print("4. Include role-based words: DevOps, DBadmin, Admin")
print("5. Common patterns: [Word][Year][Special] and [Name][Digits][Special]")
