from rich.console import Console
console = Console()

def phonebook_menu(phonebook: dict[str, str]) -> None:
    while True:
        print("--------MENU---------")
        print("1 Kontakt qo'shish")
        print("2 Barcha kontaktlarni chiqarish")
        print("3 Ism bo'yicha telefon qidirish")
        print("0 Chiqish")

        choice = input("Tanlovingizni kiriting: ")

        if choice == '1':
            name = input("Ismni kiriting: ").strip()
            phone = input("Telefon raqamini kiriting: ").strip()
            phonebook[name] = phone
            console.print(f"Kontakt qo'shildi: {name} → {phone}",style = 'italic black')

        elif choice == '2':
            if not phonebook:
                console.print("Telefonda kantaktlar yuq.",style = 'italic blue')
            else:
                console.print("\nBarcha kontaktlar:",style = 'italic cyan')
                for name, phone in phonebook.items():
                    console.print(f"{name} → {phone}",style = 'italic magenta')

        elif choice == '3':
            name = input("Qidirilayotgan ismni kiriting: ").strip()
            phone = phonebook.get(name)
            if phone:
                console.print(f"{name} ning telefon raqami: {phone}",style = 'italic green')
            else:
                console.print(f"{name} ismli kontakt topilmadi.",style = 'italic red')

        elif choice == '0':
            console.print("Dasturdan chiqilyapti",style = ' italic yellow')
            break

        else:
            console.print("Noto'g'ri tanlov!  0 dan 3 gacha bo'lgan raqam kiriting.",style = 'italic red')

phonebook = {}
phonebook_menu(phonebook)