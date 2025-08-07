# Como configurar/instalar/usar o `listar as pastas dentro de outra com o maior volume de dados` no `Linux Ubuntu`

## Resumo

Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar o `listar as pastas dentro de outra com o maior volume de dados` no `Linux Ubuntu`.

## _Abstract_

_This document contains the main commands and settings for configuring/installing/using the `list the folders within another with the largest volume of data` on `Linux Ubuntu`._

## Descrição [2]

### `Pasta`

Uma pasta, no contexto de sistemas operacionais e gerenciamento de arquivos, é uma estrutura de armazenamento que organiza e agrupa arquivos e outras pastas. Também conhecida como diretório, a pasta facilita a organização e a localização de arquivos, permitindo que os usuários criem uma hierarquia de dados. As pastas podem conter documentos, imagens, programas e outros tipos de arquivos, e podem ser estruturadas de forma a refletir a organização desejada pelo usuário, tornando a navegação e o gerenciamento de arquivos mais eficiente.


## 1. Como configurar/instalar/usar o `listar as pastas dentro de outra com o maior volume de dados` no `Linux Ubuntu` [1][3]

Para configurar/instalar/usar o `listar as pastas dentro de outra com o maior volume de dados` no `Linux Ubuntu`, você pode seguir estes passos:

1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`

2. Certifique-se de que seu sistema esteja limpo e atualizado.

    2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando:
    
    ```bash
    sudo apt clean
    ``` 
    
    2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando:
    
    ```bash
    sudo apt autoclean
    ```

    2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando:
    
    ```bash
    sudo apt autoremove -y
    ```

    2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: 
    
    ```bash
    sudo apt update
    ```

    2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes:
    
    ```bash
    sudo apt --fix-broken install
    ```

    2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando:
    
    ```bash
    sudo apt clean
    ``` 
    
    2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  
    
    ```bash
    sudo apt list --upgradable
    ```

    2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`:
    
    ```bash
    sudo apt full-upgrade -y
    ```

3. Para listar as pastas dentro de, por exemplo, `home` com maior volume de dados no `Linux Ubuntu`, você pode usar o comando du (`disk usage`) em conjunto com outros comandos como `sort` e `head` para ordenar e exibir as pastas com maior volume de dados. Aqui está o comando que você pode usar no `Terminal Emulator`: `sudo du -sh /home/* | sort -rh | head -n 10`

    3.1 Para listar as pastas dentro de, por exemplo, `/` com maior volume de dados no `Linux Ubuntu`, você pode usar o comando du (`disk usage`) em conjunto com outros comandos como `sort` e `head` para ordenar e exibir as pastas com maior volume de dados. Aqui está o comando que você pode usar no `Terminal Emulator`: `sudo du -sh /* | sort -rh | head -n 10`


Vamos explicar o que cada parte do comando faz:

1. **`du -sh /home/*`**: Calcula o uso de disco para cada diretório dentro de `/home`, exibindo o resultado em um formato legível (`-h` para `human-readable`) e resumido (`-s` para `summary`).

2. **`sort -rh`**: Ordena o resultado em ordem decrescente (`-r` para reverse) com base no tamanho, interpretando os tamanhos de forma legível por humanos (`-h`).

3. **`head -n 10`**: Exibe as 10 primeiras linhas do resultado, que correspondem às 10 pastas com maior volume de dados.

Executando esse comando no seu `Terminal Emulator`, você obterá uma lista das pastas dentro de `/home` com maior volume de dados, ordenadas de forma decrescente.


### 1.1 Código completo para configurar/instalar/usar

Para configurar/instalar/usar o `listar as pastas dentro de outra com o maior volume de dados` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:

