from datetime import datetime

# 1. Создайте словарь email
email1 = {
    "subject": "Quarterly Report",
    "from": "Alice.Cooper@Company. ",
    "to": " bob_smith@Gmail.com ",
    "body": "Hello Bob,\n\tHere is the quarterly report."
            "\n\tPlease review and let me know your feedback."
            "\n\nBest,\nAlice",
}

email2 = {
    "subject": " Weekd plans ",
    "from": "katya_yan@yandex. ",
    "to": "frid@mail. ",
    "body": "\tHey!\nLet's go hiking this weekd.\nBring snacks!\n",
}

email3 = {
    "subject": "Reminder: Meeting",
    "from": "ceo@corporation.com ",
    "to": " team_lead@outlook.com ",
    "body": " ",
}

email4 = {
    "subject": " ",
    "from": " alex@business.net ",
    "to": " hr@company. ",
    "body": "Hi HR,\nPlease find attached my updated CV.\nThanks!",
}

email5 = {
    "subject": "Project collaboration",
    "from": " partner@organization.org ",
    "to": "lead_dev@icloud.com ",
    "body": "Hello,\nWe are interested in a partnership."
            "\tPlease reply soon.\nRegards,\nTeam",
}

# 2. Добавьте дату отправки
send_date = datetime.now().strftime("%Y-%m-%d")

email1["date"] = send_date
email2["date"] = send_date
email3["date"] = send_date
email4["date"] = send_date
email5["date"] = send_date

# 3. Нормализуйте e-mail адреса
email1["from"] = email1["from"].strip().lower()
email2["from"] = email2["from"].strip().lower()
email3["from"] = email3["from"].strip().lower()
email4["from"] = email4["from"].strip().lower()
email5["from"] = email5["from"].strip().lower()

email1["to"] = email1["to"].strip().lower()
email2["to"] = email2["to"].strip().lower()
email3["to"] = email3["to"].strip().lower()
email4["to"] = email4["to"].strip().lower()
email5["to"] = email5["to"].strip().lower()

# 4. Извлеките логин и домен отправителя
login_1, domain_1 = email1["from"].split("@")
login_2, domain_2 = email2["from"].split("@")
login_3, domain_3 = email3["from"].split("@")
login_4, domain_4 = email4["from"].split("@")
login_5, domain_5 = email5["from"].split("@")

# 5. Создайте сокращённую версию текста
email1["short_body"] = email1["body"][0:10] + "..."
email2["short_body"] = email2["body"][0:10] + "..."
email3["short_body"] = email3["body"][0:10] + "..."
email4["short_body"] = email4["body"][0:10] + "..."
email5["short_body"] = email5["body"][0:10] + "..."

# 6. Списки доменов
personal_domains_list = [
    "gmail.com",
    "list.ru",
    "yahoo.com",
    "outlook.com",
    "hotmail.com",
    "icloud.com",
    "yandex.ru",
    "mail.ru",
    "list.ru",
    "bk.ru",
    "inbox.ru",
]
corporate_domains_list = [
    "company.ru",
    "corporation.com",
    "university.edu",
    "organization.org",
    "company.ru",
    "business.net",
]

unique_personal_domains = list(set(personal_domains_list))
unique_corporate_domains = list(set(corporate_domains_list))

# 7. Проверьте что в списке личных и корпоративных доменов нет пересечений
intersection = set(unique_personal_domains).intersection(set(unique_corporate_domains))

if len(intersection) > 0:
    print(f"Количество найденных пересечений: {len(intersection)}")
    print()
else:
    print("Пересечений не найдено")
    print()

# 8. Проверьте «корпоративность» отправителя
is_corporate_1 = domain_1 in unique_corporate_domains
is_corporate_2 = domain_2 in unique_corporate_domains
is_corporate_3 = domain_3 in unique_corporate_domains
is_corporate_4 = domain_4 in unique_corporate_domains
is_corporate_5 = domain_5 in unique_corporate_domains

message1 = "входит" if is_corporate_1 else "не входит"
print(f"Домен отправителя {domain_1} {message1} в список корпоративных доменов")

message2 = "входит" if is_corporate_2 else "не входит"
print(f"Домен отправителя {domain_2} {message2} в список корпоративных доменов")

message3 = "входит" if is_corporate_3 else "не входит"
print(f"Домен отправителя {domain_3} {message3} в список корпоративных доменов")

message4 = "входит" if is_corporate_4 else "не входит"
print(f"Домен отправителя {domain_4} {message4} в список корпоративных доменов")

message5 = "входит" if is_corporate_5 else "не входит"
print(f"Домен отправителя {domain_5} {message5} в список корпоративных доменов")
print()

