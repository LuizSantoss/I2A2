TAREFA5

📝 Sobre
Sistema em Python para monitorar ninhos de tartarugas em comunidades ribeirinhas da Amazônia. 
O projeto digitaliza e organiza dados coletados em campo, facilitando a análise e o manejo para a conservação de quelônios.

✨ Funcionalidades Principais
 * Registrar Ninho: Adiciona um novo ninho à base de dados.
 * Listar Registros: Exibe todos os ninhos monitorados em uma tabela.
 * Calcular Média de Ovos: Calcula a média de ovos para ninhos com risco "Estável" (🟢).
 * Identificar Ninhos para Eclosão: Lista ninhos que eclodirão em 5 dias ou menos.
 * Apontar Região de Maior Risco: Mostra a região com mais ninhos em risco "Crítico" (🔴).
 * Contar Ninhos em Duplo Risco: Informa a quantidade de ninhos "Danificados" e com "Predadores".

📁 Estrutura de Dados
Os dados são armazenados em uma lista de dicionários. Cada ninho é um dicionário com as seguintes chaves:
| Chave | Tipo | Descrição |
|---|---|---|
| Região | str | Localidade do ninho. |
| Quantidade de ovos | int | Número de ovos no ninho. |
| Status | str | Condição: "Intacto", "Ameaçado", "Danificado". |
| Risco | str | Classificação: 🟢, 🟡, 🔴. |
| Dias para eclosão | int | Estimativa de dias para eclosão. |
| Predadores | bool | Presença (True) ou ausência (False) de predadores. |
