from tkinter import *
from tkinter import messagebox


def video_select():
    from pytube import YouTube
    url = website_entry.get()
    yt = YouTube(url)
    if len(url) == 0:
        messagebox.showinfo(
         title="Erro!",
            message="Favor insira uma URL válida")
    else:
        opcao_escolhida = messagebox.askokcancel(
            title=url,
            message=f"O nome do vídeo é: \n "
              f"{yt.title} \n "
              f"Pronto para baixar?")




    if opcao_escolhida:
        
        for stream in yt.streams.filter(only_audio=True):
            print(stream)

        yt = yt.streams.get_audio_only()
        yt.download(output_path= "Downloads do YouTube")
     




window = Tk()
window.title("Shiwid Downloader")
window.config(padx=10, pady=100)

website_label = Label(text="URL:")
website_label.grid(row=2, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=2, column=1, columnspan=2)
website_entry.focus()
add_button = Button(text="Baixar Video MP3", width=36, command=video_select)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
