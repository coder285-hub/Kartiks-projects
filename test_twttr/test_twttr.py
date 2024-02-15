from twttr import shorten

def main():
     lower_uppercase_test()


def lower_uppercase_test():
     assert shorten("twitter")=="twttr"
     assert shorten("TWIITER")

if __name__ == "__main__":
    main()
