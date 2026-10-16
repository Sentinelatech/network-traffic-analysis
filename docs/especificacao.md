# Especificação — network-traffic-analysis

**Semana:** 17/10 a 23/10/2026
**Entrega final:** relatório em `relatorio/` + captura em `capturas/`

## Contexto

Você recebeu a tarefa de documentar, para quem está começando no time, o que realmente acontece na rede quando um usuário abre um site. O material precisa ser preciso e apoiado em evidência própria, não em teoria copiada.

## Escopo

O relatório deve cobrir, em ordem:

1. **Resolução de nome (DNS)** — a consulta e a resposta, o tipo de registro, o servidor consultado e o tempo.
2. **Conexão (TCP)** — o handshake de três vias (SYN, SYN-ACK, ACK) identificado na captura.
3. **Canal seguro (TLS)** — o início da negociação (Client Hello, Server Hello), a versão do TLS e a validação do certificado.
4. **Primeira troca HTTP** — a requisição e a resposta (ou a observação de que, sob TLS, o conteúdo aparece cifrado).

Para cada etapa: o que é, o que apareceu na sua captura (com o número do pacote) e **um ponto de atenção de segurança** (ex.: DNS sem criptografia expõe os domínios visitados).

## Critério de aceite

- [ ] Captura própria em `capturas/`, revisada para não conter dados sensíveis
- [ ] As quatro etapas explicadas com referência a pacotes reais da captura
- [ ] Ao menos um diagrama (a sequência da requisição)
- [ ] Um ponto de atenção de segurança por etapa
- [ ] README com o resultado preenchido em uma linha

## Fora de escopo

Interceptar tráfego de terceiros; capturar em rede que não seja a sua; qualquer tentativa de decifrar TLS alheio.

## Fases (issues da semana)

A issue de cada dia detalha a tarefa. O tamanho é uma estimativa; o que vale é o prazo da semana.

| Dia | Fase | Entrega do dia |
|---|---|---|
| Sáb 17/10 | Montar o ambiente e fazer a primeira captura (dia leve) | `.pcapng` salvo e aberto no Wireshark |
| Dom 18/10 | DNS (dia leve) | Seção de DNS do relatório |
| Seg 19/10 | TCP | Seção do handshake TCP |
| Ter 20/10 | TLS | Seção de TLS, em rascunho |
| Qua 21/10 | HTTP e diagrama | Seção HTTP e o diagrama de sequência |
| Qui 22/10 | Pontos de segurança e revisão | Relatório completo em rascunho |
| Sex 23/10 | Fechamento | Relatório final, README e limpeza da captura |
