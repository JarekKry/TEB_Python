# SimpleEncryption - Opis algorytmu

**Haslo głowne** - Ciąg znaków wprowadzany przez użytkownika

**Key** - Hash generowany algorytmem [pbkdf2](https://en.wikipedia.org/wiki/PBKDF2) na  podstawie ciągu **Haslo głowne**

**rKey** - Hash generowany algorytmem [pbkdf2](https://en.wikipedia.org/wiki/PBKDF2) na podstawie odwróconego ciągu **Key**

**KeySum** - Suma klucza generowana na podstawie **Key** oraz **rKey**. Każda litera obu kluczy sprowadzana jest do wartości liczbowej oraz dodawana do **KeySum** według wzoru:

**KeySum** += ( **KeySum[x]** * **KeySum[x]** ) - ( **KeySum[x]** - **KeySum[x]** )

## Zaszyfrowywanie
---

**Text** - Ciąg tekstowy do zaszyfrowania

**TextLen** - Długość ciągu **Text**

**Output** - Wyjściowy ciąg w formacie liczb szesnastkowych oddzielonych myślnikami. Każdy element **Text** jest dodawany do ciągu wyjściowego według wzoru:

**Output** += ( **Text[x]** + **TextLen** + **Key[x]** ) + **KeySum** - ( **Key[x]** * **rKey[x]** )

## Odszyfrowywanie
---

**EncryptedText** - Wejściowy ciąg w formie liczb szesnastkowych oddzielonych myślnikami

**SplitedText** - Tablica tworzona po rozdzieleniu **EncryptedText** na pojedyncze l iczby szesnastkowe

**SplitedTextLen** - Liczba elementów tablicy **SplitedText** 

**Output** - Wyjściowy ciąg znaków. Każdy element **SplitedText** jest dodawany do wyjściowego ciągu znaków według wzoru:


**Output** += ( **SplitedText[x]** + ( **Key[x]** * **rKey[x]** ) ) - **KeySum** - **SplitedTextLen** - **Key[x]**

# SimpleEncryption - UML klas

![UML](/Dokumentacja/UML/SimpleEncryptor.svg)