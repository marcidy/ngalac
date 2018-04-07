import asyncio
from obswsrc import OBSWS
from obswsrc.requests import (GetStreamingStatusRequest,
                              StartStreamingRequest,
                              StopStreamingRequest,
                              StartStopStreamingRequest,
                              StartStopRecordingRequest
                              )
from obswsrc.types import Stream, StreamSettings
from arduino_controller import NgalacArduinoController as arduino
import time

# need port detection to pass to arduino controller


async def main():
    g = arduino("COM5")
    g.release_latches()
    streaming = False
    obs_streaming = False

    async with OBSWS('localhost', 4444, 'password') as obsws:

        while True:
            try:
                g.clear()
                g.get_state()
                ret = g.rec()

                if ret:
                    cmd, state = ret
                    print("{}: {}".format(cmd, state))

                    if state[11] == 1:
                        await obsws.require(StartStopStreamingRequest())
                        g.release_latches()

                        obs_status = await obsws.require(GetStreamingStatusRequest())  #NOQA
                        obs_streaming = obs_status['streaming']

                if streaming and not obs_streaming:
                    streaming = False
                    g.lights(0)

                elif not streaming and obs_streaming:
                    streaming = True
                    g.lights(1)

            except ConnectionRefusedError:
                print("sleeping a bit, yawn")
                time.sleep(2)


loop = asyncio.get_event_loop()
try:
    asyncio.ensure_future(main())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    loop.close()
