# Comandos de Infraestrutura SSH

### 🚀 Atalhos configurados no .bashrc
- 'tunel': Abre o redirecionamento da porta 9999 -> porta 8888 em segundo plano.

### 🛑 Gerenciamento do Túnel
- 'pkill ssh': Fecha todas as conexões SSH e derruba o túnel;
- 'ps aux | grep ssh': Localiza o ID do processo do túnel se precisar matar apenas um.

### 🛡️ Segurança do Servidor (/etc/ssh/sshd_config)
- 'PermitRootLogin no': Bloqueia o acesso root direto;
- 'PasswordAuthentication no': Só permite entrar com minha chave RSA/ed25519.
