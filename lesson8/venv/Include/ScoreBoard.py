import pygame

class ScoreBoard:
    score=0
    time=0
    @staticmethod
    def init_ScoreBoard(rectangle=pygame.rect.Rect(0,50,200,50),textSize=100,textColor=(50,70,100)):
        ScoreBoard.textSize=textSize
        ScoreBoard.textColor=textColor
        ScoreBoard.rectangle=rectangle

    @staticmethod
    def set_Score(score=0):
        ScoreBoard.score+=score
        ScoreBoard.score_fontedText=pygame.font.Font("fonts/ARCADE.TTF",ScoreBoard.textSize).render(str(ScoreBoard.score),True,ScoreBoard.textColor)
        ScoreBoard.score_textRectangle=pygame.rect.Rect(0,0,ScoreBoard.score_fontedText.get_width(),ScoreBoard.score_fontedText.get_height())
        ScoreBoard.score_textRectangle.center=ScoreBoard.rectangle.center


    @staticmethod
    def draw(screen):
        screen.blit(ScoreBoard.score_fontedText,ScoreBoard.score_textRectangle)










