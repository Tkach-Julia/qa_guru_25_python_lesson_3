from datetime import datetime

email1 = {
    "subject": "Quarterly Report",
    "from": "Alice.Cooper@Company. ",
    "to": " bob_smith@Gmail.com ",
    "body": "Hello Bob,\n\tHere is the quarterly report.\n\tPlease review and let me know your feedback.\n\nBest,\nAlice"
}

email2 = {
    "subject": " Weekd plans ",
    "from": "katya_yan@yandex. ",
    "to": "frid@mail. ",
    "body": "\tHey!\nLet's go hiking this weekd.\nBring snacks!\n"
}

email3 = {
    "subject": "Reminder: Meeting",
    "from": "ceo@corporation.com ",
    "to": " team_lead@outlook.com ",
    "body": " "
}

email4 = {
    "subject": " ",
    "from": " alex@business.net ",
    "to": " hr@company. ",
    "body": "Hi HR,\nPlease find attached my updated CV.\nThanks!"
}

email5 = {
    "subject": "Project collaboration",
    "from": " partner@organization.org ",
    "to": "lead_dev@icloud.com ",
    "body": "Hello,\nWe are interested in a partnership.\tPlease reply soon.\nRegards,\nTeam"
}


send_date = datetime.now().strftime("%Y-%m-%d")


email1["date"] = send_date
email2["date"] = send_date
email3["date"] = send_date
email4["date"] = send_date
email5["date"] = send_date


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


login_1, domain_1 = email1["from"].split('@')
login_2, domain_2 = email2["from"].split('@')
login_3, domain_3 = email3["from"].split('@')
login_4, domain_4 = email4["from"].split('@')
login_5, domain_5 = email5["from"].split('@')


# print(email1)
# print(email2)
# print(email3)
# print(email4)
# print(email5)
#
# print(f"Логин отправителя: {login_1}")
# print(f"Домен отправителя: {domain_1}")


