# Criado por: Moisés Pereira
# Data: 22/07/2018
# 
from pyspark 		import SparkContext, SparkConf
from pyspark.sql 	import SQLContext

# Configuração da Aplicação Spark 
conf            = SparkConf().setAppName('Test_Semantix_Nasa')
sc              = SparkContext(conf=conf) 

# Arquivos de Log adicionados ao HDFS
file_log_jul95  = "/user/nasa/access_log_Jul95"
file_log_aug95  = "/user/nasa/access_log_Aug95"

# Criação e concatenação dos RDDs
rdd_jul 	    = sc.textFile(file_log_jul95)
rdd_aug 	    = sc.textFile(file_log_aug95)
rdd_logs        = rdd_jul + rdd_aug


# 1 - Número de hosts únicos.
hosts = rdd_logs.map(lambda x: (x.split(' - - [')[0])).distinct().count()
print("\n\n 1) - Número​ ​de​ ​hosts​ ​únicos: " + str(hosts))


# 2 - O total de erros 404.
err_404 = rdd_logs.filter(lambda x: x[-5:] == '404 -').count()
print("\n\n 2) - O​ ​total​ ​de​ ​erros​ ​404: " + str(err_404) )


# 3 - As​ ​5​ ​URLs​ ​que​ ​mais​ ​causaram​ ​erro​ ​404
# Atribuicao da Chave e Valor
# Negativo para pegar o valor na ordem decrescente
url_5_404 = rdd_logs.filter(lambda x: x[-5:] == '404 -')\
    .map(lambda x: ((x.split(' - - [')[0]), 1))\
    .reduceByKey(lambda k, v: k + v)\
    .takeOrdered(5, lambda x: -x[1])
print("\n\n 3) - Os​ ​5​ ​URLs​ ​que​ ​mais​ ​causaram​ ​erro​ ​404: " + str(url_5_404) )


# 4 - Quantidade​ ​de​ ​erros​ ​404​ ​por​ ​dia.
err_404_dia = rdd_logs.filter(lambda x: x[-5:] == '404 -')\
	.map(lambda x: ( ( x.split('[')[1][:11] ), 1))\
	.reduceByKey(lambda k, v: k + v)
print( "\n\n 4) - Quantidade​ ​de​ ​erros​ ​404​ ​por​ ​dia: \n")
for i in err_404_dia.collect():
	print( str(i) )


# 5 - O​ ​total​ ​de​ ​bytes​ ​retornados.
bytes_por_linha = rdd_logs.map(lambda x: x.split(" ")[-1])
numericos = bytes_por_linha.filter(lambda x: x.isnumeric())
total_bytes = numericos.map(lambda x: int(x)).sum()

print("\n\n 5) - O​ ​total​ ​de​ ​bytes​ ​retornados: " + str(total_bytes))


print("\n\n *******************************************")
print("                FIM DO TESTE               ")
print("*******************************************")

