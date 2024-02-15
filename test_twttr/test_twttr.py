from twttr import shorten

def main():
    lower_uppercase_test()

def lower_uppercase_test():
    # Test with lowercase input
    assert shorten("twitter") == "twttr"
    # Test with uppercase input
    assert shorten("TWITTER") == "TWTTR"

if __name__ == "__main__":
    main()
