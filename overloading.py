import logging

logging.basicConfig(filename='oops_log.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger()


class OverLoading:

    def argument(self, *args):
        try:
            addition = 0
            for i in args:
                addition += i
            return addition
        except Exception as ex:
            logger.exception(ex)

    def key_arguments(self, **kwargs):
        try:
            for key, value in kwargs.items():
                print(key, value)
        except Exception as ex:
            logger.exception(ex)


if __name__ == '__main__':
    oops = OverLoading()
    result1 = oops.argument(10)
    print(result1)
    result2 = oops.argument(10, 20)
    print(result2)
    result3 = oops.argument(10, 20, 30, 40)
    print(result3)
    oops.key_arguments(name="Elavarasu", roll_no="14AU013", year=2018)
