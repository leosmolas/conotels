from distutils.core import setup
import py2exe

setup(console=[{"script":"inst.py"}], options={"py2exe":{"includes":["sip"]}})