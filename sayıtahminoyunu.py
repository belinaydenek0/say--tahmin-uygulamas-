import random
import tkinter as tk

# Rastgele sayı seçimi
sayi = random.randint(1, 100)
tahmin_hakki = 10
tahmin_sayisi = 0

# Tahmin kontrol fonksiyonu
def tahmin_et():
    global tahmin_sayisi
    tahmin = tahmin_giris.get()

    if not tahmin.isdigit():
        sonuc_label.config(text="Lütfen geçerli bir sayı girin.")
        return

    tahmin = int(tahmin)
    tahmin_sayisi += 1

    if tahmin < sayi:
        mesaj = "Daha yüksek bir sayı deneyin."
    elif tahmin > sayi:
        mesaj = "Daha düşük bir sayı deneyin."
    else:
        mesaj = f"Tebrikler! {tahmin_sayisi}. denemede doğru tahmin ettiniz 🎉"
        tahmin_buton.config(state="disabled")

    if tahmin_sayisi >= tahmin_hakki and tahmin != sayi:
        mesaj = f"Hakkınız bitti. Doğru sayı: {sayi}"
        tahmin_buton.config(state="disabled")

    # Kalan hakkı güncelle
    tahmin_hakki_buton.config(text=f"Kalan Hakkınız: {tahmin_hakki - tahmin_sayisi}")
    sonuc_label.config(text=mesaj)

# Pencere oluşturma
pencere = tk.Tk()
pencere.title("Sayı Tahmin Oyunu")
pencere.geometry("400x300")

# Arayüz elemanları
etiket = tk.Label(pencere, text="Sayı Tahmin Oyununa Hoşgeldiniz!", font=("Arial", 16), fg="darkblue")
etiket.pack(pady=10)

etiket2 = tk.Label(pencere, text="1 ile 100 arasında bir sayı tuttum.", font=("Arial", 12), fg="red")
etiket2.pack(pady=5)

etiket_giris = tk.Label(pencere, text="Lütfen tahmininizi giriniz:", font=("Arial", 12), fg="black")
etiket_giris.pack(pady=5)

tahmin_giris = tk.Entry(pencere, font=("Arial", 12))
tahmin_giris.pack(pady=5)

tahmin_buton = tk.Button(pencere, text="Tahmin Et", font=("Arial", 12), command=tahmin_et)
tahmin_buton.pack(pady=5)

tahmin_hakki_buton = tk.Label(pencere, text=f"Kalan Hakkınız: {tahmin_hakki}", font=("Arial", 12), fg="purple")
tahmin_hakki_buton.pack(pady=5)

sonuc_label = tk.Label(pencere, text="", font=("Arial", 12), fg="green")
sonuc_label.pack(pady=10)

# Pencereyi başlat
pencere.mainloop()