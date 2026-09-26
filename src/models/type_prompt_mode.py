from enum import Enum

class PromptMode(Enum):

    # Oriented for Update confirmation prompts
    UPDATE_CONFIRM = "update"
    UPDATE_MORE_CONFIRM = "update_more"

    # Oriented for Delete confirmation prompts
    DELETE_CONFIRM = "delete"

    # Oriented for Add confirmation prompts
    ADD_CONFIRM = "add"