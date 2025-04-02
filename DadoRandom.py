import random

#● ┌ ┐ └ ┘ ─ │

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"


cara_dados= {
    1:("┌─────────┐"
       "│         │"
       "│    ●    │"
       "│         │"
       "└─────────┘"),
    2:("┌─────────┐"
       "│ ●       │"
       "│         │"
       "│       ● │"
       "└─────────┘"),
    3:("┌─────────┐"
       "│ ●       │"
       "│    ●    │"
       "│       ● │"
       "└─────────┘"),
    4:("┌─────────┐"
       "│ ●     ● │"
       "│         │"
       "│ ●     ● │"
       "└─────────┘"),
    5:("┌─────────┐"
       "│ ●     ● │"
       "│    ●    │"
       "│ ●     ● │"
       "└─────────┘"),
    6:("┌─────────┐"
       "│ ●  ●  ● │"
       "│         │"
       "│ ●  ●  ● │"
       "└─────────┘")
    
    
}

dado = []
total = 0

numero_de_dados = int(input("Cuantos dados? : "))

for x in range(numero_de_dados):
    dado.append(random.randint(1, 6))

for x in range(numero_de_dados):
    for linea in cara_dados.get(dado[x]):
        print(linea)

for x in dado:
    total += x

print(f"total: {total}")