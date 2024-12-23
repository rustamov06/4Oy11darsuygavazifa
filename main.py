#  4 OY 11 dars    MAVZU: Asinxronlik

# async,   await;
# import asyncio


# ---------------------------------------

# import asyncio
#
# async def genereate_numbr():
#     i = 0
#     while i < 10 :
#         print(i)
#         i += 1
#         await asyncio.sleep(1)
# async def genereate_numbr2():
#     print("Asinhron ishladi !!!")
#     i = 0
#     while i < 10:
#         print(i , "++")
#         i += 1
#         await asyncio.sleep(0.2)
# async def main():
#     await asyncio.gather(genereate_numbr(), genereate_numbr2())
# asyncio.run(main())

# ---------------------------------------

# Ob- havo malumotini async usulda olish

#==============================================Uyga vazifa============================================


# 1 vazifa

# import asyncio
# async def ab(password):
#     updated_password = ""
#     index = 0
#     while index < len(password):
#         char = password[index]
#         if not char.isdigit():
#             updated_password += char
#         index += 1
#         await asyncio.sleep(0.1)
#     return updated_password
# async def main():
#     password = input("Rassword : ")
#     print(f"Asl matn: {password}")
#     updated_password = await ab(password)
#     print(f"Yangilangan matn (raqamlarsiz): {updated_password}")
# asyncio.run(main())


# --------------------------------------------------------------------------------------------------------

# 2 vazifa

# import asyncio
#
# async def ab(text):
#     result = ""
#     i = 0
#     while i < len(text) and i < 10:
#         result += text[i]
#         i += 1
#         await asyncio.sleep(0.1)
#     print(f"Birinchi 10 ta belgi: {result}")
# async def main():
#     a = input("Matnni kiriting: ")
#     await ab(a)
# asyncio.run(main())


# --------------------------------------------------------------------------------------------------------

# 3 vazifa

# import asyncio
# async def ab(ism):
#     updated_ism = ""
#     index = 0
#     while index < len(ism):
#         char = ism[index]
#         if not char.isdigit():
#             updated_ism += char
#         index += 1
#         await asyncio.sleep(0.1)
#     return updated_ism
# async def main():
#     ism = input("Ism kiriting : ")
#     updated_ism = await ab(ism)
#     print(f"Yangilangan Ism (raqamlarsiz): {updated_ism}")
# asyncio.run(main())


# --------------------------------------------------------------------------------------------------------

# 4 vazifa

# import asyncio
# async def ab(text):
#     result = ""
#     i = 0
#     while i < len(text):
#         char = text[i]
#         if char != " ":
#             result += char.lower()
#         i += 1
#         await asyncio.sleep(0.1)
#     print(f"To'g'irlangan matn: {result}")
# async def main():
#     a = input("Matnni kiriting: ")
#     await ab(a)
# asyncio.run(main())


# --------------------------------------------------------------------------------------------------------

# 5 vazifa

# import asyncio
# async def ab(text):
#     result = ""
#     i = 0
#     while i < len(text):
#         char = text[i]
#         if char == "a" or char == "e" or char == "u" or char == "i" or char == "o" or char == "o'" or char == "A" or char == "E" or char == "U" or char == "I" or char == "O" or char == "O'":
#             result += char
#         i += 1
#         await asyncio.sleep(0.1)
#     print(f"To'g'irlangan matn: {result}")
# async def main():
#     a = input("Matnni kiriting: ")
#     await ab(a)
# asyncio.run(main())


# --------------------------------------------------------------------------------------------------------

# 6 vazifa


# import asyncio
# async def ab(text):
#     result = ""
#     i = 0
#     while i < len(text):
#         if text[i] == "a":
#             if i + 1 < len(text) and text[i + 1] == "b":
#                 result += "#"
#                 i += 1
#             else:
#                 result += text[i]
#         else:
#             result += text[i]
#         i += 1
#         await asyncio.sleep(0.1)
#     print(f"To'g'irlangan matn: {result}")
# async def main():
#     a = input("Matnni kiriting: ")
#     await ab(a)
# asyncio.run(main())


# --------------------------------------------------------------------------------------------------------

# 7 vazifa

