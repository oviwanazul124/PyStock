from src.models.type_prompt_mode import PromptMode
from src.utils.confirmation_prompt import confirmation_prompt

def test_confirmation_prompt(monkeypatch):
    # Test for UPDATE_CONFIRM
    monkeypatch.setattr('builtins.input', lambda _: 'y')
    assert confirmation_prompt(PromptMode.UPDATE_CONFIRM) is None

    monkeypatch.setattr('builtins.input', lambda _: 'n')
    assert confirmation_prompt(PromptMode.UPDATE_CONFIRM) == False

    # Test for UPDATE_MORE_CONFIRM
    monkeypatch.setattr('builtins.input', lambda _: 'y')
    assert confirmation_prompt(PromptMode.UPDATE_MORE_CONFIRM) == True

    monkeypatch.setattr('builtins.input', lambda _: 'n')
    assert confirmation_prompt(PromptMode.UPDATE_MORE_CONFIRM) == False

    # Test for DELETE_CONFIRM
    monkeypatch.setattr('builtins.input', lambda _: 'y')
    assert confirmation_prompt(PromptMode.DELETE_CONFIRM) == True

    monkeypatch.setattr('builtins.input', lambda _: 'n')
    assert confirmation_prompt(PromptMode.DELETE_CONFIRM) == False

    # Test for ADD_CONFIRM
    monkeypatch.setattr('builtins.input', lambda _: 'y')
    assert confirmation_prompt(PromptMode.ADD_CONFIRM) == True

    monkeypatch.setattr('builtins.input', lambda _: 'n')
    assert confirmation_prompt(PromptMode.ADD_CONFIRM) == False