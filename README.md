# Semantix
Desafio Engenheiro de Dados

## 1) Qual o objetivo do comando cache em Spark?
R: Cache no Spark, serve para armazenar o estado de um RDD em Memória, para que possa ser utilizado posteriormente sem fazer transformação.

## 2) O mesmo código implementado em Spark é normalmente mais rápido que a implementação equivalente em
MapReduce. Por quê?
R: O Spark por realizar o processamento em Memória, chega a ser até 100X mais rápido que o MapReduce, que precisa fazer o I/O no Disco para realizar o processamento.

## 3) Qual é a função do SparkContext ?
R: A função do SparkContext é setar as configurações dos serviços do Spark e realizar a conexão com o Cluster.

## 4) Explique com suas palavras o que é Resilient Distributed Datasets (RDD).
R: RDD é DataSet, tolerante a falhas, que armazena os dados em Memória e realiza o processamento Distribuido. Ele pode ser criado de 2 formas, carregando dataset externo ou uma collection no seu programa. Ele possui 2 operações: Transformação e Ação.
Transformação -> Cria um novo RDD, exemplo o Map.
Ações -> Retornam as informações do RDD, exemplo first().


## 5) GroupByKey é menos eficiente que reduceByKey em grandes dataset. Por quê?
R: Ele é menos eficiente porque, agrupa os dados dentro da partição e envia pela rede, sem ser feito o shuffle. Com isso ele acaba enviando mais dados e gastando mais tempo para realizar o shuffle de todas as partições no final.

## 6) Explique o que o código Scala abaixo faz.
```python
val textFile = sc.textFile ( "hdfs://..." ) #Cria um RDD com os dados lidos do HDFS
val counts = textFile . flatMap ( line => line . split ( " " )) #Quebra as palavras por espaço em branco
    .map ( word => ( word , 1 )) # Adiciona uma chave para cada palavra "Map"
    .reduceByKey ( _+_ ) # Faz o reduce e a contagem das palavras "chaves iguais"
counts . saveAsTextFile ( "hdfs://..." ) # Salva o resultado no hdfs
```
#### Esse codigo faz o WordCount


# ------------ Questões ------------------

 ## 1) - Número​ ​de​ ​hosts​ ​únicos: 137979


 ## 2) - O​ ​total​ ​de​ ​erros​ ​404: 20900


 ## 3) - Os​ ​5​ ​URLs​ ​que​ ​mais​ ​causaram​ ​erro​ ​404: 
 #### [(u'hoohoo.ncsa.uiuc.edu', 251), 
 #### (u'piweba3y.prodigy.com', 157), 
 #### (u'jbiagioni.npt.nuwc.navy.mil', 132), 
 #### (u'piweba1y.prodigy.com', 114), (u'www-d4.proxy.aol.com', 91)]


 ## 4) - Quantidade​ ​de​ ​erros​ ​404​ ​por​ ​dia: 

1. (u'08/Jul/1995', 302)
2. (u'26/Aug/1995', 366)
3. (u'04/Aug/1995', 346)
4. (u'22/Jul/1995', 192)
5. (u'04/Jul/1995', 359)
6. (u'31/Aug/1995', 526)
7. (u'13/Aug/1995', 216)
8. (u'26/Jul/1995', 336)
9. (u'17/Jul/1995', 406)
10. (u'17/Aug/1995', 271)
11. (u'08/Aug/1995', 391)
12. (u'13/Jul/1995', 531)
13. (u'22/Aug/1995', 288)
14. (u'21/Jul/1995', 334)
15. (u'10/Aug/1995', 315)
16. (u'07/Aug/1995', 537)
17. (u'07/Jul/1995', 570)
18. (u'14/Jul/1995', 413)
19. (u'10/Jul/1995', 398)
20. (u'21/Aug/1995', 305)
21. (u'25/Jul/1995', 461)
22. (u'18/Jul/1995', 465)
23. (u'14/Aug/1995', 287)
24. (u'03/Jul/1995', 474)
25. (u'03/Aug/1995', 304)
26. (u'29/Aug/1995', 420)
27. (u'18/Aug/1995', 256)
28. (u'25/Aug/1995', 415)
29. (u'15/Aug/1995', 327)
30. (u'06/Aug/1995', 373)
31. (u'24/Aug/1995', 420)
32. (u'19/Jul/1995', 639)
33. (u'28/Aug/1995', 410)
34. (u'20/Jul/1995', 428)
35. (u'19/Aug/1995', 209)
36. (u'06/Jul/1995', 640)
37. (u'15/Jul/1995', 254)
38. (u'02/Jul/1995', 291)
39. (u'28/Jul/1995', 94)
40. (u'24/Jul/1995', 328)
41. (u'11/Aug/1995', 263)
42. (u'20/Aug/1995', 312)
43. (u'11/Jul/1995', 471)
44. (u'05/Jul/1995', 497)
45. (u'01/Aug/1995', 243)
46. (u'16/Jul/1995', 257)
47. (u'27/Jul/1995', 336)
48. (u'12/Aug/1995', 196)
49. (u'27/Aug/1995', 370)
50. (u'12/Jul/1995', 471)
51. (u'30/Aug/1995', 571)
52. (u'23/Jul/1995', 233)
53. (u'09/Jul/1995', 348)
54. (u'16/Aug/1995', 259)
55. (u'05/Aug/1995', 236)
56. (u'01/Jul/1995', 316)
57. (u'23/Aug/1995', 345)
58. (u'09/Aug/1995', 279)


## 5) - O​ ​total​ ​de​ ​bytes​ ​retornados: 65524314915


# *******************************************
##                FIM DO TESTE               
# *******************************************
