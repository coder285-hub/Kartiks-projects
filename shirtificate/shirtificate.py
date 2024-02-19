from fpdf import FPDF

# Define constants for A4 size
A4_WIDTH = 210
A4_HEIGHT = 297

# Define function to create the shirtificate
def create_shirtificate(name):
    # Create instance of FPDF class
    pdf = FPDF(orientation='P', unit='mm', format='A4')

    # Add a page
    pdf.add_page()

    # Set font for title
    pdf.set_font("Arial", size=16)

    # Add title
    pdf.cell(0, 10, txt="CS50 Shirtificate", ln=True, align='C')

    # Set font for name
    pdf.set_font("Arial", size=12)

    # Add name
    pdf.set_text_color(255, 255, 255)  # white color for the name
    pdf.cell(0, 10, txt=name, ln=True, align='C')

    # Load and center the shirt image
    shirt_image = "shirtificate.png"
    image_width = 100  # Adjust the width as needed
    pdf.image(shirt_image, x=(A4_WIDTH - image_width) / 2, w=image_width)

    # Save the PDF
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    # Prompt user for their name
    name = input("Enter your name: ")

    # Generate the shirtificate
    create_shirtificate(name)
