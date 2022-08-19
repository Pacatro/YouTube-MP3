from pytube import Playlist
from pytube import YouTube
from pathlib import Path
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os


class MainWindow:
    def __init__(self, root):
        root.geometry("700x470")
        root.title("YouTube MP3-MP4")
        root.config(bg = "#202326")
        root.resizable(0, 0)
        
        title = Label(root, text = "Youtube MP3-MP4", bg = "#202326", font = ("System", 30), fg = "White")
        title.pack(pady = 30)
        
        choose_title = Label(root, text = "What do you want to do?", bg = "#202326", font = ("System", 18), fg = "White")
        choose_title.pack(pady = 15)
        
        pl_button = Button(root, text = "Download Playlist", font = ("System", 18), fg = "White", bg = "#1F1F1F", bd = 5, cursor = "hand2", command = lambda: [root.destroy(), PlaylistWindow.init_playlistwindow(self)])
        pl_button.pack(pady = 30)
        
        yt_button = Button(root, text = "Download Video", font = ("System", 18), fg = "White", bg = "#1F1F1F", bd = 5, cursor = "hand2", command = lambda: [root.destroy(), YoutubeWindow.init_YoutubeWindow(self)])
        yt_button.pack(pady = 30)

        
class PlaylistWindow:
    def __init__(self, root2):
        
        root2.geometry("700x350")
        root2.title("Download Playlist")
        root2.config(bg = "#202326")
        root2.resizable(0, 0)
        
        title = Label(root2, text = "Youtube MP3-MP4", bg = "#202326", font = ("System", 30), fg = "White")
        title.pack(pady = 30)
        
        choose_title = Label(root2, text = "Playlist URL:", bg = "#202326", font = ("System", 18), fg = "White")
        choose_title.pack()
        
        url_entry = Entry(root2, font=("System", 10), bg = "White", fg = "#161616", width = 80)
        url_entry.pack(pady = 20)

        download_button = Button(root2, text = "Download", font = ("System", 18), fg = "White", bg = "#1F1F1F", bd = 5, cursor = "hand2", command = lambda: [download_playlist_mp3(url_entry.get()), root2.destroy(), main()])
        download_button.pack(pady = 30)
        
   
    def init_playlistwindow(self):
        app = tk.Tk()
        
        pl_window = PlaylistWindow(app)
        
        app.mainloop()


class YoutubeWindow:
    def __init__(self, root3):
        root3.geometry("700x350")
        root3.title("Download Playlist")
        root3.config(bg = "#202326")
        root3.resizable(0, 0)
        
        title = Label(root3, text = "Youtube MP3-MP4", bg = "#202326", font = ("System", 30), fg = "White")
        title.pack(pady = 30)
        
        choose_title = Label(root3, text = "Video URL:", bg = "#202326", font = ("System", 18), fg = "White")
        choose_title.pack()
        
        url_entry = Entry(root3, font=("System", 10), bg = "White", fg = "#161616", width = 80)
        url_entry.pack(pady = 20)

        download_button = Button(root3, text = "Download", font = ("System", 18), fg = "White", bg = "#1F1F1F", bd = 5, cursor = "hand2", command = lambda: [download_youtube_mp3(url_entry.get()), root3.destroy(), main()])
        download_button.pack(pady = 30) 
    
    def init_YoutubeWindow(self):
        app = tk.Tk()
        
        yt_window = YoutubeWindow(app)
        
        app.mainloop()
        
#Get directory to save files
def get_dir():
    directory = filedialog.askdirectory()
    
    if directory != "":
        os.chdir(directory)
        
    return directory

#Download a Youtube Playlist in .mp3
def download_playlist_mp3(url_pl):
    directory = get_dir()
    
    pl = Playlist(url_pl)
    
    videos = pl.videos
    
    for video in videos:
        print("\nDownloading:", video.title, "in mp3...")
        output_file = video.streams.filter(only_audio = True).first()
        download_file = output_file.download(output_path = directory)
        str(download_file)
        base, ext = os.path.splitext(download_file)
        new_file = base + ".mp3"
        os.rename(download_file, new_file)
    
    messagebox.showinfo(message = "Download finished!", title = "Info")

#Download Youtube videos in .mp3
def download_youtube_mp3(url_yt):
    directory = get_dir()
    
    yt = YouTube(url_yt)
    
    print("\nDownloading:", yt.title, "in mp3...")
    
    output_file = yt.streams.filter(only_audio = True).first()
    download_file = output_file.download(output_path = directory)
    str(download_file)
    base, extensión = os.path.splitext(download_file)
    nuevo_archivo = base + ".mp3"
    os.rename(download_file, nuevo_archivo)

    messagebox.showinfo(message = "Download finished!", title = "Info")

#Run main window
def main():
    app = tk.Tk()
    
    window = MainWindow(app)
    
    app.mainloop()


if __name__ == '__main__':
    main()    