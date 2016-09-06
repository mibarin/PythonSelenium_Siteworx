import time
import httplib
import json
import os
import time
import sys
import unittest
import socket
import re
import __main__ as main
from selenium import webdriver
from selenium.common import exceptions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.action_chains import ActionChains
#import page
"""
class Timeout
Prints execution times for blocks of code.
Raises a timeout exception if the block took longer than the
specified timeout in seconds to complete.
"""
class Timeout():
    """
    Takes a timeout in seconds and name to indentify the block
    """
    def __init__(self, timeout, name):
        self.timeout = timeout
        self.name = name

    def __enter__(self):
        self.start = time.time()

    """
    On block exit check that the block executed within the timeout.
    If it did, print the time the block took to execute.
    If it did not, raise a timeout exception.
    """
    def __exit__(self, *args):
        runtime =  time.time() - self.start
        host = 'monitoring.siteworx.com'
        port = 2003
        try:
            sock = socket.socket()
            sock.connect((host,port))
        except (host):
            print "Pass connecting"
            pass
        if (runtime > self.timeout):
            msg = '"{0}" exceeded timeout of {1} seconds'.format(self.name , self.timeout)#name and timeout are from init
            data = '{0}.{1}.Latency {2} {3}\n'.format("_".join( main.__file__.split() ).split('.')[0] , "_".join( self.name.split() ) , self.timeout , int(time.time()))
            data = data + '{0}.{1}.Uptime 0 {2}\n'.format("_".join( main.__file__.split() ).split('.')[0] , "_".join( self.name.split() ) , int(time.time()))
            sock.send(data)
            print data
            raise Exception(msg)
        else:
            print '"{0}" took {1} seconds'.format(self.name , runtime)
            #data = '{0}.{1} {2} {3}\n'.format("_".join( main.__file__.split() ).split('.')[0] , "_".join( self.name.split() ) , int(runtime*1000) , int(time.time()))
            data =  '{0}.{1}.Latency {2} {3}\n'.format("_".join( main.__file__.split() ).split('.')[0] , "_".join( self.name.split() ) , runtime , int(time.time()))
            print sys.exc_info()
            if (sys.exc_info()[0]):
              data = data + '{0}.{1}.Uptime 0 {2}\n'.format("_".join( main.__file__.split() ).split('.')[0] , "_".join( self.name.split() ) , int(time.time()))
            else:
              data = data + '{0}.{1}.Uptime 1 {2}\n'.format("_".join( main.__file__.split() ).split('.')[0] , "_".join( self.name.split() ) , int(time.time()))
            sock.send(data)
            print data
        sock.close()

def log_errors(func):
    def wrapper(*arg):
        that = arg[0]
        that.e = None
        try:
            return func(*arg)
        except:
            that.e = sys.exc_info()
            that.driver.save_screenshot('error.png')
            raise
    return wrapper


class TestTools():

    """
    Wait for an element to exist.  Takes a lamdba function that finds the element
    and a timeout value. as an example
    """
    def wait_for(self, func, timeout):
        start_time = time.time()
        cur_time  = start_time
        while (cur_time - start_time < timeout):
            try:
              return func()
            except(exceptions.ElementNotVisibleException, exceptions.NoSuchElementException):
              pass
            cur_time = time.time()
            time.sleep(0.2)

        raise Exception("Timed out looking for element after %s seconds" % timeout)

    def is_showing(self, element, timeout):
        start_time = time.time()
        cur_time  = start_time
        while (cur_time - start_time < timeout):
            try:
                if element.is_displayed():
                    return
            except(exceptions.ElementNotVisibleException, exceptions.NoSuchElementException):
                pass
        cur_time = time.time()
        time.sleep(0.2)
        raise Exception("Timed out waiting for element to be visible after %s seconds" % timeout)

    def check_exists_by_class_name(self, classname):
        try:
            class_visible = self.driver.find_element_by_class_name(classname)
            if class_visible.is_displayed():
                return True
            else:
                return False
        except NoSuchElementException:
            return False
        return True

    def _testname(self):
        return self.id().split(".").pop()

    """
    check_ordered_items checks to see if elements of product list typically in Order History Details and in Order Confirmation.
    """
    def check_ordered_items(self, elements, items):
        """
        checks in ordered items lit in order history details.
        :param items: array that contains purchased product skus
        elements: elements of displayed order items
        :return:
        """
        i = 0
        for elem in elements:
            try:
                assert re.search(items[i], elem.find_element_by_tag_name('a').get_attribute('href')), "product link not found in order history details."
                i = i+1
            except:
                raise Exception(items[i] + " is not found.")
        return True