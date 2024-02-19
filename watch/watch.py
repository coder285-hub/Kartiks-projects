import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Regular expression pattern to match YouTube video URLs in src attribute of iframe elements
    pattern = r'<iframe.*?src="(https?://(?:www\.)?youtube\.com/embed/([^\s"/]+))".*?>'

    # Search for the pattern in the input HTML
    match = re.search(pattern, s)

    if match:
        # Extract the video ID from the match
        video_id = match.group(2)

        # Construct the youtu.be URL
        youtu_be_url = f"https://youtu.be/{video_id}"

        return youtu_be_url
    else:
        return None


if __name__ == "__main__":
    main()
