# Network Automation Toolkit

A production-grade Python framework designed for **Atomic Resource Lifecycle Management** in automated testing.

## Why this framework?
In large-scale integration testing (especially for microservices and network components), resource leakage (dangling cloud resources, leaked connections) is a common cause of flaky pipelines. 
This toolkit provides a **Context-Manager based abstraction** that ensures:
1. **Atomicity**: Environment setup and teardown are treated as a single unit of work.
2. **Resilience**: Leveraging `try...finally` logic, it guarantees cleanup even when tests fail.
3. **Hierarchy**: Native support for **nested dependency management** (VPC -> K8s -> Pod).

## Usage Example
```python
from modules.resource_manager import managed_test_resource

# Define your resources
def setup_env(): ...
def cleanup_env(): ...

# Safe, nested execution
with managed_test_resource("Environment", setup_env, cleanup_env):
    # Your test logic here
    assert 1 == 1
