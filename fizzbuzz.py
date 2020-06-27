#https://repl.it/repls/BlindSupportiveMemorypool


class Test:
  @staticmethod
  def equals(name, condition):
    if condition:
      print(f"{name}: Ran and Passed!")
    else:
      print(f"{name}: Ran and Failed!")

  @staticmethod
  def notImplemented():
    raise Exception("Method not implemented!")

#Cost levels for implementation
#1 cost: Constant value, i.e., "1" or "2"
#2 cost: Variable assignment i.e number = "string"
#3 cost: Builtin function call, i.e., str(num)
#4 cost: if condition else (one elif doesnt cost anything, however each elif after incurs an exponential value)
#5 cost: looping
#6 cost: custom function

#implementation
class FizzBuzz:
	def __init__(self):
		pass
	def convert(self, number):
		if number % 3 == 0:
			return "Fizz"
		elif number % 5 == 0:
			return "Buzz"
		else:
			return str(number)




#tests:
#Step1) Create a hypothesis(or test)
#Step2) Perform the experiment(do not change the test otherwise its unfair)
#Step3) Capture your results(read what the test output says)
#Step4) Draw your conclusions based on what information you have 
class fizzBuzzShould:
	@staticmethod
	def convert_1_to_1():
		Test.equals("convert_1_to_1", "1" == FizzBuzz().convert(1))

	@staticmethod
	def convert_2_to_2():
		Test.equals("convert_2_to_2", "2" == FizzBuzz().convert(2))

	@staticmethod
	def convert_4_to_4():
		Test.equals("convert_4_to_4", "4" == FizzBuzz().convert(4))

	def convert_3_to_Fizz():
		Test.equals("convert_3_to_Fizz", "Fizz" == FizzBuzz().convert(3))

	def convert_6_to_Fizz():
		Test.equals("convert_6_to_Fizz", "Fizz" == FizzBuzz().convert(6))

	def convert_5_to_Buzz():
		Test.equals("convert_5_to_Buzz", "Buzz" == FizzBuzz().convert(5))

	def convert_10_to_Buzz():
		Test.equals("convert_10_to_Buzz", "Buzz" == FizzBuzz().convert(10))


fizzBuzzShould.convert_1_to_1()
fizzBuzzShould.convert_2_to_2()
fizzBuzzShould.convert_4_to_4()
fizzBuzzShould.convert_3_to_Fizz()
fizzBuzzShould.convert_6_to_Fizz()
fizzBuzzShould.convert_5_to_Buzz()
fizzBuzzShould.convert_10_to_Buzz()

#Homework - Create FizzBuzz 
