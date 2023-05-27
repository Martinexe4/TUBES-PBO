class Keyboard:
    __key_input = 0

    def get_key_input():
        return Keyboard.__key_input
    
    def set_key_input(key_input):
        Keyboard.__key_input = key_input
    
    def reset_Keyboard_input():
        Keyboard.__key_input = 0