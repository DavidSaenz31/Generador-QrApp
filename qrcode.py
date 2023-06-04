import qrcode
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image


def generar_qr():
    # Obtener el texto o URL del campo de entrada
    contenido = entrada.get()

    # Generar el código QR
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
    qr.add_data(contenido)
    qr.make(fit=True)

    # Crear la imagen del código QR
    imagen_qr = qr.make_image(fill_color="black", back_color="white")

    # Convertir la imagen a un formato compatible con Tkinter
    imagen_tk = ImageTk.PhotoImage(imagen_qr)

    # Mostrar la imagen del código QR en la ventana
    etiqueta_imagen.configure(image=imagen_tk)
    etiqueta_imagen.image = imagen_tk


def guardar_qr():
    # Obtener el texto o URL del campo de entrada
    contenido = entrada.get()

    # Generar el código QR
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
    qr.add_data(contenido)
    qr.make(fit=True)

    # Crear la imagen del código QR
    imagen_qr = qr.make_image(fill_color="black", back_color="white")

    # Abrir el cuadro de diálogo de guardar archivo
    archivo_guardado = filedialog.asksaveasfile(defaultextension=".png", filetypes=(("PNG files", "*.png"), ("All files", "*.*")))

    # Guardar la imagen del código QR en un archivo
    if archivo_guardado is not None:
        imagen_qr.save(archivo_guardado.name)
        archivo_guardado.close()


# Crear la ventana de la aplicación
ventana = tk.Tk()
ventana.title("Generador de códigos QR")
ventana.geometry("450x550")

# Etiqueta y campo de entrada para el texto o URL
etiqueta = tk.Label(ventana, text="Coloque un texto o un URL", font=("Calibri", 12))
etiqueta.pack()
entrada = tk.Entry(ventana, font=("Calibri", 12))
entrada.pack()

# Botones para generar y guardar el código QR
boton_generar = tk.Button(ventana, text="Generar QR", command=generar_qr, bg="green", fg="white", font=("Calibri", 12))
boton_generar.pack(pady="1mm")
boton_guardar = tk.Button(ventana, text="Guardar QR", command=generar_qr, bg="Blue", fg="white", font=("Calibri", 12))
boton_guardar.pack()


# Etiqueta para mostrar la imagen del código QR
etiqueta_imagen = tk.Label(ventana)
etiqueta_imagen.pack(pady="1mm")

# Iniciar el bucle principal de la aplicación
ventana.mainloop()


#para verificar que funciona el generador, copia y pega este URL https://davidsaenz31.github.io/ o bien escribe algun texto.