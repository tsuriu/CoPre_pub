# Zabbix - Aula 1

## Introdução

### O que é Zabbix?

Zabbix é uma ferramenta capaz de monitorar diversos componentes na área de TI, incluindo redes e seus ativos, servidores, máquinas virtuais, serviços em nuvem, distribuída sobre a licença GPLv2. É composta essencialmente por três partes:
	
	* Banco de dados (MySQL/MariaDB, PostegreSQL, SQLServer, Oracle, IBM DB2)
	* WEB UI (Escrita em PHP)
	* Aplicação CORE (Escreita em C)

É possível utilizar diversos meios para monitorar os ativos e serviços, tais como:	

	* Agente [SNMP](https://pt.wikipedia.org/wiki/Simple_Network_Management_Protocol), é um protocolo padrão usado por diversos fabricantes de equitamentos e desenvolvedores de sistemas para permitir a coleta e organização de informações sobre os seus produtos. Além de permitir alteração de tais informações, podendo assim alterar o comportamento do ativo. 
	* [Agente Zabbix](https://www.zabbix.com/zabbix_agent), é uma aplicação também escrita em C que possibilita o monitoramento de sistemas que não possuem suporte aos outros protocolos utilizados pelo zabbix.



#### Caracteristicas
