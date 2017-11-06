import pandas as pd
import xlsxwriter
import comparacao

universidades = pd.read_excel('/home/victor/Área de Trabalho/Lista_santander.xls')
universidades = universidades['DESCRICAO']

instituicoes = pd.read_excel('/home/victor/Área de Trabalho/Pasta.xlsx')
instituicoes = instituicoes['Instituicao']

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('/home/victor/Área de Trabalho/universidades.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write(0, 0, 'Tabela1')
worksheet.write(0, 1, 'Tabela2')
worksheet.write(0, 2, 'Taxa de Similaridade')
i = 0
j = 0

for nome1 in universidades:
    i = i + 1
    j = 0
    for nome2 in instituicoes:
        j = j + 1
        if comparacao.sml(nome1.lower(), nome2.lower()) > 8:
            #teste.write(nome1 + " na linha:" + str(i) + " e " + nome2 + " na linha: " + str(j) + "\n")
            worksheet.write(i, 0, nome1)
            worksheet.write(i, 1, nome2)
            worksheet.write(i, 2, comparacao.sml(nome1.lower(), nome2.lower()))

            break

workbook.close()
#teste.close()
