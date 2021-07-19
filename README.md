# Bank System
## DIM0517 - GERÊNCIA DE CONFIGURAÇÃO E MUDANÇAS - T01 (2021.1 - 24T12)

Projeto para desenvolver um sistema bancário utilizando de qualquer framework desejado pelo grupo

## Como rodar localmente?
- Primeiramente será necessario instalar o [POSTGRESQL](https://www.youtube.com/watch?v=e1MwsT5FJRQ)
- Faça o clone do seu repositório e após isso vá em: *BANK SYSTEM* -> `settings.py`
- No arquivo `settings.py` realize a seguinte alteração:\
Desfaça o comentário para o número 1 e deixe a segunda parte comentada. (Inverter os comentários)\
Atenção!! Coloque os dados do Banco que você criou no seu banco de dados local no POSTGRES!!\
![image](https://user-images.githubusercontent.com/39765254/126182292-19ee1bd9-87e4-4cc2-aecd-0557449d119b.png)
- Crie um ambiente virtual, no *Windows*: `python -m venv <nome do seu repositorio virtual>`
- Ative seu ambiente virtual em: `cd <nome do seu repositorio virtual>/Scripts/activate.bat`
- Adicione o `<nome do seu repositório virtual>` no arquivo .gitignore
- Na raiz do repositório, onde está localizado o arquivo `requirements.txt`, faça: `pip install -r requirements.txt`
- Após isso ainda na raiz do repositório rode o comando: `python manage.py runserver` e vualá!\

### Dúvidas
[![telegram-removebg-preview](https://user-images.githubusercontent.com/39765254/126184041-1af08087-923d-46a4-9f95-6a2a700683f4.png)](https://t.me/wesleygurgel)



___
## Technologies used

### Database
![PostgreSQL Logo in a shields.io badge](https://img.shields.io/badge/PostgreSQL-gray.svg?logo=postgresql&style=for-the-badge&color=4169E1&logoColor=white)

### Deployed
[![Heroky Logo in a shields.io badge](https://img.shields.io/badge/Heroku-gray.svg?logo=heroku&style=for-the-badge&color=430098&logoColor=white)](https://bank-system-whr.herokuapp.com/)

___
## Componentes
- Wesley Gurgel
- Hilton Kevin
- Raul Souto
