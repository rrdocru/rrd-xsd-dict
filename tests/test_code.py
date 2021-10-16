# coding: utf-8
from rrd_xsd_dict.xds import XSDDict, value_from_xsd


def test_dalldocumentsout_v03():
    """Тест получение кода из словаря dAllDocumentsOut_v03.xsd"""
    xsd_dict = XSDDict('dAllDocumentsOut_v03.xsd')
    assert xsd_dict.code2value("008001009000") == "Временное удостоверение, выданное взамен военного билета"
    assert xsd_dict.value2code("Военный билет военнослужащего") == "008001008000"


def test_dalloweduse_v02():
    """Тест получение кода из словаря dAllowedUse_v02.xsd"""
    xsd_dict = XSDDict('dAllowedUse_v02.xsd')
    assert xsd_dict.code2value("214001001001") == "Выращивание зерновых и иных сельскохозяйственных культур"
    assert xsd_dict.value2code("Выращивание зерновых и иных сельскохозяйственных культур") == "214001001001"


def test_dassbuilding_v01():
    """Тест получение кода из словаря dAssBuilding_v01.xsd"""
    xsd_dict = XSDDict('dAssBuilding_v01.xsd')
    assert xsd_dict.code2value("204001000000") == "Нежилое здание"
    assert xsd_dict.value2code("Нежилое здание") == "204001000000"
    assert xsd_dict.code2value("204002000000") == "Жилой дом"
    assert xsd_dict.value2code("Жилой дом") == "204002000000"


def test_dassflat_v01():
    """Тест получение кода из словаря dAssFlat_v01.xsd"""
    xsd_dict = XSDDict('dAssFlat_v01.xsd')
    assert xsd_dict.code2value("206001000000") == "Нежилое помещение"
    assert xsd_dict.value2code("Нежилое помещение") == "206001000000"
    assert xsd_dict.code2value("206002000000") == "Жилое помещение"
    assert xsd_dict.value2code("Жилое помещение") == "206002000000"


def test_dcategories_v01():
    """Тест получение кода из словаря dCategories_v01.xsd"""
    xsd_dict = XSDDict('dCategories_v01.xsd')
    assert xsd_dict.code2value("003005000000") == "Земли лесного фонда"
    assert xsd_dict.value2code("Земли лесного фонда") == "003005000000"


def test_ddocuments():
    """Тест получение кода из словаря dDocuments.xsd"""
    xsd_dict = XSDDict('dDocuments.xsd')
    assert xsd_dict.code2value("010001000000") == "Закон"
    assert xsd_dict.value2code("Закон") == "010001000000"
    assert xsd_dict.code2value("010002003000") == "Передаточный акт"
    assert xsd_dict.value2code("Передаточный акт") == "010002003000"


def test_dencumbrances_v03():
    """Тест получение кода из словаря dEncumbrances_v03.xsd"""
    xsd_dict = XSDDict('dEncumbrances_v03.xsd')
    assert xsd_dict.code2value("022001001000") == "Публичный сервитут"
    assert xsd_dict.value2code("Публичный сервитут") == "022001001000"


def test_dgovernance():
    """Тест получение кода из словаря dGovernance.xsd"""
    xsd_dict = XSDDict('dGovernance.xsd')
    assert xsd_dict.code2value("007001001001") == "Российская Федерация"
    assert xsd_dict.value2code("Российская Федерация") == "007001001001"


def test_dparcels_v01():
    """Тест получение кода из словаря dParcels_v01.xsd"""
    xsd_dict = XSDDict('dParcels_v01.xsd')
    assert xsd_dict.code2value("02") == "Единое землепользование"
    assert xsd_dict.value2code("Единое землепользование") == "02"


def test_drealty_v03():
    """Тест получение кода из словаря dRealty_v03.xsd"""
    xsd_dict = XSDDict('dRealty_v03.xsd')
    assert xsd_dict.code2value("002001000000") == "Объекты учёта и регистрации"
    assert xsd_dict.value2code("Объекты учёта и регистрации") == "002001000000"
    assert xsd_dict.code2value("002001004002") == "Условная часть линейного сооружения"
    assert xsd_dict.value2code("Условная часть линейного сооружения") == "002001004002"


def test_dregionsrf_v01():
    """Тест получение кода из словаря dRegionsRF_v01.xsd"""
    xsd_dict = XSDDict('dRegionsRF_v01.xsd')
    assert xsd_dict.code2value("01") == "Республика Адыгея (Адыгея)"
    assert xsd_dict.value2code("Республика Адыгея (Адыгея)") == "01"


def test_drights_v02():
    """Тест получение кода из словаря dRights_v02.xsd"""
    xsd_dict = XSDDict('dRights_v02.xsd')
    assert xsd_dict.code2value("001002000000") == "Общая долевая собственность"
    assert xsd_dict.value2code("Общая долевая собственность") == "001002000000"


def test_dunit_v01():
    """Тест получение кода из словаря dUnit_v01.xsd"""
    xsd_dict = XSDDict('dUnit_v01.xsd')
    assert xsd_dict.code2value("055") == "Квадратный метр"
    assert xsd_dict.value2code("Квадратный метр") == "055"


def test_dutilizations_v01():
    """Тест получение кода из словаря dUtilizations_v01.xsd"""
    xsd_dict = XSDDict('dUtilizations_v01.xsd')
    assert xsd_dict.code2value("141003000000") == "Для ведения личного подсобного хозяйства"
    assert xsd_dict.value2code("Для ведения личного подсобного хозяйства") == "141003000000"


def test_value_from_xsd():
    """Тест получение значения общей функцией и наоборот"""
    assert value_from_xsd("dUtilizations_v01.xsd", "141003000000") == "Для ведения личного подсобного хозяйства"
    assert value_from_xsd("dUtilizations_v01.xsd", "Для ведения личного подсобного хозяйства") == "141003000000"
