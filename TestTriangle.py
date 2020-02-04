# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testScaleneTriangle(self):
    	self.assertEqual(classifyTriangle(2,3,4),'Scalene', '2,3,4 should be scalene')

    def testIsoscelesTriangleA(self):
    	self.assertEqual(classifyTriangle(2,3,3),'Isosceles', '2,3,3 should be isosceles')

    def testIsoscelesTriangleB(self):
    	self.assertEqual(classifyTriangle(3,2,3),'Isosceles', '3,2,3 should be isosceles')

    def testIsoscelesTriangleC(self):
    	self.assertEqual(classifyTriangle(2,2,3),'Isosceles', '2,2,3 should be isosceles')

    def testBoundariesA(self):
    	self.assertEqual(classifyTriangle(201,200,200),'InvalidInput', '201,200,200 should be an invalid triangle')

    def testBoundariesB(self):
    	self.assertEqual(classifyTriangle(200,201,200),'InvalidInput', '200,201,200 should be an invalid triangle')

    def testBoundariesC(self):
    	self.assertEqual(classifyTriangle(200,200,201),'InvalidInput', '200,200,201 should be an invalid triangle')

    def testBoundariesD(self):
    	self.assertEqual(classifyTriangle(0,1,1),'InvalidInput', '0,1,1 should be an invalid triangle')

    def testBoundariesE(self):
    	self.assertEqual(classifyTriangle(1,0,1),'InvalidInput', '1,0,1 should be an invalid triangle')

    def testBoundariesF(self):
    	self.assertEqual(classifyTriangle(1,1,0),'InvalidInput', '1,1,0 should be an invalid triangle')

    def testBoundariesG(self):
    	self.assertEqual(classifyTriangle("ABC",200,200),'InvalidInput', '"ABC",200,200 should be an invalid triangle')

    def testBoundariesH(self):
    	self.assertEqual(classifyTriangle(200,150.50,200),'InvalidInput', '200,150.50,200 should be an invalid triangle')

    def testBoundariesI(self):
    	self.assertEqual(classifyTriangle(200,200,150.50),'InvalidInput', '200,200,150.50 should be an invalid triangle')

    def testValidSidesA(self):
    	self.assertEqual(classifyTriangle(2,2,6),'NotATriangle', '2,2,6 is not a triangle')
    
    def testValidSidesB(self):
    	self.assertEqual(classifyTriangle(2,6,2),'NotATriangle', '2,6,2 is not a triangle')
    
    def testValidSidesC(self):
    	self.assertEqual(classifyTriangle(6,2,2),'NotATriangle', '6,2,2 is not a triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

