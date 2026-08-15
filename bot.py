import json
import logging
import socket
import time

# This project is intentionally a real TCP client foundation.
# Terraria's protocol is binary and version-specific. A complete 1.4.5.6
# implementation requires maintaining all packet IDs, serialization rules,
# and handshake states from the client protocol.

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


def load_config():
    with open("config.json", "r", encoding="utf-8") as f:
        return json.load(f)


def connect_to_server(config):
    logging.info("Connecting to %s:%s", config["server_ip"], config["server_port"])
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(15)
    sock.connect((config["server_ip"], config["server_port"]))
    return sock


def main():
    config = load_config()
    sock = None
    try:
        sock = connect_to_server(config)
        logging.info("TCP connection established")

        # Placeholder until the full Terraria 1.4.5.6 client protocol layer is added.
        # Do not send fake ping data: servers require the proper handshake.
        time.sleep(30)

    except Exception as exc:
        logging.error("Bot failed: %s", exc)
        raise
    finally:
        if sock:
            sock.close()
            logging.info("Disconnected")


if __name__ == "__main__":
    main()
