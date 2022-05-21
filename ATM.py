# ATM Debit System
notes = [1000,500,100,50,10,1]
rupee = int(input("Enter rupee : "))
j = 0
rs = rupee
note_freq = [0,0,0,0,0,0]
is_start = True

while True:
    for i in range(len(notes)):
        if(rs > notes[i] or ((rs == notes[i]) and (not is_start))):
            j = i
            break
    rs = rs - notes[j]
    note_freq[j] += 1
    if(rs == 0):
        break
    is_start = False
    
for i in range(len(note_freq)):
    if(note_freq[i] > 0):
        print(f"\n{notes[i]} : {note_freq[i]}\n")