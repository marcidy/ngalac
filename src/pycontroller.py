import asyncio
from obswsrc import OBSWS
from obswsrc.requests import (GetStreamingStatusRequest, 
        StartStreamingRequest, 
        StopStreamingRequest,
        StartStopStreamingRequest
        )
from obswsrc.types import Stream, StreamSettings
from arduino_controller import NgalacArduinoController as acontrol


async def main():
    g = acontrol()
    streaming = False

    async with OBSWS('localhost', 4444, 'password') as obsws:
        response = await obsws.require(GetStreamingStatusRequest())
        if g.get_state()[11] == 1:
            g.flip_lights()
            g.release_latches()

            await obsws.require(StartStopStreamingRequest())


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
