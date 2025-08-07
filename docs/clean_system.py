# -*- coding: utf-8 -*-
"""
Script para limpeza de arquivos temporários e caches no Ubuntu.

Atenção: algumas ações requerem privilégios de superusuário (sudo).
"""

import subprocess

def run_command(command):
    # Executa um comando no shell com mensagens visíveis
    print(f"\n[INFO] Running: {command}")
    subprocess.run(command, shell=True, check=False)

def clean_system():
    print("🧹 Starting system cleanup...")

    # Limpa as pastas temporárias
    run_command("sudo rm -vrf /tmp/*")
    run_command("sudo rm -vrf /var/tmp/*")

    # Limpa o cache de pacotes .deb do apt
    run_command("sudo apt-get clean -y")

    # Remove logs antigos e limpa a pasta de logs
    run_command("sudo journalctl --vacuum-time=2weeks")
    run_command("sudo rm -vrf /var/log/*")

    # Remove o cache de aplicativos do usuário
    run_command("sudo rm -vrf ~/.cache/*")

    # Remove relatórios de falhas do sistema
    run_command("sudo rm -vrf /var/crash/*")

    # Remove pacotes órfãos
    run_command("sudo apt-get autoremove -y")

    # Limpa a lixeira sem apagar sua estrutura
    run_command("rm -vrf ~/.local/share/Trash/files/*")
    run_command("rm -vrf ~/.local/share/Trash/info/*")

    print("\n🔎 Check if you have Timeshift snapshots consuming disk space.")
    print("💡 Tip: You can also use BleachBit for advanced graphical cleaning.")
    print("✅ Cleanup finished!")

if __name__ == "__main__":
    clean_system()
