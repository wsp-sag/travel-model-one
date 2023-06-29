:: convert-csv-to-dbf.bat
::
:: MS-DOS batch file that uses R to convert CSV files to DBF.

set CODE_DIR=D:\Projects\travel-model-one\utilities\taz-data-csv-to-dbf\
set R_DIR=E:\projects\ccta\31000190\R\R-4.0.4\bin\x64

set PATH=%R_DIR%;%PATH%

set YEAR_ARRAY=2020

for %%X in (%YEAR_ARRAY%) do (
	
	echo Converting %%X ...
	copy tazData%%X.csv input.csv
	call Rscript.exe --vanilla %CODE_DIR%\taz-data-csv-to-dbf.R
	copy output.dbf tazData%%X.dbf
	del output.dbf
	echo -------------------------------------------

	)
