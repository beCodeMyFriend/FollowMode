import sublime, sublime_plugin
import socket
import sys

HOST, PORT = "localhost", 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def send(data):
    try:
        sock.sendall(data + "\n")
    except Exception,e:
        print e
        sock.connect((HOST, PORT))
        sock.sendall(data + "\n")        
    finally:
        print "wow"

class eventslog(sublime_plugin.EventListener):  
    def on_load(self, view):
        send(view.substr(sublime.Region(0,view.size())) + "just got loaded")  
  
    def on_pre_save(self, view):  
        print view.file_name(), "is about to be saved"  
  
    def on_post_save(self, view):  
        print view.file_name(), "just got saved"  
          
    def on_new(self, view):  
        print "new file"  
  
    def on_modified(self, view):  
        print view.file_name(), "modified"  
  
    def on_activated(self, view):  
        print view.file_name(), "is now the active view"  
  
    def on_close(self, view):  
        print view.file_name(), "is no more"  
  
    def on_clone(self, view):  
        print view.file_name(), "just got cloned"  
