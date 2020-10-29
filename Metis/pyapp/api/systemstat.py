from flask import Blueprint, request, jsonify, Response
from flask_restx import Namespace, Resource
from pyapp.auth import auth, parseAuthHeader
import sys
import platform,socket,re,uuid,json,psutil,logging
from pyapp import config

api = Namespace('systemstat', description='System Stats Endpoints')

@api.route("/all_info")
class Allinfo(Resource):
    
    def get(self):        
        '''
        Return the System Information
        '''
        auth = request.headers.get('Authorization')
        valid, token = parseAuthHeader(auth)
        if valid and config.AUTH_TOKEN==token :
            info={}
            info['platform']=platform.system()
            info['platform-release']=platform.release()
            info['platform-version']=platform.version()
            info['architecture']=platform.machine()
            info['hostname']=socket.gethostname()
            info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
            info['processor']=platform.processor()
            info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
            return jsonify(info)
        else:
            return Response("{'message':'Invalid Authprization Token or Headers'}", status=400, mimetype='application/json')

@api.route("/cpu")
class CPU(Resource):
    
    def get(self):        
        '''
        Return Cpu Information
        '''
        auth = request.headers.get('Authorization')
        valid, token = parseAuthHeader(auth)
        if valid and config.AUTH_TOKEN==token :
            info={}
            info['processor']=platform.processor()
            info['CPU Percentage']=str(psutil.cpu_percent())+' %'
            info['CPU Count']=str(psutil.cpu_count())
            info['CPU Time Percent']=str(psutil.cpu_times_percent())
            info['CPU Stat']=str(psutil.cpu_stats())
            info['Max Frequency']=str(psutil.cpu_freq().max)+' Mhz'
            info['Min Frequency']=str(psutil.cpu_freq().max)+' Mhz'
            info['Current Frequency']=str(psutil.cpu_freq().max)+' Mhz'
            return jsonify(info)
        else:
            return Response("{'message':'Invalid Authprization Token or Headers'}", status=400, mimetype='application/json')
        
@api.route("/ram")
class Ram(Resource):
    
    def get(self):        
        '''
        Return RAM Information
        '''
        auth = request.headers.get('Authorization')
        valid, token = parseAuthHeader(auth)
        if valid and config.AUTH_TOKEN==token :
            info={}
            info['Ram Total']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
            info['Ram Available']=str(round(psutil.virtual_memory().available / (1024.0 **3)))+" GB"
            info['Ram Used']=str(round(psutil.virtual_memory().used / (1024.0 **3)))+" GB"
            return jsonify(info)
        else:
            return Response("{'message':'Invalid Authprization Token or Headers'}", status=400, mimetype='application/json')

@api.route("/disk")
class Ram(Resource):
    
    def get(self):        
        '''
        Return Disk Information
        '''
        auth = request.headers.get('Authorization')
        valid, token = parseAuthHeader(auth)
        if valid and config.AUTH_TOKEN==token :
            info={}
            info['Total read']=str(round(psutil.disk_io_counters().read_bytes / (1024.0 **3)))+" GB"
            info['Total write']=str(round(psutil.disk_io_counters().write_bytes / (1024.0 **3)))+" GB"
            return jsonify(info)
        else:
            return Response("{'message':'Invalid Authprization Token or Headers'}", status=400, mimetype='application/json')

