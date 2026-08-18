cnh = True
bebidinha = False

posso_dirigir = cnh and not bebidinha

print(f"Posso dirigir? {posso_dirigir}")

onibus = True
trem = False

venho_pra_aula = onibus or trem
print(f"Venho pra aula? {venho_pra_aula}")

locomocao = input("Diga sua locomoção:")
choveu = True

if choveu and locomocao == "moto":
    resultado = "Tô todo molhado :("
elif not choveu and locomocao == "moto":
    resultado = "Tô seco :)"
else:
    resultado = "Tô seco :)"

print(resultado)