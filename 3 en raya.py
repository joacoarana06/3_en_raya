import tkinter as tk
from tkinter import messagebox

# Función para reiniciar la partida
def reset_game():
    button_1.config(text="", state=tk.NORMAL)
    button_2.config(text="", state=tk.NORMAL)
    button_3.config(text="", state=tk.NORMAL)
    button_4.config(text="", state=tk.NORMAL)
    button_5.config(text="", state=tk.NORMAL)
    button_6.config(text="", state=tk.NORMAL)
    button_7.config(text="", state=tk.NORMAL)
    button_8.config(text="", state=tk.NORMAL)
    button_9.config(text="", state=tk.NORMAL)
    global turn
    turn = "X"

# Función para verificar si hay un ganador
def check_winner():
    winning_combinations = [
        [button_1, button_2, button_3], [button_4, button_5, button_6], [button_7, button_8, button_9],  # Filas
        [button_1, button_4, button_7], [button_2, button_5, button_8], [button_3, button_6, button_9],  # Columnas
        [button_1, button_5, button_9], [button_3, button_5, button_7]                                      # Diagonales
    ]
    
    for combo in winning_combinations:
        if combo[0]["text"] == combo[1]["text"] == combo[2]["text"] != "":
            messagebox.showinfo("¡Ganador!", f"¡El jugador {combo[0]['text']} ha ganado!")
            disable_buttons()
            return True
    return False

# Función para manejar el clic en cada casilla
def on_click(button):
    global turn
    if button["text"] == "":
        button.config(text=turn)
        if not check_winner():
            turn = "O" if turn == "X" else "X"

# Función para desactivar los botones después de que haya un ganador
def disable_buttons():
    button_1.config(state=tk.DISABLED)
    button_2.config(state=tk.DISABLED)
    button_3.config(state=tk.DISABLED)
    button_4.config(state=tk.DISABLED)
    button_5.config(state=tk.DISABLED)
    button_6.config(state=tk.DISABLED)
    button_7.config(state=tk.DISABLED)
    button_8.config(state=tk.DISABLED)
    button_9.config(state=tk.DISABLED)

# Crear ventana
root = tk.Tk()
root.title("3 en Raya")

# Variables de control
turn = "X"  # El jugador X empieza

# Crear los botones manualmente
button_1 = tk.Button(root, text="", width=10, height=3, font=("Arial", 24), command=lambda: on_click(button_1))
button_1.grid(row=0, column=0)

button_2 = tk.Button(root, text="", width=10, height=3, font=("Arial", 24), command=lambda: on_click(button_2))
button_2.grid(row=0, column=1)

button_3 = tk.Button(root, text="", width=10, height=3, font=("Arial", 24), command=lambda: on_click(button_3))
button_3.grid(row=0, column=2)

button_4 = tk.Button(root, text="", width=10, height=3, font=("Arial", 24), command=lambda: on_click(button_4))
button_4.grid(row=1, column=0)

button_5 = tk.Button(root, text="", width=10, height=3, font=("Arial", 24), command=lambda: on_click(button_5))
button_5.grid(row=1, column=1)

button_6 = tk.Button(root, text="", width=10, height=3, font=("Arial", 24), command=lambda: on_click(button_6))
button_6.grid(row=1, column=2)

button_7 = tk.Button(root, text="", width=10, height=3, font=("Arial", 24), command=lambda: on_click(button_7))
button_7.grid(row=2, column=0)

button_8 = tk.Button(root, text="", width=10, height=3, font=("Arial", 24), command=lambda: on_click(button_8))
button_8.grid(row=2, column=1)

button_9 = tk.Button(root, text="", width=10, height=3, font=("Arial", 24), command=lambda: on_click(button_9))
button_9.grid(row=2, column=2)

# Botón para reiniciar el juego
reset_button = tk.Button(root, text="Reiniciar", width=10, height=3, font=("Arial", 16), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3)

# Ejecutar la aplicación
root.mainloop()
