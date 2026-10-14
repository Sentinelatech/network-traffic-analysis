#!/usr/bin/env python3
"""
resumo_captura.py — resume uma captura de rede (.pcap/.pcapng) nas quatro
camadas do projeto: DNS, TCP, TLS e HTTP.

Uso:
    python resumo_captura.py <arquivo.pcapng>
    python resumo_captura.py <arquivo.pcapng> --host exemplo.com

Depende de scapy (veja requirements.txt). Faz apenas LEITURA do arquivo:
não envia nada à rede. Pensado para a sua própria captura de laboratório.

A saída é um resumo em texto que serve de base factual para o relatório.
Nenhum conteúdo de pacote é impresso — só metadados (nomes, IPs, portas,
contagens), para não vazar dado sensível ao colar no relatório.
"""
import argparse
import sys
from collections import Counter

try:
    from scapy.all import rdpcap, DNS, DNSQR, IP, IPv6, TCP
    from scapy.layers.tls.record import TLS  # requer cryptography instalado
    HAS_TLS = True
except ImportError as e:
    if "tls" in str(e).lower():
        from scapy.all import rdpcap, DNS, DNSQR, IP, IPv6, TCP
        HAS_TLS = False
    else:
        print("Instale as dependências: pip install -r scripts/requirements.txt")
        sys.exit(1)


def resolver_ip(pkt):
    if IP in pkt:
        return pkt[IP].src, pkt[IP].dst
    if IPv6 in pkt:
        return pkt[IPv6].src, pkt[IPv6].dst
    return None, None


def main():
    ap = argparse.ArgumentParser(description="Resume uma captura nas camadas DNS/TCP/TLS/HTTP.")
    ap.add_argument("arquivo", help="caminho do .pcap ou .pcapng")
    ap.add_argument("--host", help="filtra por um domínio de interesse (opcional)")
    args = ap.parse_args()

    try:
        pkts = rdpcap(args.arquivo)
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {args.arquivo}")
        sys.exit(1)

    total = len(pkts)
    dns_consultas = Counter()
    syn = syn_ack = ack_handshake = 0
    portas_dst = Counter()
    tls_registros = 0

    for pkt in pkts:
        # DNS: consultas (qr == 0)
        if pkt.haslayer(DNS) and pkt[DNS].qr == 0 and pkt.haslayer(DNSQR):
            nome = pkt[DNSQR].qname.decode(errors="ignore").rstrip(".")
            if not args.host or args.host in nome:
                dns_consultas[nome] += 1

        # TCP: flags do handshake e portas de destino
        if pkt.haslayer(TCP):
            flags = pkt[TCP].flags
            portas_dst[int(pkt[TCP].dport)] += 1
            if flags == "S":
                syn += 1
            elif flags == "SA":
                syn_ack += 1
            elif flags == "A" and pkt[TCP].seq and not pkt[TCP].payload:
                ack_handshake += 1

        # TLS: registros (quando o suporte está disponível)
        if HAS_TLS and pkt.haslayer(TLS):
            tls_registros += 1

    print("=" * 56)
    print(f"Resumo da captura: {args.arquivo}")
    print(f"Total de pacotes: {total}")
    print("=" * 56)

    print("\n[DNS] consultas observadas")
    if dns_consultas:
        for nome, n in dns_consultas.most_common(15):
            print(f"  {n:>3}x  {nome}")
    else:
        print("  nenhuma consulta DNS (ou filtrada pelo --host)")

    print("\n[TCP] handshake de três vias")
    print(f"  SYN:     {syn}")
    print(f"  SYN,ACK: {syn_ack}")
    print(f"  ACK:     {ack_handshake}")
    print("  portas de destino mais vistas:")
    for porta, n in portas_dst.most_common(6):
        rotulo = {443: " (HTTPS)", 80: " (HTTP)", 53: " (DNS)"}.get(porta, "")
        print(f"    {n:>4}x  porta {porta}{rotulo}")

    print("\n[TLS] registros")
    if HAS_TLS:
        print(f"  registros TLS: {tls_registros}")
    else:
        print("  suporte a TLS do scapy indisponível (instale 'cryptography').")
        print("  dica: no Wireshark, filtre por 'tls.handshake' para ver o Client/Server Hello.")

    print("\nUse estes números no relatório, sempre citando o nº do pacote no Wireshark.")


if __name__ == "__main__":
    main()
