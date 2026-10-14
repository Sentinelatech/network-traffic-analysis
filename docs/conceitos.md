# Conceitos — a teoria por trás de cada camada

Material de apoio do projeto. A ideia é entender o suficiente para interpretar a sua própria captura, não decorar.

## 1. DNS — resolver o nome

Antes de qualquer conexão, o navegador precisa trocar o nome (`exemplo.com`) por um endereço IP. Ele pergunta a um servidor DNS (consulta tipo **A** para IPv4, **AAAA** para IPv6) e recebe a resposta.

- **O que observar na captura:** a consulta, a resposta, o tempo entre as duas e qual servidor respondeu.
- **Ponto de segurança:** o DNS tradicional viaja **em claro**. Quem está na mesma rede vê todos os domínios que você visita. É o que DoH (DNS over HTTPS) e DoT (DNS over TLS) resolvem.

## 2. TCP — abrir a conexão

Com o IP em mãos, o navegador abre uma conexão TCP com a porta do servidor (443 para HTTPS). O começo é o **handshake de três vias**:

1. Cliente → servidor: **SYN**
2. Servidor → cliente: **SYN, ACK**
3. Cliente → servidor: **ACK**

- **O que observar:** os três pacotes, as portas de origem e destino, os números de sequência.
- **Ponto de segurança:** uma porta aberta é uma superfície de ataque. Varredura de portas (Nmap) é a primeira coisa que um atacante faz; é também o que você vai usar de forma defensiva no projeto 4.

## 3. TLS — tornar o canal seguro

Sobre o TCP, o TLS negocia a criptografia antes de qualquer dado sensível trafegar.

- **Client Hello:** o navegador propõe versões e cifras e diz qual site quer (campo SNI, que viaja em claro no TLS 1.2).
- **Server Hello + certificado:** o servidor escolhe a cifra e apresenta o certificado.
- **Validação:** o navegador confere se o certificado foi emitido por uma autoridade confiável, se é do domínio certo e se está no prazo.
- **Ponto de segurança:** certificado inválido, expirado ou de domínio errado é sinal de problema (erro de configuração ou interceptação). O SNI em claro ainda entrega qual site você acessa.

## 4. HTTP — a troca de verdade

Com o canal seguro, vem a requisição HTTP (GET da página) e a resposta. Sob TLS, **o conteúdo aparece cifrado** na captura: você vê os pacotes, mas não o texto.

- **O que observar:** o volume e o padrão dos pacotes, mesmo sem o conteúdo.
- **Ponto de segurança:** é por isso que análise de tráfego cifrado olha metadados (tamanho, tempo, destino), não o conteúdo. E é por isso que capturar HTTP **sem** TLS expõe tudo, inclusive senhas.

## A sequência completa

```
Digitar URL
   │
   ▼
DNS: qual o IP de exemplo.com?  ──►  resposta: 93.184.x.x
   │
   ▼
TCP: SYN ─► SYN,ACK ─► ACK      (conexão aberta na porta 443)
   │
   ▼
TLS: Client Hello ─► Server Hello + certificado ─► canal cifrado
   │
   ▼
HTTP: GET /  ─►  200 OK         (cifrado dentro do TLS)
   │
   ▼
Página carregada
```

## Fontes para aprofundar

- Professor Messer — Network+ e Security+ (vídeos gratuitos)
- RFC 1035 (DNS), RFC 9293 (TCP), RFC 8446 (TLS 1.3) — as fontes primárias
- Wireshark User's Guide — a documentação oficial da ferramenta
