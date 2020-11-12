import xlsxwriter

def excel_writer(returned_data, title):

    print("Excel writer func")
    worksheet_number = 1

    workbook = xlsxwriter.Workbook("out.xlsx")

    worksheet = workbook.add_worksheet()
    print("Worksheet name: {}".format(title))

    print("print from excel writer")
    print("title {}".format(title))
    worksheet.write("A1", "Symbols")
    worksheet.write("B1", title)

    row = 1
    col = 0

    for the_lists in returned_data:
        row +=1
        for dict in the_lists:
            for key, value in dict.items():
                if key == 'name':
                    worksheet.write(row, col, value)

                if key == 'id':
                    worksheet.write(row, col, value)

                elif key != 'phone' and key != 'name':
                    worksheet.write(row, col + 1, value)

            row += 1


    workbook.close()

