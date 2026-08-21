# 3MTT NEXTGEN Cybersecurity Capstone
## Suspicious Login Log Analysis

**Author:** Samuel A. Ojeka  
**Programme:** 3MTT NEXTGEN – Cybersecurity  
**Project Type:** Cybersecurity Capstone / Defensive Security Lab

### Project Overview
This project demonstrates how authentication logs can be reviewed to identify suspicious login activity and possible credential-guessing behaviour in a controlled laboratory environment.

### Objectives
- Analyse authentication/login logs.
- Identify repeated failed login attempts.
- Review successful logins requiring investigation.
- Observe supporting network traffic.
- Produce security alerts and remediation recommendations.

### Laboratory Environment
- VirtualBox
- Kali Linux
- Ubuntu Server
- Wireshark
- Linux authentication logs
- Python

### Methodology
1. Build an isolated VirtualBox laboratory.
2. Generate controlled authentication events.
3. Collect and review authentication logs.
4. Monitor supporting traffic with Wireshark.
5. Identify suspicious patterns.
6. Document findings and recommend defensive controls.

### Key Finding
Repeated failed login attempts and successful logins requiring review were identified. Repeated activity from the same internal laboratory source was treated as a high-priority indicator of possible credential-guessing behaviour.

### Detection Script
Run:

```bash
python scripts/detect_suspicious_logins.py sample_data/auth.log --threshold 5
```

### Recommended Remediation
- Enable multi-factor authentication.
- Enforce strong passwords.
- Apply account lockout or rate limiting.
- Restrict SSH/RDP exposure.
- Centralise authentication logs.
- Monitor repeated authentication failures.
- Keep systems patched.
- Investigate unexpected successful logins.

## 🔎 Laboratory Evidence
The following visual evidence provides an overview of the controlled cybersecurity laboratory environment, including the VirtualBox setup, Kali Linux testing environment, Wireshark traffic monitoring, and suspicious login analysis.
![Cybersecurity Lab Environment](cybersecurity-lab-environment.png)

### Project Walkthrough
[Watch the 3MTT NEXTGEN Cybersecurity Capstone on YouTube](https://youtu.be/JbTqNCzr118)

### Repository Structure
```text
suspicious-login-log-analysis/
├── README.md
├── LICENSE
├── SECURITY.md
├── .gitignore
├── requirements.txt
├── scripts/
│   └── detect_suspicious_logins.py
├── sample_data/
│   └── auth.log
└── docs/
    └── PROJECT_SUMMARY.md
```

### Safety
This is an educational cybersecurity project intended for authorised, isolated laboratory testing only. No unauthorised real-world access is intended or demonstrated.
