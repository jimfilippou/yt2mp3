import yt2mp3

def main():
    cli = yt2mp3.cli.CLI()
    cli.prompt = "<yt2mp3> -> "
    cli.cmdloop("Starting app...")


if __name__ == '__main__':
    main()
