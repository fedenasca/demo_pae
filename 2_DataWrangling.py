#################################################################################
#	PROYECTO:																	#
# 			MODELO 1: Modelo predictivo de propension a la compra de PIRs		#
#################################################################################

#-------------------------------------------------------------------------------#
#	PASO 2: 	DATA WRANGLING										        	#
#-------------------------------------------------------------------------------#

#Revision: 1 (1-mar-2019)
#running mode: on cluster Spark
#Version Spark: 2.2.0
#Version Python: 2.7.5
#Autor: Matias F. Nasca

#Descripcion: DATA WRANGLING
#					Variable Selection 
# 					Filter values 
# 					Data Cleaning 
#					Data Enrichment

#################################################################################
#	LIBRERIAS Y MODULOS															#
#################################################################################

# Paths
from path_vars import *

# Configuracion de Spark
from spark_conf import *

# Funciones personalizadas
from AUX_F_pirs_spark_modelo1 import *

#################################################################################
#	CONFIGURACION DEL LOG 														#
#################################################################################

today = datetime.datetime.now().strftime('%Y-%m-%d')  # La fecha de hoy en formato yyyy-mm-dd
logging.basicConfig(filename=os.path.join(logs_path, 'mn_pirs_model1_dw.log'),
					level=logging.INFO,
					format='%(asctime)s %(message)s', 
					datefmt='%m/%d/%Y %I:%M:%S %p')

#################################################################################
#	LECTURA DEL CONFIG INI 														#
#################################################################################

config = configparser.ConfigParser()
config.read_file(open(os.path.join(source_path, 'config.ini')))

#################################################################################
#	INICIO DEL PROGRAMA															#
#################################################################################
logging.info('STEP 2: DATA WRANGLING... running')

# VARIABLES DE INTERES
from F_AUX_VS_pirs_spark_modelo1 import * #raw variables
from F_AUX_VD_pirs_spark_modelo1 import * #derivated variables

# FUNCIONES DE FILTRADO
def dataWNfilter(df):
	"""
	Reduce el dataframe segun el/los filtro/s aplicado/s. 
	:param df: spark dataframe
	:return: el dataframe modificado (filtrado)
	"""
	
	#WIDE
	df = wide_filter(df,'combinado')

	#NARROW
	df = narrow_filter(df,"mb_total_qt")
	df = narrow_filter(df,"arpu_negocio_promedio")

	return df

# FUNCIONES DE LIMPIEZA
def dataCleaning(df):
	"""
	Realiza el proceso de formateo de tipo de variables, imputacion de nulos,  
	transformacion y limpieza de variables categoricas.
	:param df: spark dataframe
	:return: el dataframe modificado
	"""
	
	#FORMATING
	df = convertNulls(df)
	df = transformVar(df,raw_variables_int_F,'int')
	df = transformVar(df,raw_variables_float_F,'float')
	df = transformVar(df,raw_variables_string_F,'string')
	df = convert_month_dt(df)

	#HANDLING MISSING VALUES
	df = fillNAList(df,raw_variables_int_F,'0') 
	df = fillNAList(df,raw_variables_float_F,'median')
	df = fillNAList(df,raw_variables_string_F,'NULL')

	#TRANSFORMATION
	df = arreglaTecnologiaEquipo(df)
	df = arregla_no_informadoLIST(df,raw_variables_string_F)
	
	return df

