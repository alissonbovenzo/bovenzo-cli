#!/Users/alissonbovenzo/Fontes/Astrahus/bovenzo-cli/.venv/bin/python3

import click
import os
from subprocess import Popen

@click.command('vport')
@click.option('--port', default=8181, help="Porta [ Por Padrão:8181 ]")
def verify_port(port):
    """Retorna a busca de processos sobre uma porta de rede específica"""
    click.echo(click.style('Lista de processos', fg='green'))
    click.echo(click.style('USER\tPID\t%CPU\t%MEM\tVSZ\tRSS\tTT\tSTAT STARTED\tTIME COMMAND', fg='green'))
    os.system(f"ps aux | grep {port}")

@click.command('sps')
@click.option('--port', default=8181, help="Porta [ Por Padrão:8181 ]")
def simple_server(port):
    """Executa um servidor HTTP Python 3 na pasta atual e abre o browser\n
    - Extremamente útil para validar pastas de arquivos de distribuição de front
    - Para encerrar, pressione CTRL + C e a cli matará o PID do servidor iniciado aqui
    """
    os.system('python3 --version')
    server_process = Popen(["python3", "-m", "http.server", str(port)])
    os.system(f"open http://localhost:{port}")
    click.echo(click.style(f'Para sair pressione CTRL + C\nPID: {server_process.pid}', fg='green'))
    server_process.wait()
    server_pid = server_process.pid
    os.system(f"kill {server_pid}")


@click.group(name="redes")
def redes():
    """Grupo de comandos de rede"""
    pass

@click.group(name="node")
def nodejs():
    """Grupo de comandos de NodeJS"""


@click.group(name="finder")
def nodejs():
    """Grupo de comandos de procura de arquivos e outros caminhos"""



@click.group(name="bovenzo")
def cli():
    """Linha de comando com comandos úteis normalmente usados pelo Bovenzo"""
    pass

redes.add_command(verify_port)
cli.add_command(simple_server)
cli.add_command(redes)

if __name__ == '__main__':
    cli()