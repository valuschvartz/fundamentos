#!/usr/bin/env python3
import re
texto = "Lorem ipsum dolor sit amet, consectetur ipsum elit. Amet sit amet."
patron = "ipsum(.*)sit"
print(re.search(patron, texto), "\n")
print(re.search(patron, texto).group())
print(re.search(patron, texto).group(0))
print(re.search(patron, texto).group(1))
print(re.sub(patron, "###", texto))