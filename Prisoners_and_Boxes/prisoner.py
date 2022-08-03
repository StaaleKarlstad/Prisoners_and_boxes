
class Prisoner:

    

    def __init__(self, number, number2):
        self.number=number
        self.check_next_box=number2
    
    free=False
    check_next_box=0
    
    def check_note(self, a):
        if a == self.number:
            self.free=True
        else:
            self.check_next_box=a
