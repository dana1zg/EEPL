import random
print("Δημιουργία πίνακα Ναρκαλιευτή")
print()

# Πόσο μεγάλος θα είναι ο πίνακας;
Rows = int(input("Δώσε αριθμό σειρών:"))
Columns = int(input("Δώσε αριθμό στηλών:"))
Bombs = int(input("Δώσε αριθμό βομβών:"))

# Δημιουργία πίνακα Rows*Columns
MineSweeperArray = [["0" for j in range(Columns)] for i in range (Rows)]

#Μηδενίζουμε ένα μετρητή που θα περιέχει τον αριθμό ναρκών που φυτεύθηκαν στο πίνακα
k = 0
while k < Bombs:
    i = random.randint(0, Rows - 1)
    j = random.randint(0, Columns - 1)
    #Να βεβαιωθούμε ότι δεν υπάρχει ήδη νάρκη εκεί
    if MineSweeperArray[i][j] != "*":
        #Δεν υπάρχει ήδη, φυτεύουμε μία
        MineSweeperArray[i][j] = "*"
        k = k + 1

# Εμφάνιση πίνακα
for i in range(len(MineSweeperArray)):
    for j in range(len(MineSweeperArray[i])):
        print(MineSweeperArray[i][j], end=' ')
    print()
