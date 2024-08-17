import email
from email import policy

def analyze_email_headers(email_file):
    with open(email_file, 'r') as f:
        msg = email.message_from_file(f, policy=policy.default)
        for header in ['From', 'To', 'Subject', 'Received']:
            print(f"{header}: {msg[header]}")

email_file = 'suspicious_email.eml'
analyze_email_headers(email_file)
