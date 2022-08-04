from box import Box
from prisoner import Prisoner
import random
import matplotlib.pyplot as plt

def generate_notes():
        randomize_notes = [x for x in range(1,101)]
        random.shuffle(randomize_notes)
        return randomize_notes

def generate_boxes_with_notes(box_list, note_list):
        box_list.clear()
     
        for x in range(1, 101):            
            box_list.append(Box(x, note_list[x - 1]))

def generate_prisoners(prisoner_list):
        prisoner_list.clear()
        for x in range(1, 101):
            prisoner_list.append(Prisoner(x, x))
    
def check_for_correct_note(box_list, prisoner):
        box_index = (prisoner.check_next_box) - 1                                               
        check_box = box_list[box_index]
        prisoner.check_note(check_box.note_number)
        return prisoner.free
                   

if __name__ == '__main__':
    
    success = 0
    failure = 0

    rounds = int(input("Rounds of simulations:(int) "))

    for round in range(rounds):
        all_boxes = []
        all_prisoners = []
        generate_boxes_with_notes(all_boxes, generate_notes())
        generate_prisoners(all_prisoners)

        freed_prisoner_count = 0        
        failed_prisoner = 0
        
        for prisoner in all_prisoners:
            if failed_prisoner == 1:                
                failure += 1
                break
            
            boxes_checked = 0
                          
            while boxes_checked < 50:                               
                if check_for_correct_note(all_boxes, prisoner):
                    freed_prisoner_count += 1
                    if freed_prisoner_count == 100:
                        success += 1                    
                    break
                    
                else:
                    box_index=(prisoner.check_next_box) - 1
                    boxes_checked += 1
                    if boxes_checked == 50:                        
                        failed_prisoner += 1
    
    bars=['Successes','Failures']
    values=[success, failure]
    new_colors=['green', 'red']
    
    plt.bar(bars, values, color = new_colors)
    plt.title('Prisoners and Boxes', fontsize = 14)
    plt.ylabel("Simulations")
    plt.xlabel("Outcomes")
    plt.text(0, values[0], f'{success}', fontsize = 14, ha = "center", va = "bottom")
    plt.text(1, values[1], f'{failure}', fontsize = 14, ha = "center", va = "bottom")
    plt.ylim(top = rounds)
    plt.show()




        
        
   