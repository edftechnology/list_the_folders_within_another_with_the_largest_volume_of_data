#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar/usar o `listar as pastas dentro de outra com o maior volume de dados` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar o `listar as pastas dentro de outra com o maior volume de dados` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _This document contains the main commands and settings for configuring/installing/using the `list the folders within another with the largest volume of data` on `Linux Ubuntu`._

# ## Descrição [2]
# 
# ### `Pasta`
# 
# Uma pasta, no contexto de sistemas operacionais e gerenciamento de arquivos, é uma estrutura de armazenamento que organiza e agrupa arquivos e outras pastas. Também conhecida como diretório, a pasta facilita a organização e a localização de arquivos, permitindo que os usuários criem uma hierarquia de dados. As pastas podem conter documentos, imagens, programas e outros tipos de arquivos, e podem ser estruturadas de forma a refletir a organização desejada pelo usuário, tornando a navegação e o gerenciamento de arquivos mais eficiente.
# 

# ## 1. Como configurar/instalar/usar o `listar as pastas dentro de outra com o maior volume de dados` no `Linux Ubuntu` [1][3]
# 
# Para configurar/instalar/usar o `listar as pastas dentro de outra com o maior volume de dados` no `Linux Ubuntu`, você pode seguir estes passos:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
#     

# Para listar as pastas dentro de, por exemplo, `home` com maior volume de dados no `Linux Ubuntu`, você pode usar o comando du (`disk usage`) em conjunto com outros comandos como `sort` e `head` para ordenar e exibir as pastas com maior volume de dados. Aqui está o comando que você pode usar no `Terminal Emulator`: `du -sh /home/* | sort -rh | head -n 10`
# 
# Vamos explicar o que cada parte do comando faz:
# 
# 1. **`du -sh /home/*`**: Calcula o uso de disco para cada diretório dentro de `/home`, exibindo o resultado em um formato legível (`-h` para `human-readable`) e resumido (`-s` para `summary`).
# 
# 2. **`sort -rh`**: Ordena o resultado em ordem decrescente (`-r` para reverse) com base no tamanho, interpretando os tamanhos de forma legível por humanos (`-h`).
# 
# 3. **`head -n 10`**: Exibe as 10 primeiras linhas do resultado, que correspondem às 10 pastas com maior volume de dados.
# 
# Executando esse comando no seu `Terminal Emulator`, você obterá uma lista das pastas dentro de `/home` com maior volume de dados, ordenadas de forma decrescente.
# 

# ### 1.1 Código completo para configurar/instalar/usar
# 
# Para configurar/instalar/usar o `listar as pastas dentro de outra com o maior volume de dados` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     NÃO há.
#     ```
# 

# ## Referências
# 
# [1] OPENAI. ***Listar pastas maiores linux.*** Disponível em: <https://chatgpt.com/c/eb532506-f911-4eb4-a483-6e060cd00863> (texto adaptado). Acessado em: 25/07/2024 13:33.
# 
# [2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). Acessado em: 25/07/2024 13:33.
# 
