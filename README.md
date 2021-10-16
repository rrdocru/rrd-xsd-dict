# RRD-XDS-DICT
Пакет для получения текстового описания по коду из словарей в формате xsd-файлов

# Пример использования
```cmd
pip install rrd-xsd-dict

rrd-xsd-dict -d dAllDocumentsOut_v03.xsd -i 008001009000
Временное удостоверение, выданное взамен военного билета

rrd-xsd-dict -d dAssBuilding_v01.xsd -i "Нежилое здание" --reverse
204001000000
```