# 9. Соберите «чистый» текст сообщения
email1["clean_body"] = email1["body"].replace("\n", " ").replace("\t", " ")
email2["clean_body"] = email2["body"].replace("\n", " ").replace("\t", " ")
email3["clean_body"] = email3["body"].replace("\n", " ").replace("\t", " ")
email4["clean_body"] = email4["body"].replace("\n", " ").replace("\t", " ")
email5["clean_body"] = email5["body"].replace("\n", " ").replace("\t", " ")

# 10. Сформируйте текст отправленного письма многострочной f-строкой
email1["sent_text"] = f"""
Кому: {email1["to"]}, от {email1["from"]}
Тема: {email1["subject"]}, дата {email1["date"]}
{email1["clean_body"]}
"""
email2["sent_text"] = f"""
Кому: {email2["to"]}, от {email2["from"]}
Тема: {email2["subject"]}, дата {email2["date"]}
{email2["clean_body"]}
"""
email3["sent_text"] = f"""
Кому: {email3["to"]}, от {email3["from"]}
Тема: {email3["subject"]}, дата {email3["date"]}
{email3["clean_body"]}
"""
email4["sent_text"] = f"""
Кому: {email4["to"]}, от {email4["from"]}
Тема: {email4["subject"]}, дата {email4["date"]}
{email4["clean_body"]}
"""
email5["sent_text"] = f"""
Кому: {email5["to"]}, от {email5["from"]}
Тема: {email5["subject"]}, дата {email5["date"]}
{email5["clean_body"]}
"""

# 11. Рассчитайте количество страниц печати для email["sent_text"]
symbols_per_page = 500
pages_email1 = (len(email1["sent_text"]) + 499) // symbols_per_page
pages_email2 = (len(email2["sent_text"]) + 499) // symbols_per_page
pages_email3 = (len(email3["sent_text"]) + 499) // symbols_per_page
pages_email4 = (len(email4["sent_text"]) + 499) // symbols_per_page
pages_email5 = (len(email5["sent_text"]) + 499) // symbols_per_page

# 12. Проверьте пустоту темы и тела письма
is_subject_empty_email1 = not email1["subject"].strip()
is_subject_empty_email2 = not email2["subject"].strip()
is_subject_empty_email3 = not email3["subject"].strip()
is_subject_empty_email4 = not email4["subject"].strip()
is_subject_empty_email5 = not email5["subject"].strip()

is_body_empty_email1 = not email1["body"].strip()
is_body_empty_email2 = not email2["body"].strip()
is_body_empty_email3 = not email3["body"].strip()
is_body_empty_email4 = not email4["body"].strip()
is_body_empty_email5 = not email5["body"].strip()

# 13. Создайте «маску» e-mail отправителя
email1["masked_from"] = login_1[0:2] + "***@" + domain_1
email2["masked_from"] = login_2[0:2] + "***@" + domain_2
email3["masked_from"] = login_3[0:2] + "***@" + domain_3
email4["masked_from"] = login_4[0:2] + "***@" + domain_4
email5["masked_from"] = login_5[0:2] + "***@" + domain_5

# 14. Удалите из списка личных доменов значения "list.ru" и "bk.ru"
unique_personal_domains.remove("list.ru")
unique_personal_domains.remove("bk.ru")

# ----------Вывод печати для проверки----------
print(f"Логин отправителя: {login_1}")
print(f"Домен отправителя: {domain_1}")
print(f"Логин отправителя: {login_2}")
print(f"Домен отправителя: {domain_2}")
print(f"Логин отправителя: {login_3}")
print()
print(f"Домен отправителя: {domain_3}")
print(f"Логин отправителя: {login_4}")
print(f"Домен отправителя: {domain_4}")
print(f"Логин отправителя: {login_5}")
print(f"Домен отправителя: {domain_5}")
print()

print(email1["short_body"])
print(email2["short_body"])
print(email3["short_body"])
print(email4["short_body"])
print(email5["short_body"])
print()

print(f"Личные домены (уникальные): {unique_personal_domains}")
print(f"Корпоративные домены (уникальные): {unique_corporate_domains}")
print()

print(email1["clean_body"].strip())
print(email2["clean_body"].strip())
print(email3["clean_body"].strip())
print(email4["clean_body"].strip())
print(email5["clean_body"].strip())
print()

print(email1["sent_text"])
print(email2["sent_text"])
print(email3["sent_text"])
print(email4["sent_text"])
print(email5["sent_text"])
print()

print(pages_email1)
print(pages_email2)
print(pages_email3)
print(pages_email4)
print(pages_email5)
print()

print(is_subject_empty_email1)
print(is_subject_empty_email2)
print(is_subject_empty_email3)
print(is_subject_empty_email4)
print(is_subject_empty_email5)
print()
print(is_body_empty_email1)
print(is_body_empty_email2)
print(is_body_empty_email3)
print(is_body_empty_email4)
print(is_body_empty_email5)
print()

print(email1["masked_from"])
print(email2["masked_from"])
print(email3["masked_from"])
print(email4["masked_from"])
print(email5["masked_from"])
print()

print(unique_personal_domains)
