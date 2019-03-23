from django.db import models

from django.contrib.auth.models import User

class State(models.Model):
    player              = models.ForeignKey(User, on_delete=models.CASCADE)
    duskball_is         = models.BooleanField()
    haunted_painting_is = models.BooleanField()
    lucario_is          = models.BooleanField()
    computer_on         = models.BooleanField()
    poke_ball_is        = models.BooleanField()
    left_corner_is      = models.BooleanField()
    right_corner_is     = models.BooleanField()
    bookshelf_is        = models.BooleanField()
    bear_is             = models.BooleanField()
    move_ball_down      = models.BooleanField()
    ball_gone           = models.BooleanField()
    scroll_is           = models.BooleanField()
    stair_collision     = models.IntegerField()
    cabnet_collision    = models.IntegerField()
    rail2_collision     = models.IntegerField()  
    duskball_collision  = models.IntegerField()
    painting_collision  = models.IntegerField()
    haunted_collision   = models.IntegerField()
    lucario_collision   = models.BooleanField()
    timestamp           = models.DateTimeField(auto_now_add=True)


    # def __str__(self):
    #     return self.player


class Game(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    time   = models.IntegerField() # the duration of the game in seconds
    level  = models.IntegerField()
    gold   = models.IntegerField()
    score  = models.IntegerField()

    timestamp = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.player

class Mode(models.Model):
    name          = models.CharField(max_length=100)
    snowman_delay = models.IntegerField()
    avocado_delay = models.IntegerField()
    speed         = models.IntegerField()

    def __str__(self):
        return self.name

