users = [
    {"name": "Ali", "email": "ali0@gmail.com", "age": 25, "phone": "+998901234567", "country": "Uzbekistan"},
    {"name": "Vali", "email": "vali1@yahoo.com", "age": 32, "phone": "+998911112233", "country": "USA"},
    {"name": "Gani", "email": "gani2@hotmail.com", "age": 41, "phone": "+998933334455", "country": "UK"},
    {"name": "Sami", "email": "sami3@mail.ru", "age": 29, "phone": "+998944445566", "country": "Germany"},
    {"name": "Nodir", "email": "nodir4@outlook.com", "age": 36, "phone": "+998955556677", "country": "France"},
    {"name": "Dilshod", "email": "dilshod5@gmail.com", "age": 27, "phone": "+998966667788", "country": "Japan"},
    {"name": "Kamol", "email": "kamol6@yahoo.com", "age": 22, "phone": "+998977778899", "country": "India"},
    {"name": "Umid", "email": "umid7@hotmail.com", "age": 39, "phone": "+998988889900", "country": "Turkey"},
    {"name": "Aziz", "email": "aziz8@mail.ru", "age": 30, "phone": "+998901112223", "country": "Canada"},
    {"name": "Bekzod", "email": "bekzod9@outlook.com", "age": 44, "phone": "+998912223344", "country": "Australia"},
    {"name": "Madina", "email": "madina10@gmail.com", "age": 21, "phone": "+998923334455", "country": "Uzbekistan"},
    {"name": "Malika", "email": "malika11@yahoo.com", "age": 28, "phone": "+998934445566", "country": "USA"},
    {"name": "Gulbahor", "email": "gulbahor12@hotmail.com", "age": 33, "phone": "+998945556677", "country": "UK"},
    {"name": "Shahnoza", "email": "shahnoza13@mail.ru", "age": 26, "phone": "+998956667788", "country": "Germany"},
    {"name": "Nigora", "email": "nigora14@outlook.com", "age": 35, "phone": "+998967778899", "country": "France"},
    {"name": "Sevinch", "email": "sevinch15@gmail.com", "age": 23, "phone": "+998978889900", "country": "Japan"},
    {"name": "Lola", "email": "lola16@yahoo.com", "age": 40, "phone": "+998989990011", "country": "India"},
    {"name": "Zarina", "email": "zarina17@hotmail.com", "age": 31, "phone": "+998901223344", "country": "Turkey"},
    {"name": "Aziza", "email": "aziza18@mail.ru", "age": 38, "phone": "+998912334455", "country": "Canada"},
    {"name": "Diyor", "email": "diyor19@outlook.com", "age": 24, "phone": "+998923445566", "country": "Australia"},
]

result = set()

for list in users:
    result.add(list["email"][list["email"].index("@"):])
    print(result)