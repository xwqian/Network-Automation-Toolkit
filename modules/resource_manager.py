import logging
from contextlib import contextmanager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@contextmanager
def managed_test_resource(resource_name, setup_func, teardown_func, *args, **kwargs):
    """
    Context manager to handle resource lifecycle.
    Ensures teardown_func is ALWAYS called upon exit, success or failure.
    """
    logger.info(f"--- Setting up: {resource_name} ---")
    try:
        resource = setup_func(*args, **kwargs)
        yield resource
    except Exception as e:
        logger.error(f"Test failed in {resource_name}: {e}")
        raise
    finally:
        logger.info(f"--- Cleaning up: {resource_name} ---")
        teardown_func(resource)
