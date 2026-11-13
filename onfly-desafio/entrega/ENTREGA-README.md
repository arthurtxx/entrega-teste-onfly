No primeiro erro que aparecia no terminal (FAILED tests/test\_currency.py::test\_currency\_conversion\_to\_brl \- AssertionError: assert '118.45' \== '642.00') identifiquei que ao invés dele multiplicar a taxa de cambio, ele estava dividindo, sendo assim eu troquei os sinais e assim corrigi o erro, salvei e executei o pytest \-q

No segundo erro, (FAILED tests/test\_nights.py::test\_nights\_across\_month\_boundary \- assert \-28 \== 3), percebi que estava retornando e subtraindo checkout.day e ckeckin.day, nisso ele estava calculando os dias de forma errada, identifiquei o erro e corrigi com auxilio da ia.

No terceiro erro, (FAILED tests/test\_regression\_report.py::test\_regression\_report\_on\_sample \- AssertionError: assert {'average\_nig...ions': 0, ...} \== {'average\_nig...ions': 0, ...}), compara o relatório de regressão gerado pelo programa com valores esperados, esse erro indica que pelo menos um dos campos estava com valor diferente do esperado, após isso, Identifiquei que o erro estava relacionado a uma divergência entre os dados gerados pelo relatório de regressão e os valores esperados pelo teste e consertei.

No quarto erro, (FAILED tests/test\_status\_rules.py::test\_status\_rules\_exclude\_cancelled\_and\_no\_show \- AssertionError: assert '120.00' \== '100.00'), como o teste exclui apenas os cancelados, o no show tambem é considerado e acabava sendo contabilizado, então só o confirmado é considerado para os totais, logo após alterar, executei novamente e o erro sumiu.

No ultimo erro, (FAILED tests/test\_top\_hotels.py::test\_top\_hotels\_are\_ranked\_descending \- AssertionError: assert \['H04', 'H03', 'H02'\] \== \['H01', 'H02', 'H03'\]  
5 failed in 1.10s  
), ele queria o top3 de hoteis na ordem decrescente, basicamente com auxilio da ia eu alterei na linha do codigo apos identificar o erro, coloquei sinal de menos que inverte a ordem e o resultado saiu como o esperado.  
