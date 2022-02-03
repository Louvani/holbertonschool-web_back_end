#!/usr/bin/env python3
""" 4. Tasks"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """4. Tasks"""
    delay_list = []
    for index in range(n):
        delay_list.append(await task_wait_random(max_delay))
    done = await asyncio.gather(*asyncio.as_completed(delay_list))
    return sorted(done)
