from utilities.excel_manager import get_excel_sheet, get_dictionary_from_key, get_all_rows

# excel_name from resources/data
excel_name = "testData.xlsx"


def get_standard_credentials():
    excel_sheet = get_excel_sheet(excel_name, "credentials")
    return [get_dictionary_from_key(excel_sheet, "valid")]


def get_shopping_list():
    excel_sheet = get_excel_sheet(excel_name, "itemData")
    return [get_all_rows(excel_sheet)]


def get_sauce_labs_href():
    return ["https://saucelabs.com/"]
