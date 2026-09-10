"""
Simple provider abstraction example.

The application depends on an interface rather than a specific provider.
"""


class AIProvider:
    """Base interface for AI providers."""

    def generate(self, prompt: str) -> str:
        raise NotImplementedError


class LocalProvider(AIProvider):
    """Example local AI provider."""

    def generate(self, prompt: str) -> str:
        return f"Local response to: {prompt}"


class ExternalProvider(AIProvider):
    """Example external AI provider."""

    def generate(self, prompt: str) -> str:
        return f"External response to: {prompt}"


def ask_provider(provider: AIProvider, prompt: str) -> str:
    return provider.generate(prompt)


if __name__ == "__main__":
    prompt = "Explain provider independence."

    providers = [
        LocalProvider(),
        ExternalProvider(),
    ]

    for provider in providers:
        print(ask_provider(provider, prompt))