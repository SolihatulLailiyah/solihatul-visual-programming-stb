import tkinter
from tkinter import ttk
from tkinter import * 
from tkinter.messagebox import showinfo

# inisialisasi
window = tkinter.Tk()
window.configure(bg="green")
window.geometry("700x350")
window.resizable(False,False)
window.title("Pendaftaran Mukbang")

# variable dan function
NAMA_LENGKAP = tkinter.StringVar()
ALAMAT_RUMAH = tkinter.StringVar()
MAKANAN_FAVORITE = tkinter.StringVar()
MINUMAN_FAVORITE = tkinter.StringVar()
OLAHRAGA_FAVORITE = tkinter.StringVar()

# fungsi tombol
def tombol_click():
    if not NAMA_LENGKAP.get() or not ALAMAT_RUMAH.get() or not MAKANAN_FAVORITE.get() or not MINUMAN_FAVORITE.get() or not OLAHRAGA_FAVORITE.get():
     showinfo(tittle="error!", message="mohon lengkapi semua form!")
    else:
     pesan = f"hello {NAMA_LENGKAP.get()}, KAMU SUDAH TERDAFTAR!!"
    showinfo(title="Wellcome", message=pesan)

# frame input
style = ttk.Style()
style.configure("Custom.TEntry",fieldbackground="blue")
input_frame = ttk.Frame(window)

# penempatan grid,pack,place
input_frame.pack(padx=10,pady=10,fill="x", expand = True)

# komponen nama lengkap
nama_depan_label = ttk.Label(input_frame,text="Nama Lengkap:")
nama_depan_label.pack(padx=10,fill="x", expand=True)
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_LENGKAP)
nama_depan_entry.pack(padx=10,fill="x", expand=True)
#komponen alamat rumah
alamat_rumah_label = ttk.Label(input_frame,text="Alamat:")
alamat_rumah_label.pack(padx=10,fill="x", expand=True)
alamat_rumah_entry = ttk.Entry(input_frame,textvariable=ALAMAT_RUMAH)
alamat_rumah_entry.pack(padx=10,fill="x", expand=True)
#komponen makanan favorite
makanan_favorite_label = ttk.Label(input_frame,text="Makanan Favorite:")
makanan_favorite_label.pack(padx=10,fill="x", expand=True)
makanan_favorite_entry = ttk.Entry(input_frame,textvariable=MAKANAN_FAVORITE)
makanan_favorite_entry.pack(padx=10,fill="x", expand=True)
#komponen minuman favorite
minuman_favorite_label = ttk.Label(input_frame,text="Minuman Favorite:")
minuman_favorite_label.pack(padx=10,fill="x", expand=True)
minuman_favorite_entry = ttk.Entry(input_frame,textvariable=MINUMAN_FAVORITE)
minuman_favorite_entry.pack(padx=10,fill="x", expand=True)
#komponen olahraga favorite
olahraga_favorite_label = ttk.Label(input_frame,text="Olahraga Favorite:")
olahraga_favorite_label.pack(padx=10,fill="x", expand=True)
olahraga_favorite_entry = ttk.Entry(input_frame,textvariable=OLAHRAGA_FAVORITE)
olahraga_favorite_entry.pack(padx=10,fill="x", expand=True)

#tombol
tombol_daftar = ttk.Button(input_frame, text="Daftar",command=tombol_click)
tombol_daftar.pack(fill="x", expand=True, padx=300,pady=10)

window.mainloop()