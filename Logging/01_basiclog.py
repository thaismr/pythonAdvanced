import logging


def main():
    logging.basicConfig(
        level=logging.DEBUG,
        filename='output.log'
    )
    logging.debug(' Basic debug message')
    logging.info(' Basic info message')
    logging.warning(' Basic warning message')
    logging.error(' Basic error message')
    logging.critical(' Basic critical message')


if __name__ == "__main__":
    main()
