# HRM-SYSTEM Security Policy

## 1. Supported Versions
| Version | Supported          | Security Updates Until |
| ------- | ------------------ | ---------------------- |
| 5.1.x   | :white_check_mark: | 2026-12-31             |
| 5.0.x   | :x:                | 2024-06-30             | 
| 4.0.x   | :white_check_mark: | 2025-12-31             |
| < 4.0   | :x:                | EOL                    |

## 2. System Overview
**Protected Assets**:
- Employee PII (National IDs, addresses, contact details)
- Salary/payroll records
- Medical/health information
- Performance evaluations
- Authentication credentials
- System access logs

## 3. Security Measures
### Access Control
- RBAC with 6 predefined roles (Employee, Manager, HR, Auditor, Admin, SuperAdmin)
- 2FA enforcement for privileged accounts
- Session timeout: 15 minutes inactivity

### Data Protection
- AES-256 encryption for sensitive fields
- TLS 1.3+ for data in transit
- Automatic redaction of PII in audit logs
- Daily encrypted backups (90-day retention)

### Application Security
- OWASP Top 10 protections implemented
- Quarterly penetration testing
- Static code analysis in CI/CD pipeline
- HSTS and CSP headers enforced

## 4. Vulnerability Reporting
**Responsible Disclosure Process**:
1. Email findings to `security@hrm-system.com` with:
   - Vulnerability description
   - Reproduction steps
   - Impact analysis
   - Suggested fixes

2. Expect initial response within **48 business hours**

3. Vulnerability handling timeline:
   ```plaintext
   T+0    : Report received
   T+2d   : Triage completed  
   T+7d   : Patch development
   T+14d  : Security advisory release
   T+21d  : Public disclosure
