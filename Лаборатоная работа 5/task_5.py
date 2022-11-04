import string
from random import sample

def get_random_password() -> str:
      alfab = string.digits + string.ascii_lowercase + string.ascii_uppercase
      print(alfab)
      pas_v1 = []
      while len(pas_v1) < 9:
            x = str(sample(alfab, 1)).strip("[]").strip("' '")

            if x not in pas_v1:
                  pas_v1.append(x)

      pas_v2 = str(pas_v1).strip("[]")

      norm_pas = ' '.join(i for i in pas_v2 if i.isalpha() or i.isdigit())

      return norm_pas


print(get_random_password())
