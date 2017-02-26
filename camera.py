from logger import Logger
from http_connector import Get


l = Logger(__name__)

class Camera():
    def __init__(self, host, password, useTLS=False):
        self.__setHost(host, useTLS)
        self.__setCredentials("admin", password)
    def __setCredentials(self, login, password):
        self.auth = (login, password)
        l.debug("Credentials set to: {}:{}".format(*self.auth))
    def __setHost(self, host, useTLS=False):
        self.host = host
        scheme = "http://"
        if useTLS:
            self.port = 443
            scheme = "https://"
        else:
            self.port = 80
        self.target = "{}{}:{}".format(scheme, self.host, self.port)
        l.debug("Host set to: {}:{}".format(self.host, self.port))
    def __buildURI(self, location):
        return "{}{}".format(self.target, location)
    def checkAuth(self):
        uri = self.__buildURI("/users/verify.cgi")
        r = Get(uri, self.auth, parse="common")
        if r['group'] == "Administrator":
            l.info("Successfully authenticated.")
            return True
        else:
            l.error("Authentication failed.")
            return False
    def getName(self):
        uri = self.__buildURI("/config/camera_info.cgi")
        r = Get(uri, self.auth, parse="common")
        l.info("Connected to: {}, located at: {}"\
            .format(r['name'], r['location']))
        return r.values()
    def getSdcard(self):
        uri = self.__buildURI("/config/sdcard.cgi")
        r = Get(uri, self.auth, parse="common")
        l.info("SD card status: {}.".format(r['status']))
        if r['status'] == "invalid":
            return False
        else:
            return True
    def getScreenshot(self):
        uri = self.__buildURI("/image/jpeg.cgi")
        jpeg = Get(uri, self.auth, parse="blob")
        l.info("Screenshot created. Size: {} bytes.".format(len(jpeg)))
        return jpeg
    def getWirelessConfig(self):
        uri = self.__buildURI("/config/wireless.cgi")
        r = Get(uri, self.auth, parse="common")
        l.info("Wireless state: {}. Mode: {}, essid: {} (ch:{}, {})."\
            .format(r['enable'], r['mode'], r['essid'], r['channel'], r['auth'])
            )
        return r
    def scanWifiAP(self):
        uri=self.__buildURI("config/wlansurvey.cgi")
        r = Get(uri, self.auth, parse=None)
        l.debug("Detected WIFI APs: {}".format(r))
        return r
    def getICR(self):
        uri = self.__buildURI("/config/icr.cgi")
        r = Get(uri, self.auth, parse="common")
        l.info("ICR mode: {}. Light threshold is set to {}.".format(r['mode'],
            r['light_threshold']))
        return r
    def getLED(self):
        uri = self.__buildURI("/config/led.cgi")
        r = Get(uri, self.auth, parse="common")
        l.info("Device control LED is {}.".format(r['led']))
        return r
    def getSpeaker(self):
        uri = self.__buildURI("/config/speaker.cgi")
        r = Get(uri, self.auth, parse="common")
        l.info("Speaker enabled: {}. Volume: {}.".format(r['enable'],
            r['volume']))
        return r
    def getAudioDetection(self):
        uri = self.__buildURI("/config/audio_detection.cgi")
        r = Get(uri, self.auth, parse="common")
        l.info("Audio detection enabled: {}. Sensitivity: {}.".format(r['enable'],
            r['sensitivity']))
        return r
    def getMotionDetection(self):
        uri = self.__buildURI("/config/motion.cgi")
        r = Get(uri, self.auth, parse="common")
        l.info("Motion detection enabled: {}. Sensitivity: {}.".format(r['enable'],
            r['sensitivity']))
        return r
    def getSensorInfo(self):
        uri = self.__buildURI("/config/sensor.cgi")
        r = Get(uri, self.auth, parse="common")
        l.info("Sensor: BR: {}, CN: {}, ST:{}, WB:{}. Color: {}.".format(
            r['brightness'], r['contrast'], r['saturation'], r['whitebalance'],
            r['color']))
        return r