# FUNCIONES DE ENRIQUECIMIENTO
def dataEnrichment(df):
	"""
	Realiza el proceso de creacion de variables derivadas (transformaciones, agrupamiento, 
	tendencias, historicas, etc.) y filtros utiles.
	:param df: spark dataframe
	:return: el dataframe modificado
	"""
	# TRANSFORMATIONS (NEW VARIABLES)
	# df = df.withColumn('larpu_negocio', log('arpu_negocio_promedio')) 
	
	# COMBINATED TRANSFORMATIONS
		#Sums
	df = sumCols(df,sum_variables1,"trafico_funapp") #generamos: Sumatoria del trafico de Funapp
	df = sumCols(df,sum_variables2,"min_llamadas_totales") #generamos: Sumatoria del minutos entrantes + minutos salientes
	df = sumCols(df,sum_variables3,"qt_llamadas_totales") #generamos: Sumatoria de la cantidad de llamadas entrantes + minutos
	df = sumCols(df,sum_variables4,"dias_funapp") #generamos: Sumatoria de la cantidad de dias de uso de funapp

		#Multis
	df = MultiVars(df,"mb_total_qt","min_llamadas_totales") #generamos: Multiplicacion trafico (mb) y llamadas (min)
	df = MultiVars(df,"amt_pack_pirs","amt_bono") #generamos: Multiplicacion pirs ($) y bono ($)
	df = MultiVars(df,"amt_pack_pirs","amt_multi") #generamos: Multiplicacion pirs ($) y multi ($)
	df = MultiVars(df,"trafico_funapp","dias_funapp") #generamos: Multiplicacion trafico funapp(mb) ($) y dias de uso
	
		#Ratios 
	df = ratioVars(df, "amt_pack_pirs", "amt_recarga")
	df = ratioVars(df, "qt_pack_pirs", "qt_recarga")
	df = ratioVars(df, "trafico_funapp", "mb_total_qt")

	# HISTORICS
	df=shiftMonthlyList(df, historic_n1_variables,1) #n1
	df=shiftMonthlyList(df, historic_n2_variables,2) #n2

	# SUM ACCUMULATED
	#df=lastMonthsSUMList(df, accumulated_n3_variables, 3)

	# TRENDS, AVERAGES, HISTORICS
	df = trendVarList(df, trends_variables,'median') 

	return df

# MAIN SCRIPT
def main():
	"""
	DATA WRANGLING.
	PASOS: 
		1) Carga del "raw_dataset_table"
		2) Seleccion de variables "raw_variables" del "raw_dataset_table"
		3) Reduccion de dataset de (2), segun el filtro/s aplicado/s 
		4) Proceso de data CLeaning de (3)
		5) Proceso de agregado de nuevas variables 
		6) Dataset definitivo (stored in HDFS)
	"""
	
	# 1) LOAD DATASET
	logging.info('		1) Load raw dataset')
	raw_dataset_table = 'sbx_plan_bienvenida.mn_pirs_model1_ds_0' 	# Raw Dataset 
	begining_db = str(config.get('pirs_modelo1', 'begining_db'))
	end_db = str(config.get('pirs_modelo1', 'end_db'))
	df = sqlContext.sql("select * from " + raw_dataset_table + 
						"\n where month_dt between " + begining_db + " and " + end_db)
	logging.info('				Raw Dataset shape:  # Rows: ' + str(df.count()) + ' | # Columns: ' + str(len(df.columns)))
	
	# 2) VARIABLE SELECTION
	logging.info('		2) Variable selection')
	df = df[raw_variables_F]	# Selected variables
	logging.info('				# Selected variables: ' + str(len(df.columns)))

	# 3) FILTERING
	logging.info('		3) Filtering')
	df = dataWNfilter(df)
	logging.info('				Filtered Dataset shape:  # Rows: ' + str(df.count()) + ' | # Columns: ' + str(len(df.columns)))

	# 4) DATA CLEANING
	logging.info('		4) Data Cleaning')
	df = dataCleaning(df)

	# 5) DATA ENRICHMENT
	logging.info('		5) Data Enrichment')
	df = dataEnrichment(df)

	# 6) FINAL DATASET
	logging.info('		6) Updating hive table')
	updateHiveTable(df = df,
					name = 'mn_pirs_model1_dw',
					mode = 'overwrite')
	   


if __name__ == '__main__':
	try:
		main()
	except Exception as e:
		logging.exception('[KO] Script finished with errors')
		sys.exit(1)
	else:
		logging.info('STEP 2: DATA WRANGLING... done! \n')
		logging.info('[OK] Script finished correctly  \n \n')