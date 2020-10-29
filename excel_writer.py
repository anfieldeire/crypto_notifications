import xlsxwriter

def excel_writer(returned_data, title, j):

    print("Excel writer j: {}".format(j))
    worksheet_number = 1

    workbook = xlsxwriter.Workbook("out.xlsx")

    for i in range(j):

        worksheet = workbook.add_worksheet()
        print("Worksheet name: {}".format(title))

        print("print from excel writer")
        print("title {}".format(title))
        worksheet.write("A1", "Symbols")
        worksheet.write("B1", title)

        row = 1
        col = 0

        for dict in returned_data:
            for key, value in dict.items():
                print("value {}".format(value))
                if key == 'id':
                    worksheet.write(row, col, value)

                else:
                    worksheet.write(row, col + 1, value)

            row += 1


    workbook.close()

