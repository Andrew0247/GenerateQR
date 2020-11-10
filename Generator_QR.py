import sys
import qrcode
import tkinter as tk
import os
from tkinter import messagebox, ttk, filedialog
from PIL import ImageTk, Image

formato = ".png"

# Metodo para guardar el codigo QR
def guardarQR():
    global archivoGuardar
    archivoGuardar = filedialog.asksaveasfilename(title = "Guardar en", defaultextension = formato)
    return archivoGuardar

# Metodo para generar el codigo QR
def generateQr():
    text = txt_text.get()
    if text != "":
        image = qrcode.make(text)
        archi = guardarQR()
        if archi != "":
            image.save(archi)
            messagebox.showinfo("QR CREADO","Código creado y guardado con éxito")
            imageQR = ImageTk.PhotoImage(Image.open(archi))
            lbl_image.configure(image = imageQR)
            lbl_image.image = imageQR
            txt_text.delete(0, tk.END)
    
    else:
        messagebox.showerror("ADVERTENCIA", "Error al generar QR, asegurese de haber ingresado un texto.")

root = tk.Tk()

# Label para mostrar el QR generado y guardado
lbl_image = tk.Label(root, text = "Aquí se mostrara el código QR generado y guardado en formato .png", wraplength = 350)
lbl_image.pack(side = tk.TOP, padx = 20, pady = 20)
lbl_image.config(bg = "white", font = ("Verdana", 14), bd = 50)

lbl_titulo = tk.Label(root, text = " INGRESE SU TEXTO A CONVERTIR ") # Label de un titulo
lbl_titulo.pack(padx = 5, pady = 5)

txt_text = tk.Entry(root, font = ('Arial', 15), width = 40, justify = "center") # Para ingresar el texto
txt_text.pack(side = tk.TOP, padx = 100, pady = 5)

btn_generateQR = tk.Button(root, text = ' Generar QR ', command = generateQr, font = ('Arial', 14)) # Boton para generar el codigo QR
btn_generateQR.pack(side = tk.TOP, padx=5, pady=5)

root.mainloop()