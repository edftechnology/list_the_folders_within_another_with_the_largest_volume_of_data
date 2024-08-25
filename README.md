# Como configurar/instalar/usar o `desabilitar as comfigurações do compositor` no `Linux Ubuntu`

## Resumo

Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar o `desabilitar as comfigurações do compositor` no `Linux Ubuntu`.

## _Abstract_

_This document contains the main commands and settings for configuring/installing/using the `disable composer settings` on `Linux Ubuntu`._

## Descrição [2]

### `compositor`

Um `compositor` é um componente de _software_ em sistemas operacionais que gerencia a composição e a exibição de gráficos na tela. Ele é responsável por combinar várias camadas de janelas e elementos gráficos em uma única imagem visual antes de enviá-la para o display. Isso permite efeitos visuais avançados, como transparência, sombras e animações suaves. No contexto de ambientes gráficos modernos, o `compositor` melhora a estética e a funcionalidade da interface do usuário, proporcionando uma experiência visual mais rica e fluida ao garantir que todas as janelas e efeitos sejam renderizados corretamente e de forma eficiente.


## 1. Como configurar/instalar/usar o `desabilitar as comfigurações do compositor` no `Linux Ubuntu` [1][3]

Para configurar/instalar/usar o `listar as pastas dentro de outra com o maior volume de dados` no `Linux Ubuntu`, você pode seguir estes passos:

1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`


2. Certifique-se de que seu sistema esteja limpo e atualizado.

    2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
    
    2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`

    2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`

    2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`

    2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`

    2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
    
    2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`

    2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
    

O problema que você deve estar enfrentando, onde arrastar uma janela cria várias imagens dela e faz a tela piscar, é geralmente relacionado a um problema com o _driver_ gráfico ou as configurações do `compositor` de janelas no ambiente gráfico. Aqui estão algumas possíveis soluções para resolver isso:

### 1.1 Verificar as configurações do `Compositor`

No `Linux Ubuntu`, que usa o ambiente gráfico `XFCE`, você pode tentar desativar ou ajustar o `compositor`:

1. Vá para `Configurações > Configurações do Gerenciador de Janelas`.

2. Na aba `Compositor`, você pode tentar desativar a opção `"Ativar o compositor de janelas"` para ver se isso resolve o problema.

Se desativar o `compositor` resolver o problema, mas você quiser continuar usando o `compositor`, pode tentar ajustar algumas configurações, como desmarcar `"Sombrear janelas inativas"` ou ajustar a `"Sombra da janela"`.

### 1.2 Atualizar ou reinstalar o _driver_ dráfico

O problema pode ser causado por um _driver_ gráfico mal configurado ou com defeito. Aqui estão os passos para atualizar ou reinstalar o _driver_ gráfico:

1. **Atualizar os _drivers_**: Abra um `Terminal Emulator` e execute:

    ```
    sudo apt update
    sudo apt full-upgrade -y
    ```

2. **Reinstalar o _driver_ gráfico**: Se você está usando o _driver_ `amdgpu`, pode reinstalá-lo:

    ```
    sudo apt remove --purge xserver-xorg-video-amdgpu -y
    sudo apt install xserver-xorg-video-amdgpu -y
    ```

3. **Se você está usando o _driver_ `radeon`**:

    ```
    sudo apt-get remove --purge xserver-xorg-video-radeon
    sudo apt-get install xserver-xorg-video-radeon
    ```


### Testar com um _driver_ diferente

Se você estava usando `amdgpu`, pode tentar mudar para o _driver_ radeon, ou vice-versa, para ver se o problema é resolvido.

1. **Instalar o _driver_ alternativo**:

    - **Para o `radeon`**: `sudo apt-get install xserver-xorg-video-radeon`

    - **Para o `amdgpu`**: `sudo apt-get install xserver-xorg-video-amdgpu`

### 1.3 Código completo para configurar/instalar/usar

Para configurar/instalar/usar o `listar as pastas dentro de outra com o maior volume de dados` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:

1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`

2. Digite o seguinte comando e pressione `Enter`:

    ```
    NÃO há.
    ```


## Referências

[1] OPENAI. ***Listar pastas maiores linux.*** Disponível em: <https://chatgpt.com/c/eb532506-f911-4eb4-a483-6e060cd00863> (texto adaptado). Acessado em: 25/07/2024 13:33.

[2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). Acessado em: 25/07/2024 13:33.

