import logging


logger = logging.getLogger(__name__)

GAME_START_TIME = 63
GAME_END_TIME = 80


def valid_game(game_time, score_1, score_2):
    if GAME_START_TIME <= game_time <= GAME_END_TIME:
        if score_1 + score_2 <= 3 and score_1 != 3 and score_2 != 3:
            return True
    return False
