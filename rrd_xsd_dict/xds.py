# coding: utf-8
import re

from pathlib import Path

from lxml import etree
from lxml.etree import _Element


def nodes2str(nodes):
    """
    Функция извлечения из списка(элемента) текстового значения

    :param nodes:
    :type: list, str
    :return: строковое значение
    """
    if (type(nodes) == list and len(nodes) == 0) or (nodes is None):
        return

    if type(nodes) == list:
        if len(nodes) == 1:
            value = nodes2str(nodes[0])
        else:
            value = ', '.join([nodes2str(node) for node in nodes])
    elif type(nodes) == _Element:
        value = nodes.text
    else:
        value = nodes

    # NOTE: Дополнительная проверка. Т.к. в одном месте наткнулись на то, что элемент есть, то возвращает None
    if value is not None:
        value = re.sub(r'[\r\n\t]', ' ', value).strip()
        value = re.sub(r'^[\-]', '', value)  # удалиние дефисов в начале строки
        value = re.sub(r'&quot;', '', value)
        value = re.sub(r'\(\)', '', value)  # удаление пустых скобок в конце номера
    # NOTE: пусты скобки появляются в выписках из ЕГРН для многоконтурных участков если в контуре не задан его номер
    return value


class XSDDict:
    """Класс для инициализации словаря и получения"""
    def __init__(self, dict_name):
        path_to_dict = Path(__file__).parent / 'dict' / dict_name
        self.tree = etree.parse(str(path_to_dict))
        self.root = self.tree.getroot()

    def code2value(self, code):
        nodes = self.root.xpath('.//xs:enumeration[@value={}]/xs:annotation/xs:documentation/text()'.format(code),
                                namespaces=self.root.nsmap
                                )
        return nodes2str(nodes)

    def value2code(self, value):
        nodes = self.root.xpath('//xs:documentation[text() = "{}"]/parent::*/parent::*/@value'.format(value),
                                namespaces=self.root.nsmap)
        return nodes2str(nodes)


def value_from_xsd(dict_name, code):
    """
    Общая фукнция получения значения по коду и наоборот

    :param str dict_name: имя файла словаря
    :param str code: код или текстовое значения для обратного поиска
    :return: текстовое значение или код при обратном поиске
    :rtype: str
    """
    xsd_dict = XSDDict(dict_name)
    if code.isalnum():
        return xsd_dict.code2value(code)
    else:
        return xsd_dict.value2code(code)
