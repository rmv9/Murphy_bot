"Variable custom exceptions."


class CheckTokensEnvFailure(Exception):
    """Unreacheble tokens in dotenv."""


class SendMessageFailure(Exception):
    """Failed to send message."""
