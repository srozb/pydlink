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
    def checkName(self):
        uri = self.__buildURI("/config/camera_info.cgi")
        r = Get(uri, self.auth, parse="common")
        l.info("Connected to: {}, located at: {}".format(r['name'], r['location']))
        return r.values()
    def checkSdcard(self):
        uri = self.__buildURI("/config/sdcard.cgi")
        r = Get(uri, self.auth, parse="common")
        l.info("SDCard status: {}".format(r['status']))
        if r['status'] == "invalid":
            return False
        else:
            return True
    def getScreenshot(self):
        uri = self.__buildURI("/image/jpeg.cgi")
        jpeg = Get(uri, self.auth, parse="blob")
        l.info("Screenshot created. Size: {} bytes.".format(len(jpeg)))
        return jpeg
