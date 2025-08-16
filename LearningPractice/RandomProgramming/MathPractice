from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
import matplotlib.pyplot as plt
from PIL import Image as PILImage
import os

# ---------- Function to render LaTeX math to an image ----------
def latex_to_image(latex, filename):
    fig, ax = plt.subplots(figsize=(2, 0.5))  # starting small
    ax.text(0, 0, f"${latex}$", fontsize=14, ha='left', va='bottom')
    ax.axis('off')
    fig.tight_layout(pad=0)
    plt.savefig(filename, dpi=300, bbox_inches='tight', pad_inches=0.05, transparent=True)
    plt.close(fig)

# ---------- PDF Setup ----------
pdf_file = "Mathematics_I_Exercises.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=A4)
styles = getSampleStyleSheet()
story = []

# Maximum dimensions for images in points
TARGET_HEIGHT = 30
PAGE_WIDTH, PAGE_HEIGHT = A4
PAGE_MARGIN = 36  # half inch
MAX_WIDTH = PAGE_WIDTH - 2 * PAGE_MARGIN

# Space tracker for page breaks
current_height = 0

topics = [
    ("1. Conceptes bàsics", [
        r"\frac{3x^2y^3}{6xy^2}",
        r"2x - 5 = 9",
        r"0.000345",
        r"120^\circ \text{ to radians}"
    ]),
    ("2. Límits. Funcions contínues", [
        r"\lim_{x\to 2} \frac{x^2 - 4}{x - 2}",
        r"f(x) = \frac{x^2 - 1}{x - 1}",
        r"f(x) = |x| \text{ at } x = 0"
    ]),
    ("3. La derivada", [
        r"f'(x) \text{ for } f(x) = 3x^3 - 5x + 2",
        r"y = e^{2x} \cdot \sin(x)",
        r"\text{Derivative as velocity interpretation}"
    ]),
    ("4. Optimització", [
        r"\text{Two numbers sum to 20, product max}",
        r"\text{Rectangle with perimeter 100m, max area}",
        r"y = \sqrt{x} \text{ closest to } (4,0)"
    ]),
    ("5. La integral per a funcions d'una variable", [
        r"\int (3x^2 - 4x + 1) \, dx",
        r"\int e^{2x} \, dx"
    ]),
    ("6. La integral definida", [
        r"\int_{0}^{2} x^2 \, dx",
        r"\int_{1}^{3} v(t) \, dt \text{ as displacement}"
    ]),
    ("7. Equacions diferencials ordinàries de primer ordre", [
        r"\frac{dy}{dx} = 3y, \quad y(0) = 2",
        r"\frac{dy}{dx} + y = e^x"
    ]),
    ("8. Algunes equacions diferencials de la biologia i el medi ambient", [
        r"\frac{dP}{dt} = 0.2P\left(1 - \frac{P}{1000}\right)",
        r"\frac{dN}{dt} = -\lambda N"
    ])
]

# ---------- Add content to PDF ----------
for title, exercises in topics:
    story.append(Paragraph(f"<b>{title}</b>", styles['Heading2']))
    current_height += 24  # approx heading height

    for i, ex in enumerate(exercises, start=1):
        img_file = f"math_{title.replace(' ', '_')}_{i}.png"
        latex_to_image(ex, img_file)

        # Open image and scale proportionally
        with PILImage.open(img_file) as im:
            width, height = im.size
            aspect_ratio = width / height
            scaled_width = min(TARGET_HEIGHT * aspect_ratio, MAX_WIDTH)
        # No need to close image manually; 'with' handles it

        # Check if adding this image would overflow the page
        if current_height + TARGET_HEIGHT + 12 > PAGE_HEIGHT - PAGE_MARGIN:
            story.append(PageBreak())
            current_height = 0

        story.append(Paragraph(f"{i}.", styles['Normal']))
        story.append(Image(img_file, width=scaled_width, height=TARGET_HEIGHT))
        story.append(Spacer(1, 6))
        current_height += TARGET_HEIGHT + 6

    story.append(Spacer(1, 12))
    current_height += 12

story.append(PageBreak())
story.append(Paragraph("<b>Note:</b> Attempt without reference, then check solutions.", styles['Normal']))

# ---------- Build PDF ----------
doc.build(story)

# ---------- Cleanup images ----------
for file in os.listdir():
    if file.startswith("math_") and file.endswith(".png"):
        os.remove(file)

print(f"PDF created: {pdf_file}")
