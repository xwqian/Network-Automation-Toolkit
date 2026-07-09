"""
Infrastructure Automation - Resource Manager
Author: Wendy Qian
Purpose: Provides a context manager for atomic environment setup and teardown.
Ensures zero-resource leakage in CI/CD pipelines even if tests fail.
"""

import logging
from contextlib import contextmanager

# config basic log information
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@contextmanager
def managed_test_resource(resource_name, setup_func, teardown_func):
    """
    A general context manager used to manage test resources.
    """
    logger.info(f"--- Setting up: {resource_name} ---")
    resource = setup_func()  # Initialize resource
    try:
        yield resource       # Transfer resource to the test case
    except Exception as e:
        logger.error(f"Test failed with error: {e}")
        raise                # ensure test case can capture the exception generated
    finally:
        logger.info(f"--- Cleaning up: {resource_name} ---")
        teardown_func(resource) # clean the resources no matter the test succeeds or fails

# --- use it for test ---

def test_cloud_network_integration():
    # Simulate cleaning logic for external cloud environment 
    def setup(): return {"id": "aws-sg-999", "status": "active"}
    def cleanup(res): logger.info(f"Deleting {res['id']} from cloud...")

    # use conextmanager
    with managed_test_resource("Cloud-Firewall-Rule", setup, cleanup) as res:
        logger.info(f"Running tests on {res['id']}...")
        assert res["status"] == "active"
