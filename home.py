from tkinter import *
import subprocess


def tela_add_conta():
    subprocess.Popen(["python", "add_conta.py"])
    home.destroy()


def tela_editar_conta():
    subprocess.Popen(["python", "editar_conta.py"])
    home.destroy()


def tela_consultar_conta():
    subprocess.Popen(["python", "consultar_conta.py"])
    home.destroy()


home = Tk()
home.title("MENU BANCO")

btn_Add_Conta = Button(home, text="Adicionar", fg="navy", bg="white",
                       font="Tahoma 12 bold", width=20, height=1, command=tela_add_conta)
btn_Add_Conta.grid(row=0, column=1)

btn_Editar_Conta = Button(home, text="Editar", fg="navy", bg="white",
                          font="Tahoma 12 bold", width=20, height=1, command=tela_editar_conta)
btn_Editar_Conta.grid(row=1, column=1)

btn_Consultar_Conta = Button(home, text="Consultar", fg="navy", bg="white",
                             font="Tahoma 12 bold", width=20, height=1, command=tela_consultar_conta)
btn_Consultar_Conta.grid(row=2, column=1)

home.mainloop()
