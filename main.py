def dodawanie(a, b):
	return a + b

def odejmowanie(a, b):
	return a - b

def mnozenie(a, b):
	return a * b

def dzielenie(a, b):
	return a / b if b != 0 else "nie dziel przez zero"

print("kalkulator")
print("1. dodawanie")
print("2. odejmowanie")
print("3. mnozenie")
print("4. dzielenie")

try:
	wybor = int(input("wybierz:"))
	liczba1 = float(input("pierwsza liczba"))
	liczba2 = float(input("druga liczba"))
	if wybor == 1:
		print(dodawanie(liczba1, liczba2))
	elif wybor == 2:
		print(odejmowanie(liczba1,liczba2))
	elif wybor == 3:
		print(mnozenie(liczba1,liczba1))
	elif wybor == 4:
		print(dzielenie(liczba1,liczba2))
	else:
		print("nie ma takiej opcji), wybierz z zakresu 1 - 4")
		# comment z debianSO
expect ValueError:
	print("podaj pprawidlowa liczbe")
