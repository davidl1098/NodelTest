from __future__ import print_function

import os.path
import pandas as pd
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Permissions requested by Google for project to work
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']


# Authorization function to access Drive and Sheets
def auth():
    creds = None

    # if token already exists use it to authenticate into the app
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # if no let the user log in with Goggle Account.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())


# Create PivotResults sheet given a spreadsheet
# BE SURE TO NOT EXIST ANOTHER TAB/SHEET WITH THE NAME "PivotResults"
def create(spreadsheet_id):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    try:
        service = build('sheets', 'v4', credentials=creds)
        body = {
            'requests': [{
                'addSheet': {
                    "properties": {
                        "title": "PivotResults"
                    }
                }
            }]
        }
        spreadsheet = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=body).execute()
        target_sheet_id = spreadsheet.get('replies')[0] .get('addSheet').get('properties').get('sheetId')
        print(f"Spreadsheet ID: {(spreadsheet.get('spreadsheetId'))}")
        return target_sheet_id
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error


# return specific values based on a range
def get_values(spreadsheet_id, range_name):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    try:
        service = build('sheets', 'v4', credentials=creds)
        result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
        rows = result.get('values', [])
        print(f"{len(rows)} rows retrieved")
        return result
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error


# update specific values based on a range
def update_values(spreadsheet_id, range_name, value_input_option, _values):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    try:
        service = build('sheets', 'v4', credentials=creds)
        body = {
            'values': _values
        }
        result = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range=range_name,
                                                        valueInputOption=value_input_option, body=body).execute()
        print(f"{result.get('updatedCells')} cells updated.")
        return result
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error


# converts a number to its equivalent excel column letter
def number_to_excel_letter(column_int):
    start_index = 1  # it can start either at 0 or at 1
    letter = ''
    while column_int > 25 + start_index:
        letter += chr(65 + int((column_int - start_index) / 26) - 1)
        column_int = column_int - (int((column_int - start_index) / 26)) * 26
    letter += chr(65 - start_index + (int(column_int)))
    return letter


# fills matrix with false
def fill_with_false(rows, cols):
    false_list_rows = []
    false_list = []
    for i in range(cols):
        false_list.append('False')
    for j in range(rows - 1):
        false_list_rows.append(false_list)
    return false_list_rows


# calculate indexes of countries where should change the value to true
def calculate_country_values(sheet_id, all_data, base_columns, country_list):
    for value in all_data:
        for i in range(1, len(base_columns)):
            if value[0] == base_columns[i][0]:
                for j in range(0, len(country_list)):
                    if value[2] == country_list[j][0]:
                        row = str(i+2)
                        col = number_to_excel_letter(j + 3)
                        index = col+row
                        update_values(sheet_id, "'PivotResults'!"+index, "USER_ENTERED", [['True']])


# calculate indexes of themes where should change the value to true
def calculate_themes_values(sheet_id, all_data, base_columns, themes_list, country_list):
    for value in all_data:
        for i in range(1, len(base_columns)):
            if value[0] == base_columns[i][0]:
                for j in range(0, len(themes_list)):
                    if value[3] == themes_list[j][0]:
                        row = str(i+2)
                        col = number_to_excel_letter(j + 3 + len(country_list))
                        index = col+row
                        update_values(sheet_id, "'PivotResults'!" +index, "USER_ENTERED", [['True']])


# merge the headboard cells like the example
def merge_title_cells(spreadsheet_id, sheetId, start_row, end_row, start_col, end_col):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    try:
        service = build('sheets', 'v4', credentials=creds)

        requests = [{
            "mergeCells": {
                "range": {
                    "sheetId": sheetId,
                    "startRowIndex": start_row,
                    "endRowIndex": end_row,
                    "startColumnIndex": start_col,
                    "endColumnIndex": end_col
                },
                "mergeType": "MERGE_ALL"
            }
        }]

        body = {
            'requests': requests
        }
        response = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=body).execute()
        return response

    except HttpError as error:
        print(f"An error occurred: {error}")
        return error


if __name__ == '__main__':
    DATAID = '1nUvkzOWmONQ71hYP6EwLoR06cJkqtN1YlrZy31S_AKo'
    PIVOTID = create(DATAID)
    auth()

    # DATAID = input("Enter the spreadsheet id of the data: ")

    # obtain all the necessary values from the data sheet
    print("----- Getting data from data sheet")
    all_values = get_values(DATAID, "A2:D").get('values', [])
    base = get_values(DATAID, "A:B").get('values', [])
    countries = get_values(DATAID, "C2:C").get('values', [])
    themes = get_values(DATAID, "D2:D").get('values', [])

    # get unique values for countries, themes and authors
    unique_base_columns = []
    for x in base:
        if x not in unique_base_columns:
            unique_base_columns.append(x)

    unique_country_list = []
    country_columns = []
    for x in countries:
        if x not in unique_country_list:
            unique_country_list.append(x)
    country_columns.append(sum(unique_country_list, []))
    country_end_letter = number_to_excel_letter(len(unique_country_list) + 2)

    unique_themes_list = []
    theme_columns = []
    for x in themes:
        if x not in unique_themes_list:
            unique_themes_list.append(x)
    theme_columns.append(sum(unique_themes_list, []))
    theme_start_letter = number_to_excel_letter(len(unique_country_list) + 3)
    theme_end_letter = number_to_excel_letter(len(unique_country_list) + 2 + len(unique_themes_list))

    # fills with false
    false_list = fill_with_false(len(unique_base_columns), len(unique_country_list) + len(unique_themes_list))

    # builds the PivotResult columns and general structure
    print("----- Building PivotResults sheet structure ")
    update_values(DATAID, "'PivotResults'!C1", "USER_ENTERED", [['Countries']])
    update_values(DATAID, "'PivotResults'!"+theme_start_letter+"1", "USER_ENTERED", [['Themes']])
    update_values(DATAID, "'PivotResults'!A2:B", "USER_ENTERED", unique_base_columns)
    update_values(DATAID, "'PivotResults'!C2:"+country_end_letter+"2", "USER_ENTERED", country_columns)
    update_values(DATAID, "'PivotResults'!"+theme_start_letter+"2:2", "USER_ENTERED", theme_columns)
    update_values(DATAID, "'PivotResults'!C3:"+theme_end_letter+str(len(unique_base_columns)+1), "USER_ENTERED", false_list)

    merge_title_cells(DATAID, PIVOTID, 0, 1, 2, len(unique_country_list)+2)
    merge_title_cells(DATAID, PIVOTID, 0, 1, len(unique_country_list)+2, len(unique_themes_list) + len(unique_country_list)+2)

    # calculate where to put true or false depending on the data
    print("----- Calculating info ")
    calculate_country_values(DATAID, all_values, unique_base_columns, unique_country_list)
    calculate_themes_values(DATAID, all_values, unique_base_columns, unique_themes_list, unique_country_list)





