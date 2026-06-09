# PII Masking Logic will go here.
import re

def scrub_pii(text):
    """
    Basic PII scrubber to mask emails and phone numbers 
    before contract analysis.
    """
    # Pattern for email addresses
    text = re.sub(r'\S+@\S+\.\S+', '[EMAIL_MASKED]', text)
    
    # Pattern for phone numbers (simple version)
    text = re.sub(r'\d{3}-\d{3}-\d{4}', '[PHONE_MASKED]', text)
    
    return text

if __name__ == "__main__":
    sample_text = "Contact me at venetta@caribbeanscribbles.com or 869-555-0199."
    print(f"Original: {sample_text}")
    print(f"Scrubbed: {scrub_pii(sample_text)}")
