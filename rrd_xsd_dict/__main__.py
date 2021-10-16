# coding; utf-8
import logging

from rrd_xsd_dict.xds import XSDDict

logger = logging.getLogger(__name__)


def createParser():
    """
    Объявление параметров командной строки

    :return: объект с определенными параметрами
    :rtype: argparse.ArgumentParser
    """
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument('-d', '--dictionary',
                        help='Имя словаря с расширением. Например: dAllDocumentsOut_v03.xsd',
                        type=str,
                        required=True
                        )
    parser.add_argument('-i', '--input',
                        help='Код/текст для поиска. Например: "008001000000" или "Паспорт гражданина СССР"',
                        type=str,
                        required=True
                        )
    parser.add_argument('-o', '--output',
                        help='Файл для вывода данных. По умолчанию: stdout',
                        type=argparse.FileType(encoding='utf-8', mode='w'),
                        default='-')
    parser.add_argument('-r', '--reverse',
                        help='Выполнить обратную операцию (получение кода по тексту)',
                        action='store_true')
    return parser


def main():
    parser = createParser()
    args = parser.parse_args()

    dict_name = args.dictionary
    dict_code = args.input
    xsd_dict = XSDDict(dict_name)
    args.output.write(xsd_dict.value2code(dict_code) if args.reverse else xsd_dict.code2value(dict_code))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
