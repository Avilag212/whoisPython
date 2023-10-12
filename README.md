# whoisPython
Implementação do protocolo whois em Python, consulta ao IANA e em sequência ao NIR.
[WHOIS EM PYTHON]
Por: Gabriel de Avila Farias

[ATENÇÃO]:
O script apenas busca informações de registro dispostas na Internet que são 
de domínio público, o autor não se resposabilizaa de forma alguma pelo fim para o 
qual este código poderá ser utilizado.
Use com responsabilidade.


-- DESCRIÇÃO -------------------
O script (consulta.py) abre um socket com o IANA para perguntar quem é o NIR ou LIR responsável pelo domínio pesquisado,
desta maneira a responsta torna-se mais confiável, então é aberto outro scoket para consulta whois com o 
responsável pelo domíno registrado, o script retorna exatamente a resposta que foi retornada pelo servidor whois.

[!]Uma descrição detalhada de como o código funciona será
encontrada no código em formato de comentários ao longo do mesmo.

[ATENÇÃO]:
O script utiliza o protocolo whois como citado anteriormente, portanto como cada servidor segue
o próprio padrão para implementar o protocolo o formato das respostas pode variar.
Repostas do registro.br normalmente vem em um formato mais legível.

-- MODO DE USO -----------------
[!] O código foi desenvolvido em python, é necesário que instale o python antes de usar

Chame o script (python3 consulta.py no Linux ou Mac) ou (python script.py no Windows) e passe
como parâmetro o domínio do qual deseja obter informações.
EX: python3 consulta.py www.youtube.com.br (LINUX OU MAC)
EX: python consulta.py www.youtube.com.br (Windows)
