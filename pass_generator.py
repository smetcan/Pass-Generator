import random
import string

def generate_password():
    while True:
        try:
            length = int(input("Şifre uzunluğunu girin (minimum 8, maksimum 16 hane): "))
            if length < 8 or length > 16:
                raise ValueError("Geçersiz şifre uzunluğu. Lütfen 8 ile 16 arasında bir değer girin.")
            break
        except ValueError:
            print("Geçersiz giriş. Lütfen bir tam sayı girin.")

    while True:
        use_special_characters = input("Özel karakter kullanılsın mı? (E/H): ").strip().lower()
        if use_special_characters == 'e' or use_special_characters == 'h':
            break
        else:
            print("Geçersiz giriş. Lütfen 'E' veya 'H' girin.")

    use_special_characters = use_special_characters == 'e'


    # Şifre oluşturma
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation if use_special_characters else ''

    # Her kategoriden en az bir karakter seç
    password_chars = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits)
    ]

    # Kullanıcının isteğine bağlı olarak özel karakter ekleyin
    if use_special_characters:
        password_chars.append(random.choice(special_characters))

    # Geri kalan karakterleri rastgele seçin
    remaining_length = length - len(password_chars)
    password_chars.extend(random.choices(lowercase_letters + uppercase_letters + digits + special_characters, k=remaining_length))

    # Karakterleri karıştırın
    random.shuffle(password_chars)

    # Şifreyi oluşturun
    password = ''.join(password_chars)
    return password

if __name__ == "__main__":
    password = generate_password()
    print("Oluşturulan Şifre:", password)
