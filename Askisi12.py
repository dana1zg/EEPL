#Δημιουργία πίνακα συχνοτήτων για το αγγλικό αλφάβητο
CharacterFrequencyArray = [0 for i in range(26)]

fin = open("text.txt", "r")
for line in fin:
    line = str(line)
    line = line.upper()
    for char in line:
        if char >= 'A' and char <= 'Z':
            index = ord(char) - ord('A')
            CharacterFrequencyArray[index] += 1
fin.close()

print("Πίνακας Συχνοτήτων για αρχείο text.txt:")
print(CharacterFrequencyArray)

#Τώρα πρέπει να βρούμε το περισσότερο και το λιγότερο συχνά χρησιμοποιούμενο γράμμα και να τα αντικαταστήσουμε μεταξύ τους στο κείμενο
least_index = 0
most_index = 0
least_times = CharacterFrequencyArray[0]
most_times = CharacterFrequencyArray[0]

for i in range(len(CharacterFrequencyArray)):
    if CharacterFrequencyArray[i] > most_times:
        most_times = CharacterFrequencyArray[i]
        most_index = i
    elif CharacterFrequencyArray[i] < least_times:
        least_times = CharacterFrequencyArray[i]
        least_index = i

least_char = chr(ord('A')+ least_index)
most_char = chr(ord('A') + most_index)

print("Πιο συχνός χαρακτήρας:")
print(most_char)
print("Λιγότερο συχνός χαρακτήρας:")
print(least_char)

fin = open("text.txt", "r")
fout = open("text2.txt", "w")

print("Εγγραφή στο αρχείο text2.txt....")
for line in fin:
    line = str(line)
    line_out = line.upper()

    #Αποκλείεται ένα κείμενο με κεφαλαία να περιέχει α μικρό
    line_out = line_out.replace(most_char, 'a')
    line_out = line_out.replace(least_char, most_char)
    line_out = line_out.replace('a', least_char)
    fout.write(line_out)

fin.close()
fout.close()

print("Τέλος εγγραφής!")
