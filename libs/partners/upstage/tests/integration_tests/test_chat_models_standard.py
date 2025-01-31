"""Standard LangChain interface tests"""

from typing import Type

import pytest
from langchain_core.language_models import BaseChatModel
from langchain_standard_tests.integration_tests import ChatModelIntegrationTests

from langchain_upstage import ChatUpstage


class TestUpstageStandard(ChatModelIntegrationTests):
    @pytest.fixture
    def chat_model_class(self) -> Type[BaseChatModel]:
        return ChatUpstage

    @pytest.fixture
    def chat_model_params(self) -> dict:
        return {
            "model": "solar-1-mini-chat",
        }

    @pytest.mark.xfail(reason="400s with tool calling currently")
    def test_tool_message_histories(
        self,
        chat_model_class: Type[BaseChatModel],
        chat_model_params: dict,
        chat_model_has_tool_calling: bool,
    ) -> None:
        super().test_tool_message_histories(
            chat_model_class, chat_model_params, chat_model_has_tool_calling
        )
