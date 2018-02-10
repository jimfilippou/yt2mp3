import cmd
import subprocess


class CLI(cmd.Cmd):
    """
    Class for defining the command interface.
    """

    def do_get(self, arg):
        """Gets a damn song."""
        x = arg if arg else raw_input("Hey, gimme the link of the youtube video...\n")
        print "Downloading - {}... Please wait.".format(x)
        proc = subprocess.Popen(
            [
              "youtube-dl",
              "--extract-audio", 
              "--audio-format", 
              "mp3", 
              "-f", 
              "bestaudio", 
              "--ignore-errors", 
              "-o", 
              "\"%(title)s.%(ext)s\"", 
              "--verbose",
              "{}".format(x)
            ], stdout=subprocess.PIPE, close_fds=True)

        # (out, err) = proc.communicate()
        # print "program output:", out

      
    def do_q(self, arg):
        print 'Well... bye!'
        return True
