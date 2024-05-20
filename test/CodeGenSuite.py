import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    
    # * test cơ bản về hàm main và các hàm write
    def test_1(self):
        input = """
        func main ()
        begin
            writeNumber(1)
            writeBool(true)
            writeString("baokhanh")
        end
        """
        expect = "1.0\ntrue\nbaokhanh\n"
        self.assertTrue(TestCodeGen.test(input, expect, 500))
        
        input = """
        func main ()
        begin
            writeNumber(1.0)
            writeBool(false)
            writeString("")
        end
        """
        expect = "1.0\nfalse\n\n"
        self.assertTrue(TestCodeGen.test(input, expect, 501))
    
    #* test var
    def test_2(self):
        input = """
        number a <- 1
        func main ()
        begin
            writeNumber(a)
        end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 502))   
        
        input = """
        number a <- 1
        func main ()
        begin
            number a <- 2
            writeNumber(a)
        end
        """
        expect = "2.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 502))  
        
        input = """
        number a <- 1
        func main ()
        begin
            begin
                number a <- 2
            end
            writeNumber(a)
        end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 502))  
        
        input = """
        number a <- 1
        func main ()
        begin
            begin
                number a <- 2
                writeNumber(a)
            end
            writeNumber(a)
        end
        """
        expect = "2.0\n1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 502))  
        

        
    #* hàm experCall
    def test_3(self):
        input = """
        func foo(number a)
        begin
            return a
        end
        func main ()
        begin
            writeNumber(foo(2))
        end
        """
        expect = "2.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 503)) 
        
        
        input = """
        func foo(number a)
        begin
            return true
        end
        func main ()
        begin
            writeBool(foo(2))
        end
        """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 503)) 
        
        input = """
        func foo(string a)
        begin
            return a
        end
        func main ()
        begin
            writeString(foo("vo"))
        end
        """
        expect = "vo\n"
        self.assertTrue(TestCodeGen.test(input, expect, 503))  
        
        input = """
        func foo()
            return true
        func main ()
        begin
            bool a <- foo() ## true
            writeBool(a)
        end
        """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 503))  
        
        input = """
        func foo()
            return "baokhanh"
        func main ()
        begin
            string a <- foo() ## true
            writeString(a)
        end
        """
        expect = "baokhanh\n"
        self.assertTrue(TestCodeGen.test(input, expect, 503)) 
        
    #* test binary
    def test_4(self): 
        input = """
        func main ()
        begin
            writeNumber(1 + 1)
            writeNumber(1 - 1)
            writeNumber(1 * 2)
            writeNumber(1 / 2)
            writeNumber(7 % 3)
        end
        """
        expect = "2.0\n0.0\n2.0\n0.5\n1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 504))
        
        input = """
        func main ()
        begin
            writeNumber(1 + 1 + 1)
            writeNumber(1 + 1 * 3 - 1 * 2 / 2)
            writeNumber(2 * 3 % 2)
        end
        """
        expect = "3.0\n3.0\n0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 504))
        
        input = """
        func main ()
        begin
            writeBool(1 > 2) ## push -1
            writeBool(2 > 1) ## push 1
            writeBool(1 > 1) ## push 0
        end
        """
        expect = "false\ntrue\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 504))
        
        input = """
        func main ()
        begin
            writeBool(1 >= 2)
            writeBool(2 >= 1) 
            writeBool(1 >= 1) 
        end
        """
        expect = "false\ntrue\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 504))
        
        input = """
        func main ()
        begin
            writeBool(1 < 2) 
            writeBool(2 < 1) 
            writeBool(1 < 1) 
        end
        """
        expect = "true\nfalse\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 504))
        
        input = """
        func main ()
        begin
            writeBool(1 <= 2) 
            writeBool(2 <= 1) 
            writeBool(1 <= 1) 
        end
        """
        expect = "true\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 504))
        
        input = """
        func main ()
        begin
            writeBool(1 != 2) 
            writeBool(2 != 1) 
            writeBool(1 != 1) 
        end
        """
        expect = "true\ntrue\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 504))
        
        input = """
        func main ()
        begin
            writeBool(1 = 2) 
            writeBool(2 = 1) 
            writeBool(1 = 1) 
        end
        """
        expect = "false\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 504))
        
        input = """
        func main ()
        begin
            writeBool(true and true) 
            writeBool(true and false)
            writeBool(false and true) 
            writeBool(false and false)  
        end
        """
        expect = "true\nfalse\nfalse\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 504))
        
        input = """
        func main ()
        begin
            writeBool(true or true) 
            writeBool(true or false)
            writeBool(false or true) 
            writeBool(false or false)  
        end
        """
        expect = "true\ntrue\ntrue\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 504))
        
        input = """
        func main ()
        begin
            writeBool(true or true and false or true) 
        end
        """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 504))
        
        input = """
        func main ()
        begin
            writeString("bao" ... "khanh") 
        end
        """
        expect = "baokhanh\n"
        self.assertTrue(TestCodeGen.test(input, expect, 504)) 
        
        input = """
        func main ()
        begin
            writeBool("vo" == "tien") 
            writeBool("tien" == "tien")
        end
        """
        expect = "false\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 504))
        
        input = """
        func main ()
        begin
            writeBool(not not true) 
            writeBool(not true)
            writeBool(not false)
        end
        """
        expect = "true\nfalse\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 504))
        
        input = """
        func main ()
        begin
            writeNumber(--1) 
            writeNumber(-1)
        end
        """
        expect = "1.0\n-1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 504))

    #* vong for  
    def test_5(self): 
        input = """
        func main ()
        begin
            number i <- 0
            for i until i >= 2 by 1
                writeNumber(i)
        end
        """
        expect = "0.0\n1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 505))
        
        input = """
        func main ()
        begin
            number i <- 0
            for i until i > 2 by 2
                writeNumber(i)
        end
        """
        expect = "0.0\n2.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 505))
        
        input = """
        func main ()
        begin
            ## var i <- 0
            number i <- 0
            for i until i > 2 by 2
                writeNumber(i)
        end
        """
        expect = "0.0\n2.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 505))
        
        input = """
        func main ()
        begin
            ## var i <- 3
            number i <- 3
            for i until i > 2 by 2
                writeNumber(i)
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 505))
        
        input = """
        func main ()
        begin
            ## var i <- 0
            number i <- 0
            for i until i >= 2 by 1
            begin
                writeNumber(i)
                continue
                writeNumber(i)
            end
        end
        """
        expect = "0.0\n1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 505))
        
        input = """
        func main ()
        begin
            ## var i <- 0
            number i <- 0
            for i until i >= 2 by 1
            begin
                writeNumber(i)
                break
                writeNumber(i)
            end
        end
        """
        expect = "0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 505))
        
        input = """
        func main ()
        begin
            ## var i <- 0
            number i <- 0
            for i until i >= 2 by 1
                break
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 505))

    def test_9(self):
        input = """
            func main()
            begin
                if (true) writeNumber(1)
                else writeNumber(0)
            end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 509)) 

        input = """
            func main()
            begin
                if (2 > 3) writeNumber(1)
                else writeNumber(0)
            end
        """
        expect = "0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 509)) 

        input = """
            func main()
            begin
                if (2 = 2) writeNumber(1)
            end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 509)) 

    def test_3(self):
        input = """
        func foo()
        begin
            writeNumber(1.0)
            return
            writeNumber(1.0)
        end        
        func main ()
        begin
            foo()
        end
        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 503))   
        
        input = """
        func foo(string a)
        begin
            writeString(a)
        end        
        func main ()
        begin
            foo("baokhanh")
        end
        """
        expect = "baokhanh\n"
        self.assertTrue(TestCodeGen.test(input, expect, 503)) 
        
        input = """
        func foo(string a)   
        func main ()
        begin
            foo("baokhanh")
        end
        func foo(string a)
        begin
            writeString(a)
        end     
        """
        expect = "baokhanh\n"
        self.assertTrue(TestCodeGen.test(input, expect, 504)) 
        
        input = """
        func foo(string a, bool b)   
        func main ()
        begin
            foo("baokhanh", true)
        end
        func foo(string a, bool b)
        begin
            writeString(a)
            writeBool(true)
        end     
        """
        expect = "baokhanh\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 505)) 
        

        input = """
        func foo()
        begin
            writeString("1")
        end  
        func foo1()
        begin
            writeString("2")
        end  
        func main ()
        begin
            foo()
            foo1()
        end
   
        """
        expect = "1\n2\n"
        self.assertTrue(TestCodeGen.test(input, expect, 505)) 
    
    def test_1(self):
        input = """
        func main ()
        begin
            writeNumber(1)
            writeBool(true)
            writeString("baokhanh")
        end
        """
        expect = "1.0\ntrue\nbaokhanh\n"
        self.assertTrue(TestCodeGen.test(input, expect, 500))
    
    def test_2(self):
        input = """
        number a
    
        func main ()
        begin
            writeNumber(1)
            writeBool(true)
            writeString("baokhanh")
        end
        """
        expect = "1.0\ntrue\nbaokhanh\n"
        self.assertTrue(TestCodeGen.test(input, expect, 500))  
    
    def test_2(self): 
        
        input = """
        func main ()
        begin
            writeNumber(1 + 1 + 1)
            writeNumber(1 + 1 * 3 - 1 * 2 / 2)
            writeNumber(2 * 3 % 2)
        end
        """
        expect = "3.0\n3.0\n0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 502))
        