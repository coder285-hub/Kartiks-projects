from twttr import shorten
def main():
     lower_uppercase_test()
# Call test functions test_upper_lower_cases()
# Test letters upper and lower cases def test_upper_lower_cases(): ...assert shorten('twitter')
def lower_uppercase_test():
     assert shorten('TWITTER') == 'TWTTR'
     assert shorten('twitter') == 'twttr'
# Test numbers

if __name__ == "__main__":
     main()
