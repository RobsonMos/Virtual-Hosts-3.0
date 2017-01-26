# Virtual Hosts 3.0
##Apache(Linux)

Desenvolvido e inspirado no modulo VirtualHost-0.0.2, modificado por RobsonMos

Algumas das linhas presentes aqui foram retirados do modulo [VirtualHost 0.0.2](https://pypi.python.org/pypi/VirtualHost/) e modificado para atenter minhas nessecidades

assim como me foi util poderia ser para outros usuarios 

então qui esta minha obra.


Modo de uso
------------
É exigido dois parametros para criar um novo Host Virtual (-p/==path | -d/--domain)

A opção "-p/--path" são opcionais, e por deful em "/var/www/html" diretorio pardrão do servidor Apache

Opção "-d/--domain" coresponde a url do novo Host Virtual a ser criado

Ex: 
---
VirtualHosts.py -d/--domain facebook.local 

Caso queira que seu Virtual Host com diretorio root apontado para um outro diretorio

VirtualHosts.py -d facebook.local -p/--path /home/user/site


Creditos
---------

[Porimol](https://github.com/porimol/vhost)