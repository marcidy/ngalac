import asyncio
from obswsrc import OBSWS
from obswsrc.requests import GetStreamingStatusRequest
from obswsrc.types import Stream, StreamSettings

async def main():
    async with OBSWS('localhost', 4444, 'password') as obsws:
        response = await obsws.require(GetStreamingStatusRequest())
        print("Streaming: {}".format(response.streaming))
        print("Recording: {}".format(response.recording))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
