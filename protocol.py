"""
Terraria 1.4.5.6 protocol foundation.

This module contains helpers for building the real Terraria client protocol.
It intentionally does not send fake ping packets. Packet IDs and serialization
must match the exact server version before joining as a player.
"""

import struct
import logging

logging.basicConfig(level=logging.INFO)


class TerrariaPacket:
    """Base packet encoder used by the future client implementation."""

    @staticmethod
    def encode(packet_id: int, payload: bytes = b"") -> bytes:
        body = bytes([packet_id]) + payload
        return struct.pack("<H", len(body)) + body


class TerrariaClientProtocol:
    def __init__(self):
        self.connected = False

    def handle_packet(self, data: bytes):
        if not data:
            return
        packet_id = data[0]
        logging.info("Received Terraria packet id=%s", packet_id)

    def build_packet(self, packet_id: int, payload: bytes = b""):
        return TerrariaPacket.encode(packet_id, payload)
