# Predictive
Predict remedy demand based on aggregate data & MS data
Inteligência Artificial - Departamento de Assistência Farmacêutica do Ministério da Saúde

Lib pro DataApp para a visualização e interação dos usuários do DAF com o MicroServiço gerado: streamlit (instalado via pip)

Principais Libs utilizadas:    
    *Algoritmos de Shallow Learning: SKLearn    
    *Algoritmos de Deep Learning: Keras + Tensorflow
    *PlotLib: Plotly
    *Report: [PandasProfilling](pip install https://github.com/pandas-profiling/pandas-p
rofiling/archive/master.zip)

1º Teste:
- Todos municípios de __uma UF__ (a que tiver mais municípios com dados no Dataset)
- __Um medicamento__ (o que representar maior valor absoluto em R$)
- Dados extraídos via SQL após carga de massa de dados via __[DataSource](https://gitlab.com/gaesi/datasource)__

Refatoração do Dataset:

1. Remover float com numero quebrado
  ```
    $ cd farmpop/datasets
    $ sed 's/\,/./g' processed-extrator-2018-2.csv > process.csv && sed 's/\;\./;0./g' process.csv > process2.csv && rm -rf process.csv
  ```

Ativando o VENV (faça isso toda vez que for executar o projeto):
```shell script
    $ source venv/bin/activate
```

## Running backend server (Flask)

```$ flask run --host=0.0.0.0```

```$ FLASK_ENV=development flask run -h 0.0.0.0```


*Download it Datasets from GOOGLE DRIVE (add it to: automated-programming/datasets)

# Preparação do Ambiente
1. Instalar o python3 via gerenciador de pacote do Sistema Operacional

    ```shell script
      # MacOS X
      $ brew install python3

      # Linux
      $ apt-get install python3

      # Windows 10 (GitBash)
      $ /c/Users/ilton/AppData/Local/Programs/Python/Python38/python.exe -m pip install --upgrade pip
    ```

1. Remover o elo (link) do python2 para tornar o python3 como default

    ```shell script
      # MacOS X
      $ nano ~/.bash_profile
      $ nano ~/.zprofile

      # Ubuntu
      $ nano ~/.bashrc
    ```

    ``` $ sudo nano ~/.zprofile ```

    ```sudo nano ~/.zprofile
      # bash_profile AND .zshrc

      # aliases
      alias pip=pip3
      alias python=python3
    ```

   // if dont want to use zsh, add it to bash_profile: ``` [[ -s "$HOME/.profile" ]] && source "$HOME/.profile" # Load the default .profile ```

1. Configuração do Virtual Env (VENV)

    1. Criação do VENV
        ```shell script
           # Vem instalado com o PIP, não precisa instalar o VirtualEnv
           $ virtualenv -p python3 venv
        ```

    1.  Ativando o VENV (faça isso toda vez que for executar o projeto)
        ```shell script
            # MacOS
            $ source venv/bin/activate

            # Windows (Gitbash)
            $ /c/Projects/gaesi/msdaf/predictive/venv/Scripts/activate.bat
            # Windows (Prompt)
            > cd C:\Projects\gaesi\msdaf\predictive
            > venv\Scripts\activate.bat
        ```

1. Instalando as dependências com as versões unificadas

    ```shell script
        # MAC
        $ pip install -r requirements_mac.txt
        # WINDOWS
        $ pip install -r requirements_win.txt
    ```

1. CASO ocorra erro no pandas profilling:

    ```shell script
        $ pip install https://github.com/pandas-profiling/pandas-profiling/archive/master.zip
    ```

1. Criando o Kernel para o jupyter para que ele "visualize" as dependências instaladas

    ```shell script
        $ ipython kernel install --user --name=ms_daf
    ```

1. Selecionando o Kernel no Jupyter

    ![Jupyter Kernel Selection img](https://github.com/TonGarcia/pbe-r/raw/master/jupyter_kernel_selection.png)

1. __SE NÃO INSTALAR CORRETAMENTE SIGA OS PRÓXIMOS PASSOS__

1. Instalar o jupyter (execute esses comandos com o VENV ativo)

    ```shell script
      # Todos Sistemas Operacionais
      $ pip install jupyter notebook
      $ pip freeze > requirements.txt

      # MAC
      $ pip freeze > requirements_mac.txt
      # WINDOWS
      $ pip freeze > requirements_win.txt
    ```

1. Instalando a dependencia da computação em núvem (floydhub):

    ```shell script
      # Todos Sistemas Operacionais
      $ pip install -U floyd-cli
    ```

1. Instalar o gerenciador de extensões do jupyter

    ```shell script
        $ pip install jupyter_contrib_nbextensions
    ```

__OBSERVAÇÃO: Não atualize (upgrade) o pip! O tensorflow 1.9 é compatível com o pip instalado neste processo!__ Caso faça o Upgrade, execute o comando a seguir, com o env ativo:

```shell script
 $ sudo pip install --force-reinstall pip==10.0.1
```

__Se aparecer stacktrace no import do tensorflow no arg async significa que existem 2 pythons interpreters rodando o tensorflow e você deve executar um uninstall do tensorflow fora do env conda__:

```shell script
 $ deactivate
 $ pip uninstall tensorflow
```


# HOSTS

edit /etc/hosts

```hosts
##
# Host Database
#
# localhost is used to configure the loopback interface
# when the system is booting.  Do not change this entry.
##
127.0.0.1       localhost
255.255.255.255 broadcasthost
::1             localhost
# Added by Docker Desktop
# To allow the same kube context to work on the host and the container:
127.0.0.1 kubernetes.docker.internal
# End of section

127.0.0.1  docker discovery cassandra rabbit gateway documents ui oracle jupyter
127.0.0.1  modulos redis identidades elk onlyoffice elasticsearch dashboard kibana
127.0.0.1  integracoes-gateway integracoes-documents integracoes-ui sinprocesso
127.0.0.1  integracoes-modulos integracoes-identidades
127.0.0.1  integracoes-configserver integracoes-discovery
```


# PyCharm
Settings > Project Structure > Exclude Folders: data & microsets

# GENERATING MODELS
Run it notebook: http://localhost:8888/notebooks/automated-programming/CEAF/CEAF_AIRunner_FactoryModels.ipynb
