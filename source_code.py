import customtkinter as ctk
import string
import random
import pyperclip

class PasswordGenerator:
    def __init__(self):
        # Настройка окна
        self.window = ctk.CTk()
        self.window.title("Генератор паролей")
        self.window.geometry("400x600")
        self.window.resizable(False, False)
        
        # Настройка темы
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Переменные
        self.password_length = ctk.IntVar(value=12)
        self.use_uppercase = ctk.BooleanVar(value=True)
        self.use_lowercase = ctk.BooleanVar(value=True)
        self.use_numbers = ctk.BooleanVar(value=True)
        self.use_symbols = ctk.BooleanVar(value=True)
        
        self.create_widgets()

    def create_widgets(self):
        # Заголовок
        title_label = ctk.CTkLabel(
            self.window,
            text="Генератор паролей",
            font=("Arial", 24, "bold")
        )
        title_label.pack(pady=20)

        # Поле для отображения пароля
        self.password_display = ctk.CTkEntry(
            self.window,
            width=300,
            height=50,
            font=("Arial", 16),
            justify="center"
        )
        self.password_display.pack(pady=20)

        # Настройки длины пароля
        length_frame = ctk.CTkFrame(self.window)
        length_frame.pack(pady=10, padx=15, fill="x")

        length_label = ctk.CTkLabel(
            length_frame,
            text="Длина пароля:",
            font=("Arial", 12)
        )
        length_label.pack(side="left", padx=10)

        length_slider = ctk.CTkSlider(
            length_frame,
            from_=4,
            to=32,
            variable=self.password_length,
            width=200
        )
        length_slider.pack(side="left", padx=10)

        length_value = ctk.CTkLabel(
            length_frame,
            textvariable=self.password_length,
            font=("Arial", 14)
        )
        length_value.pack(side="left", padx=10)

        # Настройки символов
        options_frame = ctk.CTkFrame(self.window)
        options_frame.pack(pady=20, padx=20, fill="x")

        uppercase_check = ctk.CTkCheckBox(
            options_frame,
            text="Прописные буквы (A-Z)",
            variable=self.use_uppercase
        )
        uppercase_check.pack(pady=5, padx=10, anchor="w")

        lowercase_check = ctk.CTkCheckBox(
            options_frame,
            text="Строчные буквы (a-z)",
            variable=self.use_lowercase
        )
        lowercase_check.pack(pady=5, padx=10, anchor="w")

        numbers_check = ctk.CTkCheckBox(
            options_frame,
            text="Цифры (0-9)",
            variable=self.use_numbers
        )
        numbers_check.pack(pady=5, padx=10, anchor="w")

        symbols_check = ctk.CTkCheckBox(
            options_frame,
            text="Специальные символы (!@#$%)",
            variable=self.use_symbols
        )
        symbols_check.pack(pady=5, padx=10, anchor="w")

        # Кнопки
        buttons_frame = ctk.CTkFrame(self.window)
        buttons_frame.pack(pady=20)

        generate_button = ctk.CTkButton(
            buttons_frame,
            text="Сгенерировать пароль",
            command=self.generate_password,
            width=200,
            height=40
        )
        generate_button.pack(pady=10)

        copy_button = ctk.CTkButton(
            buttons_frame,
            text="Копировать пароль",
            command=self.copy_password,
            width=200,
            height=40
        )
        copy_button.pack(pady=10)

    def generate_password(self):
        # Создаем строку с доступными символами
        chars = ''
        if self.use_uppercase.get():
            chars += string.ascii_uppercase
        if self.use_lowercase.get():
            chars += string.ascii_lowercase
        if self.use_numbers.get():
            chars += string.digits
        if self.use_symbols.get():
            chars += string.punctuation

        # Проверяем, выбран ли хотя бы один тип символов
        if not chars:
            self.password_display.delete(0, 'end')
            self.password_display.insert(0, "Выберите типы символов")
            return

        # Генерируем пароль
        password = ''.join(random.choice(chars) for _ in range(self.password_length.get()))
        self.password_display.delete(0, 'end')
        self.password_display.insert(0, password)

    def copy_password(self):
        password = self.password_display.get()
        if password and password != "Выберите типы символов":
            pyperclip.copy(password)

    def run(self):
        self.window.mainloop()

# Создаем и запускаем приложение
if __name__ == "__main__":
    app = PasswordGenerator()
    app.run()