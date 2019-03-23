from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from .models import Game, Mode, State

import json



def boat_view(request):

    return render(request, "boat/boat.html", {})
    


def home_view(request):
    modes = Mode.objects.all()
    states = []
    if request.user.is_authenticated:
        states = request.user.state_set.all()
    game_state = None
    if 'game_state' in request.GET: # check if the url has the query parameter
        game_state_id = request.GET['game_state']
        if request.user.state_set.filter(id=game_state_id).exists(): # check if the user has a game state with that id
            game_state = request.user.state_set.get(id=game_state_id) # go get the game state with that id
    context = {'modes': modes, 'states': states, 'game_state': game_state}
    return render(request, "boat/home.html", context)


def iguana_game_view(request):
    if 'game_mode' in request.GET:
        game_mode_id = request.GET['game_mode']
        game_mode = Mode.objects.get(id=game_mode_id)
    else:
        game_mode = Mode.objects.all()[0]
    average_time = 0
    gold = 0
    game_count = 0
    high_score = 0 
    if request.user.is_authenticated:
        games = request.user.game_set.all()
        for game in games:
            game_count += 1
            average_time += game.time
            gold += game.gold
        if average_time != 0:
            average_time /= game_count
    context = {'average_time':average_time, 'gold':gold, 'mode': game_mode}
    return render(request, "boat/iguana_game.html", context)


def instructions_view(request):

    return render(request, "boat/instructions.html", {})


def scores_view(request):
    all_scores = []
    high_score = 0
    top_3 = Game.objects.order_by('-score')[:3]
    # for game in games:
    #     all_scores.append(game.score)
    # all_scores.sort()
    # high_score = all_scores[]

    context = {'top_3':top_3}

    return render(request, "boat/scores.html", context)
            

def save_game(request):
    
    data = json.loads(request.body)
    game_time = data['game_time']
    game_level = data['game_level']
    game_score = data['game_score']
    gold_collected = data['gold_collected']
    player = request.user
    game = Game(score=game_score, level=game_level, gold=gold_collected, time=game_time, player=player)
    game.save()
    return HttpResponse('ok')
    
def save_state(request):
    
    data = json.loads(request.body)
    duskball_is = data['duskball_is']
    haunted_painting_is = data['haunted_painting_is']
    lucario_is = data['lucario_is']
    computer_on = data['computer_on']
    poke_ball_is = data['poke_ball_is']
    left_corner_is = data['left_corner_is']
    right_corner_is = data['right_corner_is']
    bookshelf_is = data['bookshelf_is']
    bear_is = data['bear_is']
    move_ball_down = data['move_ball_down']
    ball_gone = data['ball_gone']
    scroll_is = data['scroll_is']
    stair_collision = data['stair_collision']
    cabnet_collision = data['cabnet_collision']
    rail2_collision = data['rail2_collision']
    duskball_collision = data['rail2_collision']
    painting_collision = data['rail2_collision']
    haunted_collision = data['rail2_collision']
    lucario_collision = data['lucario_collision']
    player = request.user
    state = State(scroll_is=scroll_is, ball_gone=ball_gone, move_ball_down=move_ball_down, bear_is=bear_is, poke_ball_is=poke_ball_is, left_corner_is=left_corner_is, right_corner_is=right_corner_is, bookshelf_is=bookshelf_is, duskball_is=duskball_is, haunted_painting_is=haunted_painting_is, lucario_is=lucario_is, computer_on=computer_on, stair_collision=stair_collision, cabnet_collision=cabnet_collision, rail2_collision=rail2_collision, duskball_collision=duskball_collision, painting_collision=painting_collision, haunted_collision=haunted_collision, lucario_collision=lucario_collision, player=player)
    state.save()
    return HttpResponse('hi')


