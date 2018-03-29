import PyCmdMessenger                                                           
                                                                                
arduino = PyCmdMessenger.ArduinoBoard("/dev/ttyUSB0", baud_rate=9600)           
                                                                                
commands = [['ping', ''],                                                       
            ['pong', 's'],                                                      
            ['player', 'i'],                                                    
            ['lights', ''],                                                     
            ['get_state', ''],                                                  
            ['ret_state', 'i*'],                                                
            ['error', '']]                                                      
                                                                                
c = PyCmdMessenger.CmdMessenger(arduino, commands)                              
                                                                                
c.send('ping')                                                                  
msg = c.receive()                                                               
print(msg)                                                                      
                                                                                
c.send('player')                                                                
print(c.receive())                                                              
                                                                                
#  Turn On Lights                                                               
c.send('lights')                                                                
                                                                                
c.send('get_state')                                                             
msg = c.receive()                                                               
print(msg)                                                                      
                                                                                
#  Turn off Lights                                                              
c.send('lights')                                                                
c.send('get_state')                                                             
msg = c.receive()                                                               
print(msg)                                                                      
                                                                                
controls = msg[1]                                                               
if controls[0] != 0:                                                            
    print("Start Stream!")
