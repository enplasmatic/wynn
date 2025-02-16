class String:
    @staticmethod
    def sized(default_value, size):
        """
        Create a new String by repeating default_value size times.
        """
        return str(default_value) * int(size)
    
    @staticmethod
    def sep(val:str, delimiter, times):
        """
        Splits the string by the given delimiter.
        Returns a list of strings.
        """
        return val.split(delimiter, times)
    
    @staticmethod
    def sepall(val: str, delimiter):
        """
        Splits the string by the given delimiter.
        Returns a list of strings.
        """
        return val.split(delimiter)
    
    @staticmethod
    def assign(val: str, value, index):
        """
        Replace the character (or insert a value) at the given index.
        If index is at or beyond the last character, the value is appended (or replaces the last character).
        """
        if index >= len(val) - 1:
            left = ""
        else:
            left = val[index+1:]
        return val[:index] + str(value) + left
    
    @staticmethod
    def substr(val: str, lo, hi):
        """
        Returns a substring from index lo to hi (inclusive).
        """
        return val[lo:hi+1]
    
    @staticmethod
    def leftsub(val: str, lo):
        """
        Returns a substring from index lo to the end.
        """
        return val[lo:]
    
    @staticmethod
    def rightsub(val: str, hi):
        """
        Returns a substring from the beginning up to index hi.
        """
        return val[:hi]
    
    @staticmethod
    def find(val: str, sub):
        """
        Returns the index of the first occurrence of sub or -1 if not found.
        """
        return val.find(sub)
    
    @staticmethod
    def rfind(val: str, sub):
        """
        Returns the index of the last occurrence of sub or -1 if not found.
        """
        return val.rfind(sub)
    
    @staticmethod
    def count(val: str, sub):
        """
        Counts the number of non-overlapping occurrences of sub.
        """
        return val.count(sub)
    
    @staticmethod
    def replace(val: str, old, new, count=-1):
        """
        Replaces occurrences of old with new.
        Optionally limit replacements to count.
        """
        return val.replace(old, new, count)
    
    @staticmethod
    def lowercase(val: str):
        """Returns a new string with all characters converted to lowercase."""
        return val.lower()
    
    @staticmethod
    def uppercase(val: str):
        """Returns a new string with all characters converted to uppercase."""
        return val.upper()
    
    @staticmethod
    def reverse(val: str):
        """Returns a new string with the characters in reverse order."""
        return val[::-1]
    
    @staticmethod
    def trim(val: str):
        """Returns a new string with leading and trailing whitespace removed."""
        return val.strip()
    
    @staticmethod
    def remove(val: str, character: str):
        """Returns a new string with some character removed."""
        return val.strip(character)

    @staticmethod
    def removeleft(val: str, character: str):
        """Returns a new string with some character removed."""
        return val.lstrip(character)
    
    @staticmethod
    def removeright(val: str, character: str):
        """Returns a new string with some character removed."""
        return val.rstrip(character)
    
    @staticmethod
    def trimleft(val: str):
        """Returns a new string with leading whitespace removed."""
        return val.lstrip()
    
    def substr(string, lo, hi):
        return string[lo:hi+1]

    def lstr(string, hi):
        return string[:hi+1]
    
    def rstr(string, lo):
        return string[lo:]
    
    @staticmethod
    def trimright(val: str):
        """Returns a new string with trailing whitespace removed."""
        return val.rstrip()
    
    @staticmethod
    def pad_left(val: str, width, fillchar=" "):
        """Pads the string on the left to fill the given width."""
        return val.rjust(width, fillchar)
    
    @staticmethod
    def pad_right(val: str, width, fillchar=" "):
        """Pads the string on the right to fill the given width."""
        return val.ljust(width, fillchar)
    
    @staticmethod
    def center(val: str, width, fillchar=" "):
        """Centers the string within the given width using fillchar."""
        return val.center(width, fillchar)
    
    @staticmethod
    def join(val: str, iterable):
        """
        Joins an iterable of strings using val as the separator.
        """
        items = [str(x) for x in iterable]
        return val.join(items)
    
    @staticmethod
    def format(val: str, *args, **kwargs):
        """
        Formats the string using Python's built-in format mechanism.
        """
        return val.format(*args, **kwargs)
    
    @staticmethod
    def make_int(val: str):
        """
        Attempts to convert the string to an integer.
        Raises ValueError if conversion is not possible.
        """
        try:
            return int(val)
        except ValueError:
            raise ValueError(f"Cannot convert '{val}' to int")
    
    @staticmethod
    def make_double(val: str):
        """
        Attempts to convert the string to a float.
        Raises ValueError if conversion is not possible.
        """
        try:
            return float(val)
        except ValueError:
            raise ValueError(f"Cannot convert '{val}' to float")
    
    @staticmethod
    def is_digit(val: str):
        """Returns True if the string consists only of digits."""
        return val.isdigit()
    
    @staticmethod
    def isalpha(val: str):
        """Returns True if the string consists only of alphabetic characters."""
        return val.isalpha()
    
    @staticmethod
    def isalnum(val: str):
        """Returns True if the string consists only of alphanumeric characters."""
        return val.isalnum()
    
    @staticmethod
    def isspace(val: str):
        """Returns True if the string consists only of whitespace."""
        return val.isspace()
    
    @staticmethod
    def contains(val: str, sub):
        """Returns True if sub is found in the string."""
        return sub in val
    
    @staticmethod
    def is_palindrome(val: str):
        """Returns True if the string is a palindrome (reads the same forwards and backwards)."""
        return val == val[::-1]
    
    def reverse(val: str):
        return val[::-1]