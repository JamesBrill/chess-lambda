import os
import sys

here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "vendored"))


import json
import datetime
import chess
import chess.uci


def endpoint(event, context):
    position = "1k1r4/pp1b1R2/3q2pp/4p3/2B5/4Q3/PPP2B2/2K5 b - - 0 1"
    if os.environ.get('IS_LOCAL') == "true":
        engine_binary = "./stockfish_mac"
    else:
        engine_binary = "./stockfish_linux"
    engine = chess.uci.popen_engine(engine_binary)
    engine.uci()
    board = chess.Board(position)
    engine.position(board)
    bestmove, ponder = engine.go(movetime=2000)

    body = {
        "bestmove": str(bestmove),
        "ponder": str(ponder)
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
