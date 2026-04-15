# Breach Intelligence Report: Initech Solutions

## Summary
- **Domain Assessed**: initech-solutions.lab
- **Employees Checked**: 15
- **Employees in Breaches**: 8 (53.3%)
- **Unique Passwords Recovered**: 11
- **Most Recent Breach**: Canva (May 2019)

## Risk Assessment

### High-Risk Accounts
| Email | Breaches | Passwords Found | Risk |
|---|---|---|---|
| rwilson@initech-solutions.lab | 3 breaches | 2 passwords | CRITICAL (SysAdmin) |
| clee@initech-solutions.lab | 2 breaches | 2 passwords | CRITICAL (DevOps) |
| jsmith@initech-solutions.lab | 3 breaches | 2 passwords | HIGH (CEO) |
| danderson@initech-solutions.lab | 2 breaches | 2 passwords | MEDIUM (Developer) |

### Password Pattern Intelligence
- **Company name in passwords**: Observed (e.g., "Initech2019!")
- **Year-based patterns**: Strongly observed across multiple accounts
- **Complexity**: Most passwords meet basic complexity (upper+lower+digit+special)
- **Length**: Average 9-10 characters
- **Predictability**: HIGH --- patterns suggest seasonal rotation policy

### Recommended Attack Strategy
1. **Credential Stuffing**: Directly test recovered passwords against VPN, M365, SSO
2. **Password Spraying**: Use pattern-derived wordlist against all known accounts
3. **Targeted Phishing**: Focus on accounts with no breach history (likely less security-aware)
