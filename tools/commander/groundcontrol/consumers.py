import toolkit as tk
import urllib,json
from websocket import create_connection
from threading import Thread
from multiprocessing import Process
import psutil
import requests
import time

import socket

import base64



# COMPLETE
class Telemetry:

    """
    All telemetry requests from the client side are channeled through an instance of Telemetry class.
    These requests are forwarded to pyliner or YAMCS through web sockets. A system process is created to listen to data on these sockets.
    All the information required to track each subscription is stored in a data structure called 'subscribers' which will be used later to
    properly unsubscribe to data and kill process generated.
    """

    def __init__(self):
        """
        Initializes data structures and assigned default values to constants.
        """
        self.subscribers = []

        self.defaultInstance= None
        self.port = 8090
        self.address = '127.0.0.1'
        self.yamcs_ws = create_connection('ws://' + str(self.address) + ':' + str(self.port) + '/'+str(self.getInstanceName())+'/_websocket')

        self.tlmSeqNum = 0
        self.processArray = []
        #self.specialSeqNumber =0
        self.killed = 0
        self.ignition =True


    def connect(self, message):
        """
        Sets default instance and accepts connection from client.
        :param message: message object
        :return: void
        """
        self.housekeeping()
        message.reply_channel.send({'accept': True})
        tk.log(self.defaultInstance,'Got Telemetry connection request from client','INFO')

    def disconnect(self, message):
        """
        Sends disconnect signal to client.
        :param message: message object
        :return: void
        """
        message.reply_channel.send({'close': True})
        tk.log('self.defaultInstance', 'Got Telemetry (dis)connection request from client', 'INFO')

    def looseTelemetry(self, message):
        """
        Process unsubscribe requests for telemetry and kills all processes related to a particular telemetry.
        :param message:message object
        :return: void
        """
        message_text = message.content['text']
        print message_text

        if message_text == 'START_COMM_HS':
            message.reply_channel.send({'text': 'START_COMM_ACK'})

        elif message_text == 'CLOSE_COMM_NOFBCK':
            self.disconnect(message)
        elif message_text == 'US_ALL':
            for each in self.subscribers.keys():
                try:
                    pid = self.subscribers[each]['pid']
                    process = self.subscribers[each]['process']
                    if process.is_alive():
                        to_kill = psutil.Process(pid)
                        to_kill.kill()
                    del self.subscribers[each]
                    tk.log(each, 'Telemetry push process is now killed.', 'INFO')
                except:
                    tk.log(each, 'Telemetry push process ALREADY KILLED.', 'INFO')
        elif message_text.find('tlm')!=-1:

        # Converting message text to hashable key.
            try:
                prepare1 = json.loads(tk.byteify(message_text))
                prepare1['tlm'][0].pop('format', None)
                prepare2 = json.dumps(prepare1)
                #myUnit = self.subscribers[prepare2]

            # Converting message text to a format understood by pyliner or YAMCS.
                temp = tk.byteify(message_text)
                temp = json.loads(temp)
                temp = ' {"parameter":"unsubscribe", "data":{"list":' + str(tk.byteify(temp['tlm'])) + '}}'
                temp = temp.replace("\'", "\"")
                to_send = '[1,1,0,' + str(temp) + ']'
                print '********************************'
                print to_send
                print '********************************'
            # Get websocket object and process ID, kill process and send unsubscribe signal to pyliner or YAMCS
                #ws = myUnit['ws']
                #pid = myUnit['pid']
                #process = myUnit['process']
                #if process.is_alive():
                #    to_kill = psutil.Process(pid)
                #    to_kill.kill()
                #    self.killed=self.killed+1
                #del self.subscribers[prepare2]
                self.yamcs_ws.send(to_send)
                if  prepare2 in self.subscribers : self.subscribers.remove(prepare2)
                #self.subscribers.pop(prepare2,None)
                tk.log(message.content['text'], 'Telemetry push process is now killed.', 'INFO')
            except:
                tk.log(message_text, 'Telemetry push process ALREADY KILLED.', 'INFO')

    def getTelemetry(self, message):
        """
        Process subscribe requests for telemetry and creates system processes which pushes data to client.
        :param message: message object
        :return: void
        """
        message_text = message.content['text']
        unit = {}

        if message_text.find('tlm')!=-1:

        # Converting message text to hashable key.
            prepare1 =json.loads(tk.byteify(message_text))
            prepare1['tlm'][0].pop('format',None)
            prepare2 = json.dumps(prepare1)

            key = prepare2
            self.subscribers.append(key)
            process = None
            #myID = self.specialSeqNumber

        # Converting message text to a format understood by pyliner or YAMCS.
            temp = tk.byteify(message_text)
            temp = json.loads(temp)
            temp = ' {"parameter":"subscribe", "data":{"list":' + str(tk.byteify(temp['tlm'])) + '}}'
            temp = temp.replace("\'", "\"")
            to_send = '[1,1,0,' + str(temp) + ']'


        # Send message, start a system process, store current data in a local dict.
            self.yamcs_ws.send(to_send)
            if self.ignition:
                process = Process(target=self.push, args=(self.yamcs_ws, message))
                process.start()
                self.processArray.append(process)
            self.ignition=False
                #pid = process.pid

            #process = Process(target=self.push, args=(ws,message))
            #process.start()
            #pid = process.pid
            #self.specialSeqNumber = self.specialSeqNumber + 1
            #unit['myID'] = myID
            #unit['message'] = message
            #unit['process'] = process
            #unit['pid'] = pid
            #unit['ws'] = ws
            #self.subscribers[key]=unit

    def housekeeping(self):
        """
        Reads config file 'session.json' and sets default instance value.
        :return: void
        """
        json = tk.readSESSION()
        self.defaultInstance = json["InstanceName"]

    def getInstanceName(self):
        """
        Reads config file 'session.json' and returns default instance value.
        :return: string
        """
        json = tk.readSESSION()
        return json["InstanceName"]

    def push(self, websocket_obj, message_obj):
        """
        A forever loop to receive and push telemetry to client.
        :param websocket_obj:  websocket object
        :param message_obj: message object
        :return: void
        """
        while True:
            result = websocket_obj.recv()
            if result != '[1,2,0]':
                result = tk.preProcess(result)
                try:
                    message_obj.reply_channel.send({'text': result})
                except:
                    time.sleep(1)
                    message_obj.reply_channel.send({'text': result})
                tk.log(message_obj.content['text'], 'Telemetry packet sent to client', 'INFO')

