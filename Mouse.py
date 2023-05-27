class Mouse:
    __mouse_keklik = False
    __mouse_pos = (0,0)

    def get_mouse_keklik():
        return Mouse.__mouse_keklik
    
    def set_mouse_keklik():
        Mouse.__mouse_keklik = True
    
    def reset_mouse_keklik():
        Mouse.__mouse_keklik = False

    def set_mouse_pos(mouse_pos):
        Mouse.__mouse_pos = mouse_pos

    def mouse_pos_x():
        return Mouse.__mouse_pos[0]

    def mouse_pos_y():
        return Mouse.__mouse_pos[1]
    