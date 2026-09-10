# Design Principles

## Separation of Concerns

AI reasoning, external providers, local execution, and knowledge storage
should remain independent components.

## Provider and Resource Independence

AI systems should be designed around capabilities rather than dependency on
specific providers, services, or hardware configurations.

The system should accommodate changes in available computational resources,
model providers, execution environments, and external services without
requiring a redesign of the overall architecture.

This includes situations where:

- a service changes its pricing model
- a provider becomes unavailable
- a preferred model is replaced by a newer alternative
- local hardware limitations require a different execution strategy

The goal is to create a system where individual components can be replaced
while preserving the identity and behavior of the larger architecture.

This can be viewed as the "Clothing Principle": the system should be able to
change its external components without changing its underlying structure.

## Human Authorization

Actions affecting external systems should remain governed by explicit rules.

## Model Configuration Independence

The behavior of an AI system should not depend solely on default model
settings.

System behavior should be intentionally configured through:
- system instructions
- model parameters
- evaluation criteria
- task-specific constraints

## Local-First Development

Private data and personal workflows should remain under user control.

## Observable Systems

System behavior should be inspectable and understandable.