class Command:

    def __init__(self):
        """
        Initializes data structures and assigned default values to constants.
        """
        #self.subscribers = {}
        self.defaultInstance = None
        self.port = 8090
        self.address = '127.0.0.1'
        # self.tlmSeqNum = 0
        #self.specialSeqNumber = 0
        #self.killed = 0

    def connect(self, message):
        """
        Sets default instance and accepts connection from client.
        :param message: message object
        :return: void
        """

        message.reply_channel.send({'accept': True})
        self.housekeeping()
        tk.log(self.defaultInstance,'Got Commanding connection request from client','INFO')

    def disconnect(self, message):
        """
        Sends disconnect signal to client.
        :param message: message object
        :return: void
        """
        message.reply_channel.send({'close': True})
        tk.log('self.defaultInstance', 'Got Commanding (dis)connection request from client', 'INFO')

    def getCommandInfo(self, message):




        message_text = message.content['text']
        print '**************************'
        print '==> ', message_text
        print '**************************'
        if message_text == 'HS':
            message.reply_channel.send({'text': 'HSOK'})
        else:
            if self.defaultInstance!=None:
                response = urllib.urlopen('http://' + str(self.address) + ':' + str(self.port) + '/api/mdb/'+ str(self.defaultInstance)+'/commands'+message_text)
            else:
                response = urllib.urlopen('http://' + str(self.address) + ':' + str(self.port) + '/api/mdb/'+ self.getInstanceName()+'/commands'+message_text)

            data = json.loads(json.dumps(response.read()))
            data = data.replace("\"", "\'")


            message.reply_channel.send({'text':data})
            #time.sleep(5);
            #message.reply_channel.send({'text': 'HSOK'})


    def postCommand(self, message):
        message_text = message.content['text']


        #if message_text == 'START_COMM_HS':
        #    message.reply_channel.send({'text': 'START_COMM_ACK'})

        #elif message_text == 'CLOSE_COMM_NOFBCK':
        #    self.disconnect(message)

        #else:
        print '**************************'
        print message_text
        to_post = json.loads(message_text)
        print '**************************'
        url=''
        if self.defaultInstance!=None:
            url = 'http://' + str(self.address) + ':' + str(self.port) +'/api/processors/' + str(self.defaultInstance) + '/realtime/commands' + to_post['name'] + '?nolink'
        else:
            url = 'http://' + str(self.address) + ':' + str(self.port) +'/api/processors/' + self.getInstanceName() + '/realtime/commands' + to_post['name'] + '?nolink'

        msg = '{"sequenceNumber": 0,"origin": "user@my-machine","assignment":'+ str(json.dumps(to_post['args']))+',"dryRun": false}'
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        #msg = json.dumps(msg)
        r = requests.post(url=url, data=msg, headers = headers)
        got = r.text
        message.reply_channel.send({'text': got})
        print '**************************'
        print msg
        print got
        #to_post = json.loads(message_text)
        print '**************************'




    def housekeeping(self):
        """
        Reads config file 'session.json' and sets default instance value.
        :return: void
        """
        json = tk.readSESSION()
        self.defaultInstance = json["InstanceName"]

    def getInstanceName(self):
        """
        Reads config file 'session.json' and returns default instance value.
        :return: string
        """
        json = tk.readSESSION()
        return json["InstanceName"]

