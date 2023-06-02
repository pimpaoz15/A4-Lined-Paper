from reportlab.lib.colors import Color
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

# define the page size
PAGE_WIDTH, PAGE_HEIGHT = A4

# create a new PDF file
pdf_file = canvas.Canvas("my_pdf_file.pdf", pagesize=A4)

# define the line spacing and line thickness
line_spacing = 3 * mm
line_thickness = 0.05 * mm

# set the stroke color of the lines to light gray with 50% opacity
line_color = Color(0.8, 0.8, 0.8, alpha=0.75)

# calculate the number of lines per page
lines_per_page = int((PAGE_HEIGHT / line_spacing))

# draw lines on the page
for page in range(2):
    for line in range(lines_per_page):
        y = line * line_spacing
        pdf_file.setStrokeColor(line_color)
        pdf_file.setStrokeAlpha(0.5)  # set the opacity of the lines
        pdf_file.setLineWidth(line_thickness)
        pdf_file.line(0, y, PAGE_WIDTH, y)
    
    # add a new page
    pdf_file.showPage()

# save and close the PDF file
pdf_file.save()
