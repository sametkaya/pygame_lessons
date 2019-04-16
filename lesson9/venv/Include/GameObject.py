class GameObject():
    def __init__(self,screen):
        width=screen.get_width()
        height=screen.get_height()
        self.rectangle=pygame.rect.Rect(10,int(height/2)-int(height/5/2),int(width/5),int(height/5))

    def Draw(self):
        pass
