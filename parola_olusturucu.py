import random
import string

def parola_olustur(uzunluk=8):
    # İstediğiniz uzunlukta rastgele bir parola oluşturur

    # Parola karakterleri
    karakterler = string.ascii_letters + string.digits + string.punctuation

    # Parolayı oluştur
    parola = ''.join(random.choice(karakterler) for _ in range(uzunluk))

    return parola

# Kullanıcıdan parola uzunluğunu al
uzunluk = int(input("Parola uzunluğunu girin: "))

# Parola oluştur
parola = parola_olustur(uzunluk)
print("Oluşturulan parola:", parola)
