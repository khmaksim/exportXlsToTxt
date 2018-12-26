import xlrd
from time import gmtime, strftime

def exportXlsToTxt(source, target):
	if source != '' and target != '':
		rb = xlrd.open_workbook(source)	#, formatting_info=True)

		sheet = rb.sheet_by_index(0)	# read first sheet file

		vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]

		target_file = open(target + '\\' + strftime("%Y%m%d_%H%M%S.txt", gmtime()), 'w')
		for row in vals:
			target_file.write(str(row[2]))
			target_file.write('\n')
			target_file.write(str(row[3]))
			target_file.write('\n')
			target_file.write(str(int(row[4])))
			target_file.write('\n')
			target_file.write('\n')
			target_file.write('1')
			target_file.write('\n')

		target_file.close()

		return True

	return False
