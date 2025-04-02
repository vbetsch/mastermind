from src.Container import Container

container: Container = Container()

def main() -> None:
    cli = container.cli()
    try:
        cli.start()
    except KeyboardInterrupt:
        cli.cancel()

if __name__ == '__main__':
    main()
