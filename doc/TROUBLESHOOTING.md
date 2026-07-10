# Troubleshooting Handbook: Kubernetes & Cloud Network

This guide documents the standardized diagnostic workflow used to identify and resolve network-related service outages in K8s-based environments.

## 1. Diagnostic Logic: The "Outside-In" Principle
When a service is unreachable, we follow this hierarchical diagnostic path to minimize MTTR (Mean Time To Recovery):

1. **Infrastructure/Cloud Layer:** Check cloud gateways, VPC routing tables, and security group/firewall rules.
2. **K8s Service Layer:** Verify if endpoints are populated and if the LoadBalancer/Ingress is active.
3. **Pod Lifecycle Layer:** Check Pod status, events, and resource constraints (OOMKilled).
4. **Network/Application Layer:** Trace connectivity via `curl` and inspect application logs for internal exceptions.

## 2. Command-Line Diagnostic Checklist

| Phase | Command | Goal |
| :--- | :--- | :--- |
| **Visibility** | `kubectl get pods,svc,endpoints` | Confirm pod readiness and endpoint mapping. |
| **Event Inspection** | `kubectl describe pod <pod-name>` | Identify "ImagePullBackOff" or "CrashLoopBackOff" triggers. |
| **Logs/Trace** | `kubectl logs <pod-name> --previous` | Extract app-level exceptions from the last crash. |
| **Network Drill** | `kubectl exec -it <pod-name> -- curl -v <target>` | Verify L7 reachability from inside the pod namespace. |

## 3. Resilience Strategy (The "War Room" Mindset)
- **Isolation:** Determine if the issue is global (e.g., node down) or isolated (e.g., specific pod).
- **Log Correlation:** Use `correlation IDs` across services to trace requests through the network.
- **Rollback vs. Debug:** For critical outages, prioritize **"Rollback first, Debug later"** to restore production service before performing root cause analysis (RCA).
