# Initech Solutions - Technology Stack Assessment

## Source: Job Postings (careers.initech-solutions.lab)

### Infrastructure
- Operating Systems: Windows Server 2019, Ubuntu 22.04 LTS
- Virtualization: VMware vSphere 7.x
- Cloud: AWS (primary), Azure AD for identity
- Containers: Docker, Kubernetes (EKS)

### Security
- EDR: CrowdStrike Falcon
- SIEM: Splunk Enterprise
- Email Security: Proofpoint
- MFA: Duo Security
- VPN: Cisco AnyConnect

### Applications
- Email: Microsoft 365
- Identity: Azure Active Directory with SSO
- Collaboration: Microsoft Teams, SharePoint Online
- Source Control: GitHub Enterprise
- CI/CD: Jenkins, GitHub Actions
- Database: PostgreSQL 14, Redis

### Derived Intelligence
- Azure AD + Duo = potential MFA fatigue attack vector
- Cisco AnyConnect = potential for VPN credential spraying
- GitHub Enterprise = possible repo access with valid credentials
- Jenkins = potential for RCE if externally exposed
- M365 = primary phishing target platform
