from banco import *
from tkinter import *
from tkinter import messagebox

def cadastrarConta() -> None:
    conta = txt_conta.get()
    cliente = txt_cliente.get()
    saldo = txt_saldo.get()

    dados = {
        "conta": conta,
        "cliente": cliente,
        "saldo": saldo
    }

    banco.append(dados)
    messagebox.showinfo("Adicionado", "Contato adicionado com sucesso!!")
    txt_conta.delete(0, END)
    txt_cliente.delete(0, END)
    txt_saldo.delete(0, END)


def cancelar() -> None:
    add_conta.destroy()

add_conta = Tk()
add_conta.title("Adicionar Conta")

label_conta = Label(add_conta, text="Conta: ", fg="navy", font="Tahoma 14 bold")
label_conta.grid(row=0, column=0)
txt_conta = Entry(add_conta, fg="navy", font="Tahoma 14 bold")
txt_conta.grid(row=0, column=1)

label_cliente = Label(add_conta, text="Nome: ", fg="navy", font="Tahoma 14 bold")
label_cliente.grid(row=1, column=0)
txt_cliente = Entry(add_conta, fg="navy", font="Tahoma 14 bold")
txt_cliente.grid(row=1, column=1)

label_saldo = Label(add_conta, text="Saldo: ", fg="navy", font="Tahoma 14 bold")
label_saldo.grid(row=2, column=0)
txt_saldo = Entry(add_conta, fg="navy", font="Tahoma 14 bold")
txt_saldo.grid(row=2, column=1)

btn_cadastrar = Button(add_conta, text="CADASTRAR", fg="navy", bg="white",
                       font="Tahoma 12 bold", width=20, height=1, command=cadastrarConta)
btn_cadastrar.grid(row=3, column=0)

btn_cancelar = Button(add_conta, text="CANCELAR", fg="navy", bg="white",
                      font="Tahoma 12 bold", width=20, height=1, command=cancelar)
btn_cancelar.grid(row=3, column=1)

add_conta.mainloop()
