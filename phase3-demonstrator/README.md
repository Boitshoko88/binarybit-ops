# Binary Bit Ops Phase 3 demonstrator

This self-contained workload demonstrates 16-bit binary AND, OR, and XOR operations for HDE WBS task 3.10. It accepts two unsigned values and prints the inputs and results in decimal and binary. The default example uses 12 and 10, producing AND 8, OR 14, and XOR 6.

## Scope boundary

This directory contains a non-production demonstrator only. It has no database, credentials, personal data, or external API connections. The live Binary Bit Ops/Nexus PHP/MySQL application remains on Truehost cPanel; this workload does not modify, migrate, or deploy that application.

## Run locally

Run commands from this directory. Requires Python 3.12 or later.

```sh
python binarybitops.py
python binarybitops.py 12 10
python binarybitops.py 0xC 0b1010
python -m unittest discover -s tests -v
```

Inputs must be between 0 and 65535.

## Container image

Build from this directory so the Dockerfile context contains only the demonstrator source:

```sh
docker build -t binarybitops-demo:local .
docker run --rm binarybitops-demo:local
```

The image runs as a non-root user, prints one result, and exits. It is suitable for a separate non-production Kubernetes Job.

## HDE delivery

Use the reviewed source revision as the input to the task 3.9 Tekton delivery path. Publish an immutable image tag, record the verified digest in the separate GitOps repository through a reviewed pull request, then have the authorized platform owner manually sync the non-production Argo CD application. This README does not claim a pipeline run or deployment; save that evidence after the run succeeds.
