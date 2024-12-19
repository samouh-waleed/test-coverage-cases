class StringUtils:
    @staticmethod
    def reverse(text: str) -> str:
        """Reverse a string."""
        return text[::-1]
    
    @staticmethod
    def capitalize_words(text: str) -> str:
        """Capitalize each word in a string."""
        return ' '.join(word.capitalize() for word in text.split())
    
    @staticmethod
    def remove_spaces(text: str) -> str:
        """Remove all spaces from a string."""
        return ''.join(text.split())