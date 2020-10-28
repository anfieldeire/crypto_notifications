import xlsxwriter

def excel_writer(returned_data, title):

    worksheet_number = 1

    workbook = xlsxwriter.Workbook("out.xlsx")
    worksheet = workbook.add_worksheet(title)

    print("print from excel writer")
    worksheet.write("A1", "Symbols")
    worksheet.write("B1", title)

    row = 1
    col = 0

    for dict in returned_data:
        for key, value in dict.items():
            print("value {}".format(value))
            if key == 'id':
                worksheet.write(row, col, value)

           # elif key == 'price_change_24h':
            else:
                worksheet.write(row, col + 1, value)

        row += 1


    workbook.close()

