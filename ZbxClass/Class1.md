# Zabbix - Aula 1

## Introdução

### O que é Zabbix?

Zabbix é uma ferramenta capaz de monitorar diversos componentes na área de TI, incluindo redes e seus ativos, servidores, máquinas virtuais, serviços em nuvem, distribuída sobre a licença GPLv2. É composta essencialmente por três partes:
	
	* Banco de dados (MySQL/MariaDB, PostegreSQL, SQLServer, Oracle, IBM DB2)
	* WEB UI (Escrita em PHP)
	* Aplicação CORE (Escreita em C)

É possível utilizar diversos meios para monitorar os ativos e serviços, tais como:	

	* Agente SNMP, é um protocolo padrão usado por diversos fabricantes de equitamentos e desenvolvedores de sistemas para permitir a coleta e organização de informações sobre os seus produtos. Além de permitir alteração de tais informações, podendo assim alterar o comportamento do ativo. 
	* Agente Zabbix, é uma aplicação também escrita em C que possibilita o monitoramento de sistemas que não possuem suporte aos outros protocolos utilizados pelo zabbix.

#### Caracteristicas

O Zabbix é uma ferramenta que proporciona um monitoramento com alta disponibilidade, além de ser capaz de monitorar um número realmente grande de dispotivos, serviços e operações, quando bem dimensionado.
É possível realizar a descoberta de hosts na rede, podendo assim automatizar e acelerar o processo de monitoramento em uma grande rede, assim como descobrir itens que não estavam disponíveis no momento do inicio do processo.
Uma coisa uma muito importante principalmente em uma rede muito grande, digamos com elementos em lugares geograficamente distantes. Por isso o Zabbix é capaz de agir decentralizadamente, porém mantendo a gerencia de um ponto para facilitar todo o processo de operação.

##### Alertas e Ações

Uma das partes mais importantes de um processo de monitoramento é a detecção de eventos e antecipação de potênciais problemas em uma rede. Nesse ponto o Zabbix entrega além de um interface altamente amigável e customizável para parametrizar os alertas de acordo com suas necessidades.
