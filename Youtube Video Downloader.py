import customtkinter
from tkinter import messagebox
from pytube import YouTube

def video_select():
    url = entry_1.get()
    yt = YouTube(url)
    
    if len(url) == 0:
        messagebox.showinfo(
            title="Erro!",
            message="Favor insira uma URL válida"
        )
    else:
        opcao_escolhida = messagebox.askokcancel(
            title=url,
            message=f"O nome do vídeo é: \n "
                    f"{yt.title} \n "
                    f"Pronto para baixar?"
        )
        if opcao_escolhida:
            optionmenu_1_callback(yt)

def optionmenu_1_callback(yt):
    value = optionmenu_1.get()

    if value == "MP3":
        stream = yt.streams.filter(only_audio=True).get_by_itag("251")
        print(stream)

        stream.download(filename=f"{yt.title}.mp3", output_path="Downloads do YouTube")
    elif value == "MP4":
        stream = yt.streams.get_highest_resolution()
        print(stream)
        stream.download(filename=f"{yt.title}.mp4", output_path="Downloads do YouTube")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("400x240")
app.title("Editor's Heaven")

app.resizable(False,False)

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)    

entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="URL")
entry_1.pack(pady=50, padx=10)

button = customtkinter.CTkButton(master=app, text="Baixar", command=video_select, fg_color=("#DB3E39", "#821D1A"))
button.place(relx=0.5, rely=0.53, anchor=customtkinter.CENTER)

optionmenu_1 = customtkinter.CTkOptionMenu(frame_1, values=["MP3", "MP4"])
optionmenu_1.pack(pady=10, padx=10)
optionmenu_1.set("Formato")

app.mainloop()

