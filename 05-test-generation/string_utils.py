"""
String Utilities Module
=======================
Practice module for generating tests.

EXERCISE: Generate tests for these functions in test_string_utils.py
"""


def reverse_string(s: str) -> str:
    """Reverse a string."""
    return s[::-1]


def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome (case-insensitive, ignoring spaces)."""
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def count_vowels(s: str) -> int:
    """Count the number of vowels in a string."""
    return sum(1 for char in s.lower() if char in 'aeiou')


def count_words(s: str) -> int:
    """Count the number of words in a string."""
    return len(s.split())


def capitalize_words(s: str) -> str:
    """Capitalize the first letter of each word."""
    return ' '.join(word.capitalize() for word in s.split())


def remove_duplicates(s: str) -> str:
    """Remove duplicate characters while maintaining order."""
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)


def truncate(s: str, max_length: int, suffix: str = "...") -> str:
    """
    Truncate a string to max_length, adding suffix if truncated.
    
    Raises:
        ValueError: If max_length is less than the length of suffix.
    """
    if max_length < len(suffix):
        raise ValueError("max_length must be at least as long as suffix")
    
    if len(s) <= max_length:
        return s
    
    return s[:max_length - len(suffix)] + suffix


def slugify(s: str) -> str:
    """Convert a string to a URL-friendly slug."""
    import re
    # Convert to lowercase
    s = s.lower()
    # Replace spaces and special characters with hyphens
    s = re.sub(r'[^a-z0-9]+', '-', s)
    # Remove leading/trailing hyphens
    s = s.strip('-')
    return s


def extract_emails(text: str) -> list[str]:
    """Extract all email addresses from a text."""
    import re
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)


def mask_email(email: str) -> str:
    """
    Mask an email address for privacy.
    Example: "john.doe@example.com" -> "j***e@e*****e.com"
    """
    parts = email.split('@')
    if len(parts) != 2:
        return email
    
    local, domain = parts
    domain_parts = domain.split('.')
    
    def mask_part(s: str) -> str:
        if len(s) <= 2:
            return s
        return s[0] + '*' * (len(s) - 2) + s[-1]
    
    masked_local = mask_part(local)
    masked_domain = '.'.join(mask_part(p) for p in domain_parts)
    
    return f"{masked_local}@{masked_domain}"
