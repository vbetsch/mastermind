from src.Container import Container

container = Container()

def main():
    cli = container.cli()
    try:
        cli.start()
    except KeyboardInterrupt:
        cli.cancel()

if __name__ == '__main__':
    main()