1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`

2. Digite o seguinte comando e pressione `Enter`:

    ```
    NÃO há.
    ```


No `Linux Ubuntu`, há várias pastas que podem acumular arquivos desnecessários ao longo do tempo e que podem ser limpas com segurança. No entanto, é importante ter cuidado para não excluir arquivos importantes para o funcionamento do sistema ou dos aplicativos. Aqui estão algumas pastas que é conveniente limpar regularmente:

1. **`/tmp`**: Descrição: A pasta `/tmp` é usada para armazenar arquivos temporários que são criados e usados por programas em execução. O sistema limpa essa pasta periodicamente, mas você pode limpá-la manualmente. Como limpar:

    ```bash
    sudo rm -rf /tmp/*
    ```

2. **`/var/tmp`**: Descrição: Similar à `/tmp`, mas os arquivos aqui são mantidos por um período mais longo antes de serem excluídos automaticamente. Como limpar:
    
    ```bash
    sudo rm -rf /var/tmp/*
    ```

3. **`/var/cache/apt/archives`**: Descrição: Essa pasta armazena os pacotes `.deb` baixados durante as atualizações e instalações de _software_ usando o `apt`. Os arquivos aqui podem ser removidos após a instalação. Como limpar:

    ```bash
    sudo apt-get clean
    ```

4. **`/var/log`**: Descrição: Essa pasta contém arquivos de _log_ do sistema. Alguns _logs_ podem crescer muito com o tempo, ocupando espaço em disco. Como limpar:

    4.1 **Para remover _logs_ antigos**:
    
    ```bash
    sudo journalctl --vacuum-time=2weeks
    ```

    4.2 **Para limpar todos os _logs_ (use com cuidado)**:
    
    ```bash
    sudo rm -rf /var/log/*
    ```

5. **_Cache_ de navegadores**: Descrição: Navegadores como `Firefox` e `Chrome` armazenam caches locais para acelerar o carregamento de páginas. Esses _caches_ podem crescer bastante. Como limpar:

    5.1 **No `Firefox`**: Vá para `Configurações > Privacidade & Segurança > Cookies e dados do site > Limpar dados`.

    5.2 **No `Chrome`**: Vá para `Configurações > Privacidade e segurança > Limpar dados de navegação.`

6. **Arquivos de _cache_ no diretório do usuário**: Descrição: Muitos aplicativos criam caches no diretório do usuário, geralmente em `~/.cache`. Esses arquivos podem ser excluídos com segurança, mas alguns aplicativos podem precisar recriar o _cache_ posteriormente. Como limpar:

    ```bash
    sudo rm -rf ~/.cache/*
    ```

7. **`/var/crash`**: Descrição: Contém relatórios de falhas de aplicativos. Se nenhum programa estiver travando, você pode limpá-lo. Como limpar:

    ```bash
    sudo rm -rf /var/crash/*
    ```

8. **Arquivos órfãos**: Descrição: Pacotes instalados como dependências que **NÃO** são mais necessários. Como limpar:

    ```bash
    sudo apt-get autoremove
    ```

9. **`~/.local/share/Trash`**: Descrição: Diretório que armazena os arquivos enviados para a lixeira pelo ambiente gráfico (como `Nautilus`, `Thunar`, `Dolphin` etc.). Ele é composto por duas subpastas principais: `files/`, onde ficam os arquivos excluídos, e `info/`, que contém metadados como o caminho original e a data de exclusão. A lixeira pode ocupar bastante espaço se **NÃO** for esvaziada regularmente, principalmente após exclusão de arquivos grandes. Como limpar:

    ```bash
    rm -rf ~/.local/share/Trash/files/*
    rm -rf ~/.local/share/Trash/info/*
    ```

    - **Vantagens**:

        - Mantém a estrutura de pastas esperada pelo sistema (`files/` e `info/`)

        - Evita erros ou _bugs_ em alguns gerenciadores de arquivos que esperam essas subpastas existirem

10. Verifique se você tem o `timeshift` instalado e se este possui imagens de _backups_  que podem ser excluídas para liberar mais espaço no seu computador.

**Dica Adicional**

**`BleachBit`**: Uma ferramenta gráfica que ajuda a limpar o sistema, removendo _caches_, _logs_, e arquivos temporários de maneira segura.

Lembre-se de fazer _backup_ ou revisar o conteúdo antes de deletar qualquer coisa, especialmente em pastas que você não tem certeza sobre o propósito.

## Como usar o `clean_system.py`

O arquivo `docs/clean_system.py` automatiza tarefas de limpeza do sistema, removendo caches e arquivos temporários.
Execute o script com Python:

```bash
python docs/clean_system.py
```

Algumas etapas exigem privilégios de `sudo`, portanto você pode ser solicitado a informar a senha de administrador.

## Referências

[1] OPENAI. ***Listar pastas maiores linux.*** Disponível em: <https://chatgpt.com/c/eb532506-f911-4eb4-a483-6e060cd00863> (texto adaptado). Acessado em: 25/07/2024 13:33.

[2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). Acessado em: 25/07/2024 13:33.

