# Authorization Boundary Example

This example demonstrates the separation between AI capability and system
authority.

An AI system may propose an action, but authorization and execution remain
separate concerns.

## Concept

```text
AI Recommendation
        |
        v
Authorization Policy
        |
        +---- Approved ----> Execution
        |
        +---- Denied
```

## Purpose

This is a simplified reference example.

It demonstrates a design principle rather than a production security system.

The purpose is to show that generating an action does not automatically grant
permission to perform that action.
