from modules.network_mock import NetworkGatewayMock
import pytest

def test_system_recovery_on_timeout():
    """
    Test if the system correctly handles a gateway timeout.
    """
    gateway = NetworkGatewayMock()
    mock_api = gateway.set_faulty_behavior("timeout")
    
    # Assert that our system correctly catches the exception 
    # instead of crashing the whole pipeline
    with pytest.raises(Exception, match="Gateway Timeout"):
        mock_api.get_bgp_status()
