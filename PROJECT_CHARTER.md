# Quantum Computing Lab — Project Charter

## Vision

Build an open-source Quantum Computing Academy that provides a structured,
practical and accessible learning path from foundational concepts to advanced
quantum engineering and research.

The project aims to become more than a collection of notebooks. It is designed
as a coherent educational, experimental and research ecosystem.

## Mission

Democratize quantum computing through high-quality open education, practical
experimentation, reproducible software and community-driven knowledge.

## Project Objectives

The Quantum Computing Lab aims to:

- Provide structured quantum computing curricula
- Combine theory, mathematics and practical implementation
- Support progressive learning from beginner to research level
- Develop reusable quantum software components
- Compare quantum frameworks, simulators and hardware providers
- Reproduce and analyze relevant quantum computing research
- Offer guided projects, exercises, assessments and challenges
- Promote reproducibility and high-quality software engineering
- Build an open and welcoming contributor community

## Target Audience

The project is intended for:

- Beginners exploring quantum computing
- Software developers moving into quantum technologies
- Students and educators
- Data scientists and machine learning engineers
- Security and cryptography professionals
- Quantum software engineers
- Researchers and technical contributors

## Core Components

The repository is organized into the following major components:

| Component | Purpose |
|---|---|
| Academy | Structured educational curricula and learning paths |
| Benchmarks | Performance comparisons across frameworks and backends |
| Documentation | Technical, architectural and contributor documentation |
| Examples | Small focused usage examples |
| Projects | Guided practical projects |
| Research | Paper reproductions, experiments and original investigations |
| Source | Reusable Python packages and utilities |
| Tests | Automated validation and quality controls |
| Tools | Repository and development utilities |

## Educational Principles

Academy content should:

- Progress from fundamentals to advanced topics
- Explain concepts before introducing framework-specific code
- Include only the mathematics required for the learning objective
- Prefer visual and practical explanations where appropriate
- Provide exercises before solutions
- Clearly separate theory, implementation and experimentation
- Avoid vendor lock-in
- Compare frameworks objectively
- State assumptions, limitations and prerequisites

## Engineering Principles

The project follows these principles:

- Reproducibility
- Modularity
- Testability
- Clear documentation
- Stable repository conventions
- Automated validation
- Explicit dependency management
- Small and reviewable changes
- Framework-neutral architecture where practical

## Supported Technology Foundation

The initial technology foundation includes:

- Python 3.12
- uv
- JupyterLab
- Qiskit and Qiskit Aer
- PennyLane
- Cirq
- QuTiP
- NumPy, SciPy, SymPy and related scientific libraries
- Ruff
- Pytest
- Pre-commit
- GitHub Actions

Additional frameworks and providers may be introduced only when they provide
clear educational, experimental or research value.

## Scope

The project includes:

- Educational content
- Interactive notebooks
- Quantum circuit implementations
- Simulator-based experiments
- Hardware execution examples
- Framework comparisons
- Quantum algorithms
- Quantum machine learning
- Quantum optimization
- Quantum cryptography
- Error correction
- Benchmarking
- Research reproductions

## Out of Scope

The project does not aim to:

- Claim accreditation before a formal certification model exists
- Replace university-level physics or mathematics programs
- Present speculative quantum advantages as established facts
- Promote a single framework or commercial provider
- Store access tokens, credentials or private research data
- Guarantee that experimental examples are production-ready

## Quality Standard

Content and code should be:

- Technically accurate
- Clearly sourced where appropriate
- Reproducible
- Tested when executable
- Reviewed for readability
- Accessible to the intended learning level
- Maintained alongside dependency and API changes

## Long-Term Direction

The long-term platform may include:

- Beginner, intermediate, advanced, expert and research curricula
- Role-based learning paths
- Interactive laboratories
- Assessment and progression systems
- Open-source completion certificates
- Instructor resources
- Community contributions
- Benchmark dashboards
- Quantum AI research
- A dedicated Academy website

## Development Workflow

Changes should normally follow this workflow:

1. Start from an updated `main` branch
2. Create a focused feature branch
3. Implement one coherent milestone or step
4. Run all relevant validations
5. Review the complete diff
6. Commit with a clear conventional message
7. Push the branch
8. Merge into `main`
9. Validate after the merge
10. Push the updated `main`
11. Delete the completed feature branch

## Current Phase

The project is currently in:

> Milestone M0 — Academy Foundation

The first active curriculum will be the Beginner Track.
