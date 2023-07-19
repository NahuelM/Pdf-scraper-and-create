import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PyPDF2 import PdfWriter, PdfReader

# Configuración inicial
fig, ax = plt.subplots()

x = np.linspace(0, 2 * np.pi, 100)
line, = ax.plot(x, np.sin(x))

# Función de inicialización de la animación
def init():
    line.set_ydata(np.sin(x))
    return line,

# Función de actualización de la animación
def update(frame):
    line.set_ydata(np.sin(x + frame * 0.1))
    return line,

# Crea la animación
ani = FuncAnimation(fig, update, frames=100, init_func=init, blit=True)

# Guarda la animación en un archivo GIF temporal
gif_file = 'animacion.gif'
ani.save(gif_file, writer='pillow', dpi=150)

# Crea un archivo PDF y agrega la imagen GIF
pdf_file = 'animacion.pdf'
c = canvas.Canvas(pdf_file, pagesize=letter)
c.drawImage(gif_file, 0, 0, width=letter[0], height=letter[1])
c.save()

# Combina la imagen GIF en el archivo PDF
output_pdf = PdfWriter()
pdf_page = PdfReader(pdf_file).pages[0]
output_pdf.add_page(pdf_page)
output_pdf.write(open(pdf_file, 'wb'))
