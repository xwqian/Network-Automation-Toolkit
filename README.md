# Network Automation Toolkit

A production-grade Python framework designed for **Cloud-Native Infrastructure Lifecycle Management**. This toolkit provides robust design patterns for automated testing, fault injection, and reliable resource handling in complex CI/CD pipelines.

## Overview
In large-scale integration testing—particularly for microservices and network components—maintaining environmental consistency is a major challenge. This toolkit helps bridge the gap between infrastructure configuration and testing logic, ensuring stability and reproducibility.

---

## Key Architecture Modules

### 1. Atomic Resource Manager
**Problem:** Frequent test failures in CI/CD often lead to "orphan" cloud resources (leaked security groups, dangling containers), causing infrastructure pollution and cost inflation.

**Solution:** A **Context Manager-based Resource Lifecycle Controller**.
- **Atomic Operations:** Ensures that environment setup and teardown occur in a strictly controlled lifecycle using the `with` statement.
- **Nested Dependency Management:** Supports hierarchical resource loading (e.g., VPC → K8s Cluster → Microservice Pod), ensuring resources are torn down in the correct topological order.
- **Resilience:** By utilizing `try...finally` blocks, the framework guarantees 100% resource cleanup even during pipeline timeouts or unexpected crashes.

### 2. Network Behavior Mocking System
**Problem:** Reproducing intermittent network failures (e.g., BGP flapping, high latency, protocol resets) in a stable CI/CD pipeline is physically impossible and cost-prohibitive.

**Solution:** A **Network Behavior Injection Framework** based on `unittest.mock` and `side_effect`.
- **Fault Injection:** Programmatically simulates various network errors (e.g., 503 Service Unavailable, Connection Refused) without modifying production code.
- **Negative Testing:** Enables systematic verification of system retry policies and failure-handling mechanisms, ensuring robust defensive coding.
- **Efficiency:** Allows for the simulation of complex network convergence edge-cases in < 1 second within automated pipelines.

---

## Design Philosophy
- **Separation of Concerns:** By decoupling the **Infrastructure Lifecycle (Infra)** from the **Business Logic (Test)**, we improve test readability and maintainability.
- **Determinism:** Eliminating the randomness inherent in external network dependencies, resulting in "flaky-test-free" pipelines.
- **Defensive Engineering:** We shift the focus from "Happy Path" testing to "Failure Path" validation, ensuring system reliability under duress.

---

## Quick Start
```python
from modules.resource_manager import managed_test_resource

# Example: Managing nested infrastructure dependencies
with managed_test_resource("VPC-Layer", setup_vpc, cleanup_vpc):
    with managed_test_resource("K8s-Pod", setup_pod, cleanup_pod):
        # Business logic integration test
        assert perform_api_call() == 200
