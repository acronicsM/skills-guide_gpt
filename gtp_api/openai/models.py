from g4f import ChatCompletion
from g4f.models import default

from . import Proveders


async def get_answer(content, provider, model):

    _model = default if not model.value else model.value
    _provider = Proveders[provider.value]

    response = await ChatCompletion.create_async(
        model=_model,
        messages=[{"role": "user", "content": content}],
        provired=_provider,
    )

    return response
