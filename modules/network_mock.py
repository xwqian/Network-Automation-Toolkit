"""
Network Behavior Mocking System
Allows injection of network faults for resilience testing.
"""
from unittest.mock import MagicMock

class NetworkGatewayMock:
    def __init__(self):
        self.mock_client = MagicMock()

    def set_faulty_behavior(self, fault_type="timeout"):
        """
        Dynamically inject faults into the gateway client.
        """
        if fault_type == "timeout":
            self.mock_client.get_bgp_status.side_effect = Exception("Gateway Timeout")
        elif fault_type == "flapping":
            self.mock_client.get_bgp_status.side_effect = [{"status": "UP"}, Exception("Down"), {"status": "UP"}]
        return self.mock_client