class Instance:
    def __init__(self):
        self.port = 8090
        self.address = '127.0.0.1'

    def connect(self, message):
        message.reply_channel.send({'accept': True})


    def disconnect(self, message):
        message.reply_channel.send({'close': True})


    def getInstanceList(self, message):

        name = message.content['text']
        response = urllib.urlopen('http://' + str(self.address) + ':' + str(self.port) + '/api/instances')
        data = json.loads(json.dumps(response.read()))
        message.reply_channel.send({'text': data})


    def setDefaultInstance(self,message):
        name = message.content['text']
        json = tk.readSESSION()
        json["InstanceName"]=name
        tk.writeSESSION(json)


        #message.reply_channel.send({'close': True})

class Directory:
    def connect(self,message):
        message.reply_channel.send({'accept': True})

    def disconnect(self,message):
        message.reply_channel.send({'close': True})



    def directoryListing(self,message):
        name = message.content['text']
        print message
        response = tk.get_directory(name)
        data = json.dumps(response)
        message.reply_channel.send({'text': data})
        print '[' + tk.getDate() + ']' + ' Packet ' + name + ' sent.'

class Event:
    def __init__(self):

        self.port = 8090
        self.address = '127.0.0.1'
        self.tlmSeqNum = 0



    def connect(self,message):
        self.housekeeping()
        message.reply_channel.send({'accept': True})


    def disconnect(self,message):
        message.reply_channel.send({'close': True})



    def getEvents(self,message):
        message_text = message.content['text']
        data = '[1, 1, 1, {"events": "subscribe"}]'
        ws = create_connection('ws://' + self.address + ':' + str(self.port) + '/'+self.getDefaultInstance()+'/_websocket')
        ws.send(data)
        t = Thread(target=self.push, args=[ws, message])
        t.start()

    def getDefaultInstance(self):
        json = tk.readSESSION()
        return json["InstanceName"]

    def housekeeping(self):
        json = tk.readSESSION()
        self.defaultInstance = json["InstanceName"]



    def push(self,websocket_obj,message_obj):
        while True:
            result = websocket_obj.recv()

            if result.find('[1,4,')!=-1 :
                #result = tk.preProcess(result)
                message_obj.reply_channel.send({'text': result})
                print result
                tk.log('', 'BOUND', 'INFO')

class Misc:
    def __init__(self):

        self.mapping = {
            'ADSB':'http://127.0.0.1:9000/test'
        }
        self.port = 8090
        self.address = '127.0.0.1'

    def connect(self, message):
        message.reply_channel.send({'accept': True})


    def disconnect(self, message):
        message.reply_channel.send({'close': True})



    def getMisc(self, message):
        name = message.content['text']

        if name == 'START_COMM_HS':
            message.reply_channel.send({'text': 'START_COMM_ACK'})

        elif name == 'CLOSE_COMM_NOFBCK':
            tk.log('GET INSTANCE LIST', 'DISCONNECTING FROM SOCKET', 'INFO')
        else:
            response = urllib.urlopen(self.mapping[name])
            data = json.loads(json.dumps(response.read()))
            message.reply_channel.send({'text': data})
            tk.log(name, 'PACKET SENT', 'INFO')

class Video:
    def __init__(self):
        self.address = '127.0.0.1'
        self.video_port = 3001
        self.video_frame_counter = 0
        self.video_socket = None

    def connect(self, message):
        print 'plug0'
        message.reply_channel.send({'accept': True})


    def disconnect(self, message):
        message.reply_channel.send({'close': True})


    def getVideo(self, message):
        print 'plug0.5'
        name = message.content['text']
        #buff = \
        self.VideoThroughUDP(message)
        #message.reply_channel.send({'text': buff})

    def VideoThroughUDP(self,msg_obj):
        UDP_IP = self.address
        UDP_PORT = self.video_port
        self.video_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # UDP
        self.video_socket.bind(("", UDP_PORT))
        print 'plug1'
        while True:
            print 'plug2'
            data, addr = self.video_socket.recvfrom(65527)  # buffer size is 1024 bytes
            b64_img = base64.b64encode(data)
            self.video_frame_counter = self.video_frame_counter + 1
            print 'Frame# : ['+str(self.video_frame_counter)+'] sent.'
            msg_obj.reply_channel.send({'text': b64_img})
            #yield b64_img
