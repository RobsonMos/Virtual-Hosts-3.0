#coding: utf:8
import os
import argparse
'''
Desenvolvido e inspirado no modulo VirtualHost-0.0.2, modificado por RobsonMos
Algumas das linhas presentes aqui foram retirados do modulo VirtualHosts e modificado para atender minhas nessecidades
assim como me foi útil poderia ser para outros usuários 
então qui esta minha obra.
'''
def main():
    parse = argparse.ArgumentParser(description="Programa auxilia na criação de Virtual Hosts do servidor apache2", epilog="Criado por RobsonMos, GitHub: https://github.com/RobsonMos?tab=repositories")

    parse.add_argument('-p', '--path', default='/var/www/html', help='Diretorio rais do dominio, default: /var/www//html')
    
    parse.add_argument('-d', '--domain', required=True, help='Nome Dominio a ser criado, ex: facebook.local')
    
    args = parse.parse_args()

    local_domain = args.path + "/" + args.domain
    local_hosts = "/etc/apache2/sites-enabled/" + args.domain + ".conf"

    if not os.path.exists(local_domain):
        os.makedirs(args.path + "/" + args.domain, 0755)
        os.system("sudo touch " + local_hosts)
        os.system("sudo touch " + local_domain + "/index.html")
        os.system("sudo chmod -R 777 " + local_hosts)
        with open(local_domain + "/index.html", "a+") as vindex:
            vindex.write("<!DOCTYPE html>\n")
            vindex.write("<html>\n")
            vindex.write("<head>\n")
            vindex.write("\t<title>Virtual Hosts</title>\n")
            vindex.write("</head>\n")
            vindex.write("<body>\n")
            vindex.write("<center>\n")
            vindex.write("\tYour domino is working.\n")
            vindex.write("</center>\n")
            vindex.write("</body>\n")
            vindex.write("</html>\n")
        with open(local_hosts, "a+") as vfile:
            vfile.write("<VirtualHost *:80>\n")
            vfile.write("\tServerAdmin email.example@com\n")
            vfile.write("\tServerName " + args.domain + "\n")
            vfile.write("\tServerAlias www." + args.domain + "\n")
            vfile.write("\tDocumentRoot " + local_domain + "\n")
            vfile.write("\tErrorLog ${APACHE_LOG_DIR}/error.log\n")
            vfile.write("</VirtualHost>")
        os.system("sudo chmod -R 777 /etc/hosts")

        with open("/etc/hosts", "a+") as f:
            f.write("\n127.0.0.1 \t " + args.domain + "\t" + "www." + args.domain)

        # os.system("sudo a2ensite "+ args.domain)
        os.system("sudo service apache2 restart")
        print "%s Vai ser criado em %s" % (
        args.domain, args.path) + "\n\r" + "Você podera acessar apartir de www." + args.domain
    else:
        print "Dominio %s já existentes" % (args.domain)
if __name__ == '__main__':
    main()