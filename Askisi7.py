import random

def PrintBoard(b):
    # Εμφάνιση πίνακα
    for i in range(len(b)):
        for j in range(len(b[i])):
            print(b[i][j], end=' ')
        print()
    print()

def GameWon(b):
    for i in range(3):
        #Ελεγχος νικητή στις γραμμές
        if (b[i][0] == 'X') and (b[i][1] == 'X') and (b[i][2] == 'X'):
            return True
        elif (b[i][0] == 'O') and (b[i][1] == 'O') and (b[i][2] == 'O'):
            return True
        #Ελεγχος νικητή στις στήλες
        elif (b[0][i] == 'X') and (b[1][i] == 'X') and (b[2][i] == 'X'):
            return True
        elif (b[0][i] == 'O') and (b[1][i] == 'O') and (b[2][i] == 'O'):
            return True
    # Ελεγχος νικητή στις διαγωνίους
    if (b[0][0] == 'X') and (b[1][1] == 'X') and (b[2][2] == 'X'):
       return True
    elif (b[0][0] == 'O') and (b[1][1] == 'O') and (b[2][2] == 'O'):
       return True
    elif (b[0][2] == 'X') and (b[1][1] == 'X') and (b[2][0] == 'X'):
       return True
    elif (b[0][2] == 'O') and (b[1][1] == 'O') and (b[2][0] == 'O'):
       return True

    return False

#Έναρξη κυρίως προγράμματος
print("Τρίλιζα!")
print("Ο άνθρωπος έχει το σύμβολο Χ και ο υπολογιστής το σύμβολο Ο")

# Δημιουργία πίνακα 3*3
Board = [[" " for j in range(3)] for i in range (3)]
moves = 0

while (not GameWon(Board)) and (moves < 9):
    PrintBoard(Board)

    #Παίζει ο Άνθρωπος
    i = int(input("Δώσε σειρά:"))
    j = int(input("Δώσε στήλη:"))
    if Board[i][j] == " ":
        Board[i][j] = "X"
        moves = moves + 1
        #Μόνο αν έπαιξε ο άνθρωπος σωστά θα παίξει και ο υπολογιστής
        #Και μόνο αν δεν κέρδισε ήδη ο άνθρωπος
        if not GameWon(Board):
            #Παίζει ο Υπολογιστής
            if moves < 9:
                i = 0
                j = 0
                while Board[i][j] != " ":
                    i = random.randint(0, 2)
                    j = random.randint(0, 2)
                Board[i][j] = "O"
                moves = moves + 1

print()
PrintBoard(Board)
print("Λήξη παιχνιδιου!")