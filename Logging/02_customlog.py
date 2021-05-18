import logging


def main():
    extra_data = {
        'data': 'value'
    }
    log_format = '%(asctime)s: %(levelname)s: %(module)s - %(funcName)s - %(filename)s [%(lineno)d]: %(message)s ' \
                 'Data:%(data)s'
    logging.basicConfig(
        level=logging.DEBUG,
        format=log_format,
        filename='custom.log'
    )

    logging.debug('Basic debug message', extra=extra_data)
    logging.info('Basic info message', extra=extra_data)
    logging.warning('Basic warning message', extra=extra_data)
    logging.error('Basic error message', extra=extra_data)
    logging.critical('Basic critical message', extra=extra_data)


if __name__ == "__main__":
    main()
