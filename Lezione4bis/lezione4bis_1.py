
# Dato una stringa s che contiene parole e spazi, restituire la lunghezza del'ultima parola in s.

def lenght_of_last_word(s: str) -> int:
    l: list[str] = s.split()
    return len(l[-1])
out = lenght_of_last_word('come    stai   ')
print(out)


