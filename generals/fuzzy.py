import re

def standardize_name(name):
    # Define patterns for variations
    patterns = [
        (r'\bEmaar\s*Real\s*Estate\b', 'Emaar Properties', re.IGNORECASE),  # Match with extra words
        (r'\bEmaar\s*Property\b', 'Emaar Properties', re.IGNORECASE),  # Match with extra word
        (r'\bEmmar\b', 'Emaar Properties', re.IGNORECASE),  # Match common misspelling
        (r'\bEmaar\b', 'Emaar Properties', re.IGNORECASE),  # Exact match
    ]

    # Apply replacements in a specific order
    for pattern, replacement, flags in patterns:
        name = re.sub(pattern, replacement, name, flags=flags)

    return name

# Example usage
original_name = "Emaar"
standardized_name = standardize_name(original_name)
print(standardized_name)