# import asyncio
# async def ab(text):
#     result = ""
#     i = 0
#     while i < len(text):
#         if text[i].isdigit():
#             result += text[i]
#         i += 1
#         await asyncio.sleep(0.1)
#     print(f"To'g'irlangan matn: {result[::-1]}")
# async def main():
#     a = input("Raqamdan iborat matnni kiriting: ")
#     await ab(a)
# asyncio.run(main())



# --------------------------------------------------------------------------------------------------------

# 8 vazifa

# import asyncio
# async def ab(text):
#     result = ""
#     i = 0
#     index = round(len(text)/2) - 1
#     a = text[index]
#     while i < len(text):
#         if text[i] != a:
#             result += text[i]
#         i += 1
#         await asyncio.sleep(0.1)
#     print(f"To'g'irlangan ism: {result}")
# async def main():
#     a = input("ISmni kiriting: ")
#     await ab(a)
# asyncio.run(main())



# --------------------------------------------------------------------------------------------------------

# 9 vazifa

# import asyncio
# async def ab(text):
#     result = ""
#     i = 0
#     index = round(len(text)/2) - 1
#     a = text[index]
#     while i < len(text):
#         if text.endswith("a"):
#             result += text[i].lower()
#         else:
#             result += text[i]
#         i += 1
#         await asyncio.sleep(0.1)
#     print(f"To'g'irlangan matn: {result}")
# async def main():
#     a = input("Matnni kiriting: ")
#     await ab(a)
# asyncio.run(main())


# --------------------------------------------------------------------------------------------------------

# 10 vazifa

# import asyncio
# async def remove_duplicates(text):
#     result = ""
#     seen = set()
#     i = 0
#     while i < len(text):
#         char = text[i]
#         if char not in seen:
#             result += char
#             seen.add(char)
#         i += 1
#         await asyncio.sleep(0.1)
#     print(f"Takrorlanmagan harflar: {result}")
# async def main():
#     a = input("Matnni kiriting: ")
#     await remove_duplicates(a)
# asyncio.run(main())


# --------------------------------------------------------------------------------------------------------

# 11 vazifa

# import asyncio
# async def check_vowels(word):
#     vowels = "aeiouAEIOU"
#     for char in word:
#         if char not in vowels:
#             print("So'zda boshqa harflar bor.")
#             return
#         await asyncio.sleep(0.1)
#     print(f"So'z faqat unli harflardan iborat: {word.upper()}")
# async def main():
#     word = input("So'zni kiriting: ")
#     await check_vowels(word)
# asyncio.run(main())

# --------------------------------------------------------------------------------------------------------


# 12 vazifa

# import asyncio
# import time
# import requests
# from colorama import Fore, Style, init
# init(autoreset=True)
# API_KEY = "c0d70e2e98d28edb0941467b954dbdcc"
# async def get_weather(city):
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
#     try:
#         response = requests.get(url)
#         data = response.json()
#         if response.status_code == 200:
#             temp = data["main"]["temp"]
#             description = data["weather"][0]["description"]
#             print(f"{Fore.CYAN}Hozir {city} shahrida havo harorati: {temp}°C. Havo: {description}.")
#         else:
#             print(f"{Fore.RED}Shahar nomi noto'g'ri kiritildi!!!")
#     except Exception as e:
#         print(f"{Fore.RED}Xatolik yuz berdi: {e}")
# async def main():
#     print(f"{Fore.YELLOW}Dasturga xush kelibsiz! Ob-havo ma'lumotlarini olish uchun shahar nomini kiriting.")
#     print(f"{Fore.YELLOW}Dasturdan chiqish uchun 'stop' deb yozing.\n{'-' * 50}")
#     start_time = time.time()
#     while True:
#         city = input(f"{Fore.YELLOW}Shahar nomini kiriting: {Style.RESET_ALL}")
#         if city.lower() == "stop":
#             print(f"{Fore.RED}Dastur to'xtadi!!!")
#             end_time = time.time()
#             elapsed_time = end_time - start_time
#             print(f"{Fore.RED}{elapsed_time:.3f} sekund vaqt davomida ishladi!!!")
#             break
#         await get_weather(city)
#         print(f"{Fore.YELLOW}{'-' * 50}")
# asyncio.run(main())



# ================================================Rustamov Asilbek==========================================================