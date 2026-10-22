# Especificação — network-traffic-analysis

**Semana:** 23/10 a 29/10/2026
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

A issue de cada dia detalha a tarefa. O tamanho é uma estimativa; o que vale é o prazo da semana. O ritmo é de **2h por dia**, de segunda a sexta. Sábado e domingo ficam fora do projeto: são a folga e a margem para recuperar um dia que não rendeu.

| Dia | Fase | Entrega do dia |
|---|---|---|
| Sex 23/10 | Ambiente e captura | `.pcapng` da abertura de um site, salvo em `capturas/` |
| Seg 26/10 | DNS e TCP | Seção única: a resolução do nome e o handshake, com os pacotes citados |
| Ter 27/10 | TLS e HTTP | Seção única: onde o conteúdo deixa de ser legível |
| Qua 28/10 | Diagrama e pontos de segurança | Diagrama de sequência + o risco de cada camada |
| Qui 29/10 | Fechamento | Relatório final, README e captura revisada |
