from distutils.core import setup
import py2exe

setup(console=[{"script":"main.py"}], options={"py2exe":{"includes":["sip","PyQt4.QtSql"]}})