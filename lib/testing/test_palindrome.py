import pytest
from palindrome import longest_palindromic_substring


class TestLongestPalindromicSubstring:
    """Test suite for longest_palindromic_substring function."""
    
    def test_basic_palindromes(self):
        """Test basic palindrome cases."""
        assert longest_palindromic_substring("babad") in ["bab", "aba"]
        assert longest_palindromic_substring("cbbd") == "bb"
        assert longest_palindromic_substring("racecar") == "racecar"
        assert longest_palindromic_substring("noon") == "noon"
        assert longest_palindromic_substring("level") == "level"
    
    def test_single_character(self):
        """Test single character strings."""
        assert longest_palindromic_substring("a") == "a"
        assert longest_palindromic_substring("z") == "z"
        assert longest_palindromic_substring("5") == "5"
    
    def test_two_character_strings(self):
        """Test two character strings."""
        assert longest_palindromic_substring("ac") in ["a", "c"]
        assert longest_palindromic_substring("ab") in ["a", "b"]
        assert longest_palindromic_substring("aa") == "aa"
        assert longest_palindromic_substring("xy") in ["x", "y"]
    
    def test_no_palindrome(self):
        """Test strings with no palindromic substrings longer than 1."""
        assert longest_palindromic_substring("abc") in ["a", "b", "c"]
        assert longest_palindromic_substring("xyz") in ["x", "y", "z"]
        assert longest_palindromic_substring("def") in ["d", "e", "f"]
    
    def test_empty_string(self):
        """Test empty string edge case."""
        assert longest_palindromic_substring("") == ""
    
    def test_longer_palindromes(self):
        """Test longer palindrome strings."""
        assert longest_palindromic_substring("abba") == "abba"
        assert longest_palindromic_substring("abcba") == "abcba"
        assert longest_palindromic_substring("abccba") == "abccba"
        assert longest_palindromic_substring("abcdcba") == "abcdcba"
    
    def test_mixed_case_palindromes(self):
        """Test palindromes with mixed case."""
        # Note: "Racecar" is not a palindrome due to case sensitivity (R != r)
        # The longest palindrome in "Racecar" is "aceca" (length 5)
        assert longest_palindromic_substring("Racecar") == "aceca"
        # "Mom" is not a palindrome due to case sensitivity (M != m)
        # The longest palindrome in "Mom" is "M" (length 1)
        assert longest_palindromic_substring("Mom") == "M"
        # "Dad" is not a palindrome due to case sensitivity (D != d)
        # The longest palindrome in "Dad" is "D" (length 1)
        assert longest_palindromic_substring("Dad") == "D"
    
    def test_numeric_strings(self):
        """Test strings containing numbers."""
        assert longest_palindromic_substring("12321") == "12321"
        assert longest_palindromic_substring("1234321") == "1234321"
        assert longest_palindromic_substring("12345") in ["1", "2", "3", "4", "5"]
        assert longest_palindromic_substring("1221") == "1221"
    
    def test_alphanumeric_strings(self):
        """Test strings with both letters and numbers."""
        assert longest_palindromic_substring("a1a") == "a1a"
        assert longest_palindromic_substring("1a1") == "1a1"
        assert longest_palindromic_substring("ab1ba") == "ab1ba"
        assert longest_palindromic_substring("1abcba1") == "1abcba1"
    
    def test_repeated_characters(self):
        """Test strings with repeated characters."""
        assert longest_palindromic_substring("aaa") == "aaa"
        assert longest_palindromic_substring("aaaa") == "aaaa"
        assert longest_palindromic_substring("aaaaa") == "aaaaa"
        # Note: "aaabaa" is not a palindrome (reads "aaabaa" forwards, "aabaaa" backwards)
        # The longest palindrome in "aaabaa" is "aabaa" (length 5)
        assert longest_palindromic_substring("aaabaa") == "aabaa"
    
    def test_complex_palindromes(self):
        """Test complex palindrome patterns."""
        assert longest_palindromic_substring("abaxyzzyxf") == "xyzzyx"
        assert longest_palindromic_substring("forgeeksskeegfor") == "geeksskeeg"
        assert longest_palindromic_substring("bananas") == "anana"
    
    def test_boundary_conditions(self):
        """Test boundary conditions and constraints."""
        # Test minimum length constraint (1 <= s.length <= 1000)
        assert longest_palindromic_substring("a") == "a"
        
        # Test strings near the upper boundary
        long_string = "a" * 999 + "b" + "a" * 999
        result = longest_palindromic_substring(long_string)
        assert len(result) >= 1
        assert result == result[::-1]  # Verify it's actually a palindrome
    
    def test_multiple_palindromes_same_length(self):
        """Test cases where multiple palindromes have the same length."""
        # "babad" has both "bab" and "aba" of length 3
        result = longest_palindromic_substring("babad")
        assert len(result) == 3
        assert result in ["bab", "aba"]
        
        # "cbbd" has "bb" as the longest
        result = longest_palindromic_substring("cbbd")
        assert result == "bb"
    
    def test_palindrome_at_beginning(self):
        """Test palindromes that start at the beginning of the string."""
        assert longest_palindromic_substring("aaabc") == "aaa"
        assert longest_palindromic_substring("abac") == "aba"
        assert longest_palindromic_substring("racecarxyz") == "racecar"
    
    def test_palindrome_at_end(self):
        """Test palindromes that end at the end of the string."""
        assert longest_palindromic_substring("xyzracecar") == "racecar"
        assert longest_palindromic_substring("abcba") == "abcba"
        assert longest_palindromic_substring("xyzaa") == "aa"
    
    def test_palindrome_in_middle(self):
        """Test palindromes that are in the middle of the string."""
        assert longest_palindromic_substring("xyzabccbaxyz") == "abccba"
        assert longest_palindromic_substring("abc12321def") == "12321"
        assert longest_palindromic_substring("preabacabapost") == "abacaba"
    
    def test_odd_length_palindromes(self):
        """Test odd-length palindromes."""
        assert longest_palindromic_substring("aba") == "aba"
        assert longest_palindromic_substring("abcba") == "abcba"
        assert longest_palindromic_substring("abcdeedcba") == "abcdeedcba"
    
    def test_even_length_palindromes(self):
        """Test even-length palindromes."""
        assert longest_palindromic_substring("aa") == "aa"
        assert longest_palindromic_substring("abba") == "abba"
        assert longest_palindromic_substring("abccba") == "abccba"
        assert longest_palindromic_substring("abcddcba") == "abcddcba"
    
    def test_special_characters_allowed(self):
        """Test that the function handles special characters as specified in constraints."""
        # According to constraints, s consists of only digits and English letters
        # So we shouldn't test with special characters, but we can test edge cases
        assert longest_palindromic_substring("a") == "a"
        assert longest_palindromic_substring("z") == "z"
        assert longest_palindromic_substring("0") == "0"
        assert longest_palindromic_substring("9") == "9"
    
    def test_performance_edge_case(self):
        """Test a case that might be computationally intensive."""
        # Create a string that might test the algorithm's efficiency
        # String with many potential palindrome centers
        test_string = "a" * 100 + "b" + "a" * 100
        result = longest_palindromic_substring(test_string)
        assert len(result) == 201  # Should find the full palindrome
        assert result == result[::-1]  # Verify it's actually a palindrome
