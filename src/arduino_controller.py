import PyCmdMessenger
import obswsrc

COMMANDS = [['ping', ''],
        ['pong', 's'],
        ['player', 'i'],
        ['lights', 's'],
        ['get_state', ''],
        ['ret_state', 'i*'],
        ['release_latches', 's'],
        ['error', '']]


class NgalacArduinoController():
    '''  NGALAC uses an arduino to control button presses and turn on various lights.
    '''

    def __init__(self):
        self.arduino = PyCmdMessenger.ArduinoBoard("COM5", baud_rate=9600)
        self.commands = dict(COMMANDS)
        self.c = PyCmdMessenger.CmdMessenger(self.arduino, COMMANDS)
        self.arduino_state = self.get_state()

    def _send_cmd(self, cmd):
        if cmd in self.commands:
            self.c.send(cmd)
            return self._parse_msg(self.c.receive())
        else:
            pass  # heh, logging pls thx

    def ping(self):
        return self._send_cmd('ping')
        
    def is_player(self):
        return self._send_cmd('player')

    def flip_lights(self):
        return self._send_cmd('lights')

    def get_state(self):
        return self._send_cmd('get_state')

    def _parse_msg(self, msg):
        self.last_cmd, value, self.exec_time = msg
        return value

    def release_latches(self):
        return self._send_cmd('release_latches')

    def open(self):
        self.arduino.open()

    def close(self):
        self.arduino.close()
