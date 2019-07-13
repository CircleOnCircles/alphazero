def newmodel(argv):
    import argparse
    parser = argparse.ArgumentParser(description='New model and save to .h5 file')
    parser.add_argument('game', help='a game name i.e. checkers')
    parser.add_argument('filename', nargs='?', default='latest.h5', help='save to filename')
    args = parser.parse_args(argv)

    from util import game
    nn = game.importNn(args.game)
    nn.init(args.filename)

if __name__ == '__main__':
    args={
            "game": "makhos",
            "filename": 'makhos_test.h5',
    }
    newmodel(args)