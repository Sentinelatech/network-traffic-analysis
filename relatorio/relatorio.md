# Relatório — Análise de tráfego de uma requisição web

> Modelo a preencher. Substitua cada `[...]` pelo que você observou na sua captura. Apague esta linha ao finalizar.

| | |
|---|---|
| **Autor** | [seu nome] |
| **Data** | [data] |
| **Ambiente** | [SO, navegador, rede usada] |
| **Captura** | [`capturas/arquivo.pcapng`] · [nº de pacotes] |
| **Site analisado** | [domínio] |

## Resumo

Em um parágrafo: o que foi feito e o principal achado. (Escreva por último.)

## Metodologia

Como a captura foi feita: ferramenta, interface de rede, como o tráfego foi isolado (filtros) e como os dados sensíveis foram removidos antes de publicar.

## 1. Resolução de nome (DNS)

- **O que apareceu:** consulta no pacote nº [x], resposta no nº [y]; tipo de registro [A/AAAA]; servidor [ip]; tempo [ms].
- **Evidência:** [print do Wireshark ou trecho da saída do `resumo_captura.py`].
- **Ponto de atenção de segurança:** [ex.: DNS em claro expõe os domínios visitados a quem está na rede].

## 2. Conexão (TCP)

- **Handshake:** SYN (nº [x]) → SYN,ACK (nº [y]) → ACK (nº [z]); porta de destino [443].
- **Evidência:** [print].
- **Ponto de atenção de segurança:** [ex.: portas abertas são superfície de ataque].

## 3. Canal seguro (TLS)

- **Negociação:** Client Hello (nº [x]), Server Hello (nº [y]); versão [TLS 1.3]; cifra [...].
- **Certificado:** emissor [...], validade [...], domínio confere? [sim/não].
- **Evidência:** [print].
- **Ponto de atenção de segurança:** [ex.: certificado inválido indica erro de configuração ou interceptação; SNI em claro].

## 4. Primeira troca HTTP

- **O que apareceu:** [sob TLS, conteúdo cifrado; descreva o padrão dos pacotes].
- **Evidência:** [print].
- **Ponto de atenção de segurança:** [ex.: HTTP sem TLS exporia todo o conteúdo].

## Diagrama

[Insira o diagrama de sequência DNS → TCP → TLS → HTTP. Pode ser feito em texto, no Excalidraw ou com Mermaid.]

## Conclusão

O que esse caminho ensina sobre onde a segurança entra em cada camada, e o que você observaria de diferente num tráfego suspeito.

## Anexos

- `capturas/arquivo.pcapng` — captura sanitizada
- Saída do `scripts/resumo_captura.py`
