# capturas/

Coloque aqui a captura sanitizada (`.pcapng`) usada no relatório.

**Antes de versionar:**

- Capture só o necessário (abra um site, pare a captura).
- Remova o que for sensível. No Wireshark, use *File → Export Specified Packets* para salvar apenas os pacotes do fluxo analisado.
- Não inclua tráfego de login, cookies de sessão, tokens ou dados pessoais.
- Confirme que a captura é da **sua** rede.

Arquivos `.pcap`/`.pcapng` brutos são ignorados pelo `.gitignore`. Para versionar a amostra final, nomeie-a como `amostra.pcapng` (liberada no `.gitignore`).
