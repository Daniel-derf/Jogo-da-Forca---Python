# from . import checkLetterWithWord, getErrorCont

GAME_INPUT_MSG: str = "Digite a letra desejada:"
GAME_LOST_MSG: str = "Fim de jogo! O enforcamento aconteceu :("
GAME_WIN_MSG: str = "Vitória! Sem enforcamento :)"
INVALID_INPUT_MSG: str = "Valor inválido. Tente novamente."
ALREADY_TYPED_LETTER_MSG: str = "Valor já digitado. Tente novamente."
ERROR_CONT_MSG: str = "Quantidade de erros (máximo 5): "

typedLetters: list[str] = []
error_cont: int

def checkLetterWithWord(letter: str) -> str:
    return GAME_WIN_MSG

def getErrorCont():
    return 1


def startGame() -> None:
    error_cont = getErrorCont()
    print(ERROR_CONT_MSG, error_cont)
    game_input = input(GAME_INPUT_MSG)
    if isValidInput(game_input):
        print(checkPlay(game_input))
    else:
        print(INVALID_INPUT_MSG)
        startGame()


def isValidInput(input: str) -> bool:
    VALID_INPUT_CONDITIONS: bool = input.isalpha() and len(input) == 1
    return True if VALID_INPUT_CONDITIONS else False


def checkPlay(game_input: str) -> None:
    if game_input not in typedLetters:
        typedLetters.append(game_input)
        return checkLetterWithWord(game_input)
    else:
        return ALREADY_TYPED_LETTER_MSG


startGame()
