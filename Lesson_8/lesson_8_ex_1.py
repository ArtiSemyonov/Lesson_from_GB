import re

emails = ("lesson8@facebook.com\n"
          "geek41@google.com\n"
          "brains35@mail.ru")
pattern = r'(\w+)@([A-Z0-9]+\.[A-Z]{2,4})'
print(re.findall(pattern, emails, flags=re.IGNORECASE))
