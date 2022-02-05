

def generate_seating_sequence(group1,group2,seats_p_row):
    n = 4*seats_p_row
    group1 = group1 + [' -']*(n//2-len(group1))
    group2 = group2 + [' -']*(n//2-len(group2))
    seating_sequence = ['']*(n)
    seating_sequence[::2] = group1
    seating_sequence[1::2] = group2
    return seating_sequence
#------------------------------------------------------------#    
def group_reverse_order(group):
    reverse_group = group[::-1]
    return reverse_group 
#------------------------------------------------------------#    
def display_exam_seating(seating_sequence):  # 4 -> 2 , 6 -> 4 , 8 -> 6
    bar_in_examroom = 3*(len(seating_sequence)//8 - 1) - 2
    print('-'*(2*bar_in_examroom + 11))
    print('|' +  ' '*(bar_in_examroom) + 'Exam Room' + ' '*(bar_in_examroom) + '|')
    print('-'*(2*bar_in_examroom + 11))
    print('|' + "|".join(seating_sequence[:len(seating_sequence)//4]) + '|')
    print('-'*(2*bar_in_examroom + 11))
    print('|' + "|".join(seating_sequence[len(seating_sequence)//4 : len(seating_sequence)//2]) + '|')
    print('-'*(2*bar_in_examroom + 11))
    print('|' + "|".join(seating_sequence[len(seating_sequence)//2 : len(seating_sequence)*3//4]) + '|')
    print('-'*(2*bar_in_examroom + 11))
    print('|' + "|".join(seating_sequence[len(seating_sequence)*3//4 : len(seating_sequence)]) + '|')
    print('-'*(2*bar_in_examroom + 11))
#------------------------------------------------------------#    
def main():
    
    group1 = input().split(",")
    group2 = input().split(",")
    seats_p_row = int(input())
    is_reverse = int(input())
    
    if is_reverse:
        group1 = group_reverse_order(group1)
        group2 = group_reverse_order(group2)
        
    if len(group1) > 2*seats_p_row or len(group2) > 2*seats_p_row:
        print("Room is too small. Get a bigger exam room!")
        return
    
    if seats_p_row < 4 or seats_p_row % 2 != 0:
        print("seats_p_row has to be more than 4 and has an even number.")
        return
    
    seating_sequence = generate_seating_sequence(group1,group2,seats_p_row)
    display_exam_seating(seating_sequence)

main()

