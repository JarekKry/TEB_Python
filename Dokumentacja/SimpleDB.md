# SimpleDB - Opis działania 

SimpleDB zapisuje dane w formie wpisów zawierających nieokreśloną ilość zmiennych, dane odzielone są separatorami domyślnie w formie znaków unicode.

**ᅤ** - Odziela poszczególne **entry**

**ᅥ** - Odziela poszczególne **parm**

**ᅧ** - Odziela **parmName** od **parmValue**

**entry** - Wpis zawierający zbór nieokreślonej liczby **parm**

**parm** - Składa się z **parmName** oraz **parmValue**

**parmName** - Nazwa identyfikująca zmienną

**parmValue** - Wartość zmiennej

## Przykład 
---

Dane w czystym formacie (**imieᅧJanᅥnazwiskoᅧKowalskiᅤimieᅧPiotrᅥnazwiskoᅧNowak**) po wczytaniu rozbijane są na **entry1** oraz **entry2**

**entry1** - Składa się z **parm1** i **parm2**

**parm1** - Składa się z **parm1Name** = **imie** oraz **parm1Value** = **Jan**

**parm2** - Składa się z **parm2Name** = **nazwisko** oraz **parm2Value** = **Kowalski**

---

**entry2** - Składa się z **parm1** i **parm2**

**parm1** - Składa się z **parm1Name** = **imie** oraz **parm1Value** = **Piotr**

**parm2** - Składa się z **parm2Name** = **nazwisko** oraz **parm2Value** = **Nowak**

## Ograniczenia
---

Głównym ograniczeniem **SimpleDB** jest brak możliwości użycia jako wartości opisanych na początku 3 znaków unicode (**ᅤ**,**ᅥ**,**ᅧ**)