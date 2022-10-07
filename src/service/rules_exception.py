"""
Exceções das regras.
"""


class RulesException(Exception):
    def __init__(self, mensagem: str) -> None:
        super(RulesException, self).__init__(mensagem)
        self.mensagem = mensagem


class ExceptionNotFound(RulesException):
    def __init__(self, mensagem: str) -> None:
        super(ExceptionNotFound, self).__init__(mensagem)


class OtherExceptionRules(RulesException):
    def __init__(self, mensagem: str) -> None:
        super(OtherExceptionRules, self).__init__(mensagem)

class OtherCodesExceptions(OtherExceptionRules):
    def __init__(self) -> None:
        super().__init__("Código diferentes") 