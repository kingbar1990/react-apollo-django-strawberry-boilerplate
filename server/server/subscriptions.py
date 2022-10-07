import asyncio
from typing import AsyncGenerator

import strawberry


@strawberry.type
class Subscription:
    @strawberry.subscription
    async def count(self) -> AsyncGenerator[int, None]:
        for i in range(11):
            yield i
            await asyncio.sleep(0.5)
