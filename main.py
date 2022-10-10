from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

Folder_Name = ""

#dosya yeri
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")

    else:
        locationError.config(text="Lütfen dosya seçin!",fg="red")

#video indirme
def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if(len(url) >1):
        ytdError.config(text="")
        yt = YouTube(url)

        if(choice==choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif(choice==choices[1]):
            select = yt.streams.filter(progressive=True, file_extension='mp4').last()

        elif(choice==choices[2]):
            select = yt.streams.filter(only_audio=True, file_extension='mp3').first()

        else:
            ytdError.config(text="Lütfen tekrar deneyin!",fg="red")

    #İndirme Fonksiyonu
    select.download(Folder_Name)
    ytdError.config(text="İndirme tamamlandı!!")

root = Tk()
root.title("YouTube Downloader")
root.geometry("350x400")
root.columnconfigure(0,weight=1)

#Link yazma yeri
ytdLabel = Label(root,text="YouTube linkini girin.", font=("jost",17))
ytdLabel.grid()

#Link girme yeri
ytdEntryVar = StringVar()
ytdEntry = Entry(root, width=50, textvariable=ytdEntryVar)
ytdEntry.grid()

#Hata mesajı
ytdError = Label(root,text="Hata!",fg="red",font=("jost",10))
ytdError.grid()

#Kaydedecek yeri sorma
saveLabel = Label(root,text="Kaydedilecek yeri seçiniz.",font=("Jost",15,"bold"))
saveLabel.grid()

#yer seçme butonu
saveEntry = Button(root,width=10,bg="red",fg="white",text="Dosya seçin.",command=openLocation)
saveEntry.grid()

#Dosya hata Mesajı
locationError = Label(root,text="Konum hatası!",fg="red",font=("jost",10))
locationError.grid()

#İndirme kalitesi
ytdQuality = Label(root,text="Kalite seçiniz.",font=("jost",15))
ytdQuality.grid()

#Kombo kutusu
choices = ["1080p","720p","480p","144p","Yalnız Ses"]
ytdchoices = ttk.Combobox(root,values=choices)
ytdchoices.grid()

#İndirme butonu
downloadbtn = Button(root,text="İndir",width=10,bg="red",fg="white",command=DownloadVideo)
downloadbtn.grid()


root.mainloop()