import comparacao
import xlsxwriter

x = "FACULDADE DE CIÊNCIAS HUMANAS DE ITABIRA (FACHI)"
y = "ESCOLA SUPERIOR DE PROPAGANDA E MARKETING (ESPM)"


msg = "Taxa de similaridade "
print(msg, 'entre x e y: ', comparacao.sml(x.lower(), y.lower()))

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('universidades.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write(0, 0, x)
worksheet.write(0, 1, y)
worksheet.write(0, 2, comparacao.sml(x.lower(), y.lower()))

workbook.close()
