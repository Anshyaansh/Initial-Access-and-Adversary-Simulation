#!/usr/bin/env python3
"""Generate corporate email addresses from employee names using discovered format."""

employees = []
with open("../employees/raw_employees.txt", "r") as f:
    for line in f:
        name, title = line.strip().split(", ", 1)
        first, last = name.split(" ", 1)
        employees.append((first, last, title))

# Discovered format: {first_initial}{last}@domain
domain = "initech-solutions.lab"

print("=" * 60)
print("Generated Email Addresses for Initech Solutions")
print("Format: {first_initial}{last}@" + domain)
print("=" * 60)

for first, last, title in employees:
    email = f"{first[0].lower()}{last.lower().replace(' ', '')}@{domain}"
    print(f"{email:<40} | {title}")

print(f"\nTotal: {len(employees)} addresses generated")
