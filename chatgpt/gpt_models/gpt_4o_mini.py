from chatgpt.enums import Endpoint, Model, Role
from chatgpt.errors import ChatGPTGeneralError
from ..types import RequestDictT
from ._base import Base


class GPT4oMini(Base):
    def __init__(self, api_key: str, temperature: float = 1) -> None:
        super().__init__(
            api_key,
            Model.GPT_35_TURBO,
            Endpoint.CHAT_COMPLETION,
            temperature=temperature,
        )

    async def system_prompt(self, prompt: str) -> str:
        data: RequestDictT = {
            "model": self._model,
            "temperature": self._temperature,
            "messages": [
                {"role": Role.SYSTEM, "content": prompt},
            ],
        }

        resp = await self._request(data)
        if resp.get("error", False):
            raise ChatGPTGeneralError(f"Open AI ChatGPT API says: {resp}")
        return str(resp["choices"][0]["message"]["content"])
