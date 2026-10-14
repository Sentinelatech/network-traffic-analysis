# network-traffic-analysis

Análise do tráfego de rede gerado ao abrir um site, da digitação da URL até a página carregada. O projeto documenta, com captura real, o que acontece em cada camada: resolução de nome (DNS), estabelecimento de conexão (TCP), negociação de canal seguro (TLS) e a primeira troca HTTP.

> Projeto 1 de 7 do laboratório [sentinelatech](https://github.com/sentinelatech). Área: **redes**.

## Por que isso importa em segurança

Ler tráfego é a base de quase tudo em defesa: entender um alerta de rede, investigar uma conexão suspeita, reconhecer um certificado inválido ou um domínio estranho. Quem não lê um pacote não interpreta um IDS.

## Objetivo

Entregar um relatório técnico que explique, apoiado numa captura própria, o caminho completo de uma requisição web e onde cada etapa pode falhar em segurança.

## Estrutura

```
docs/especificacao.md   escopo e critério de aceite
docs/conceitos.md       a teoria por trás de cada camada
relatorio/              o relatório final, com diagramas e trechos da captura
capturas/               o arquivo .pcapng (sem dados sensíveis)
```

## Como reproduzir

1. Instale o Wireshark.
2. Inicie a captura na sua interface de rede.
3. Abra um site simples em uma aba nova.
4. Pare a captura e filtre por `dns`, depois pela conexão TCP do site.
5. Siga o roteiro em `docs/especificacao.md`.

## Ferramentas

Wireshark · `dig`/`nslookup` · navegador · terminal.

## Resultado

<!-- Preencher ao fim: ex. "Relatório de 6 páginas cobrindo DNS, handshake TCP, TLS 1.3 e a primeira resposta HTTP, com os pontos de atenção de segurança de cada etapa." -->

## Aviso

A captura foi feita na própria rede, para fins de estudo. O `.pcapng` publicado foi revisado para não conter credenciais, cookies de sessão ou dados pessoais.
