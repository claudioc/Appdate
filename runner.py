#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- Mode: Python -*-
# vi:si:et:sw=4:sts=4:ts=4

def runAll(path):
  import glob, os
  for filename in glob.glob(path + "/Bot_*.py"):
    # modulename = "bot_paperino"
    modulename = os.path.splitext(os.path.split(filename)[-1])[0]
    # classname = "Paperino"
    classname = modulename.split("bot_")[-1]
    # package = "path.bot_paperino"
    package = filename.replace("\\", "/").replace("/", ".")[:-3]
    mod = __import__(package)
    if classname in mod.__dict__[modulename].__dict__.keys():
      print classname
      bot = mod.__dict__[modulename].__dict__[classname]()
      if hasattr(bot, "run"):
        bot.setVerbose(True)
        projectData = bot.getProperties()
        if projectData['projectName'] == UNKNOWN_PROJECT:
          print "This project has not been given a name"
        else:
          if bot.isRunnable():
            rc = bot.run()
            if rc is not OK:
              print "An error occurred while running %s" % modulename
            else:
              releaseData = bot.getOutput()
              cursor = db.cursor()

              if releaseData['currentVersion'] == '':
                continue

              # Come hash utilizziamo il nome del progetto, piu' la sua versione
              datahash = md5.new(projectData['projectName'] + releaseData['currentVersion']).hexdigest()

              # 3 casi:
              # - il progetto non esiste
              # - il progetto ha una diversa hash (e` stato aggiornato)
              # - il progetto non ha una diversa hash (non e` stato aggiornato)

              # Si legge l'hash più recente del progetto
              cursor.execute("SELECT releaseDataHash, historyId FROM projects WHERE name=%s ORDER BY historyId DESC LIMIT 1", projectData['projectName'] )
              row = cursor.fetchone()
              try:
                twitter.update_status("#%s has been updated, new version is %s. Project history at %s" % (projectData['projectName'], releaseData['currentVersion'], "http://appdate.it/project/history/" + urllib.quote_plus(projectData['projectName'])))
              except Exception, e:
                pass
              if row is None:
                # Il progetto non esiste e lo inseriamo per la prima volta
                cursor.execute("""INSERT INTO projects 
                                         (name, projectData, historyId, historyDate, releaseData, releaseDataHash)
                                         VALUES (%s, %s, %s, now(), %s, %s)""", 
                                         (projectData['projectName'],
                                          lib.json.write(projectData),
                                          1,
                                          lib.json.write(releaseData),
                                          datahash))
              else:
                if row[0] != datahash:
                  # Le hash sono diverse, dunque il progetto è stato aggiornato e inseriamo una nuova history
                  cursor.execute("SELECT max(historyId) FROM projects WHERE name=%s", projectData['projectName'] )
                  row = cursor.fetchone()
                  cursor.execute("""INSERT INTO projects 
                                           (name, projectData, historyId, historyDate, releaseData, releaseDataHash)
                                           VALUES (%s, %s, %s, now(), %s, %s)""", 
                                           (projectData['projectName'],
                                            lib.json.write(projectData),
                                            row[0] + 1,
                                            lib.json.write(releaseData),
                                            datahash))
        #          if twitter is not None:
        #             try:
        #              twitter.update_status("#%s has been updated, new version is %s. Project history at %s" % (projectData['projectName'], releaseData['currentVersion'], "http://appdate.it/project/history/" + urllib.quote_plus(projectData['name'])))
        #            except Exception, e:
        #              pass
                else:
                  # Aggiorniamo i dati del progetto
                  cursor.execute("""UPDATE projects
                                       SET projectData=%s,
                                           releaseData=%s
                                     WHERE name=%s
                                       AND historyId=%s""",
                                       (lib.json.write(projectData),
                                        lib.json.write(releaseData),
                                        projectData['projectName'],
                                        row[1]))

if __name__ == "__main__":
  import sys
  import MySQLdb
  import md5
  import ConfigParser
  import urllib

  config = ConfigParser.ConfigParser()
  config.read('runner.ini')

  twitter = None
  if config.get("Twitter", "enabled") == "1":
    sys.path.append( "bots/lib" )
    import tweepy
    auth = tweepy.OAuthHandler(config.get("Twitter", "consumerKey"), config.get("Twitter", "consumerSecret"))
    auth.set_access_token(config.get("Twitter", "accessToken"), config.get("Twitter", "accessSecret"))
    twitter = tweepy.API(auth)

  db = MySQLdb.connect(host="localhost", 
                       user=config.get('Database', 'username'), 
                       passwd=config.get('Database', 'password'),
                       db=config.get('Database', 'dbname'))

  botsPath = 'bots'
  sys.path.append(botsPath)
  
  from lib.constants import *
  import lib.json

  runAll(botsPath)

